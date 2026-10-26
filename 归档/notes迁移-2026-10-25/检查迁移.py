"""Check this migration's explicit file list, links, snapshots and image hashes.

Uses only the Python standard library. Does not execute operational note examples.
Does not restore historical files or change the old notes directory.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[1]
MANIFEST = HERE / '文件迁移清单.json'
REPORT = HERE / '检查结果.json'
NOTE_PATHS = [
    '笔记总览.md',
    '归档/notes迁移-2026-10-25/迁移记录.md',
    '硬件开发/Altium Designer/Altium Designer学习总览.md',
    '硬件开发/Altium Designer/01-工程与原理图库.md',
    '硬件开发/Altium Designer/02-原理图绘制与检查.md',
    '硬件开发/Altium Designer/03-PCB封装与板框.md',
    '硬件开发/Altium Designer/04-PCB布局与布线.md',
    '硬件开发/ESP32/ESP32入门与ST7735显示.md',
    '系统与运维/00-系统与运维索引.md',
    '系统与运维/Windows与Ubuntu双系统问题.md',
    '系统与运维/Docker部署MySQL.md',
    '系统与运维/frp内网穿透.md',
    '生活记录/想去的餐厅.md',
    '算法小记/00-索引/算法资料入口.md',
    '算法小记/03-算法/动态规划/00-记忆化搜索.md',
    '算法小记/00-索引/算法总览.md',
    '算法小记/03-算法/动态规划/00-DP总览.md',
]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def check() -> dict:
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    source = Path(manifest['source_directory'])
    records = manifest['files']
    archive = HERE / manifest['snapshot_file']
    require(len(records) == 53, 'Unexpected source count')
    require(sum(r['source'].endswith('.md') for r in records) == 45, 'Unexpected Markdown count')
    require(sum(r['source'].endswith('.png') for r in records) == 7, 'Unexpected image count')
    require(sha256(archive.read_bytes()) == manifest['snapshot_sha256'], 'Snapshot file hash mismatch')
    archived_texts = []
    with zipfile.ZipFile(archive) as snapshot:
        require(snapshot.testzip() is None, 'Snapshot CRC failure')
        require(set(snapshot.namelist()) == {r['snapshot_entry'] for r in records}, 'Snapshot member mismatch')
        require(all('/.git/' not in n for n in snapshot.namelist()), 'Git history must not be archived')
        for record in records:
            payload = snapshot.read(record['snapshot_entry'])
            require(sha256(payload) == record['snapshot_sha256'], 'Snapshot entry mismatch: ' + record['source'])
            require(len(payload) == record['snapshot_bytes'], 'Snapshot byte count mismatch')
            if not record['redacted']:
                require(record['source_sha256'] == record['snapshot_sha256'], 'Unexpected source transformation')
            if record['source'].endswith('.md'):
                payload.decode('utf-8-sig', errors='strict')
                archived_texts.append(payload)
            if record['source'] == '建站记录/docker-mysql.md':
                values = re.findall(rb'MYSQL_ROOT_PASSWORD=([^\s]+)', payload)
                require(len(values) == 2 and all(v == b'<REDACTED>' for v in values), 'Snapshot credential redaction failure')
            for target in record['organized_targets']:
                require((VAULT / target).exists(), 'Organized target missing: ' + target)
    require(sum(r['redacted'] for r in records) == 1, 'Unexpected redacted file count')

    image_records = {r['source']: r for r in records if r['source'].endswith('.png')}
    image_map = manifest['attachment_mapping']
    require(set(image_map) == set(image_records), 'Image map coverage mismatch')
    for relative, target in image_map.items():
        image = VAULT / target
        require(image.is_file(), 'Image target missing: ' + target)
        require(sha256(image.read_bytes()) == image_records[relative]['source_sha256'], 'Image content mismatch')

    texts = {}
    links_checked = 0
    for relative in NOTE_PATHS:
        note = VAULT / relative
        payload = note.read_bytes()
        text = payload.decode('utf-8-sig', errors='strict')
        require('\ufffd' not in text, 'Unicode replacement character found: ' + relative)
        texts[relative] = text
        # TOML array-of-tables such as [[proxies]] inside fences are not WikiLinks.
        link_text = re.sub(r'(?ms)^```[^\n]*\n.*?^```[ \t]*$', '', text)
        for match in re.finditer(r'\[\[([^\]]+)\]\]', link_text):
            target = match.group(1).replace('\\|', '|').split('|', 1)[0].split('#', 1)[0].strip()
            if not target or '://' in target:
                continue
            candidate_name = target if Path(target).suffix else target + '.md'
            candidates = [VAULT / candidate_name, note.parent / candidate_name]
            if relative.startswith('算法小记/'):
                candidates += [VAULT / '算法小记' / candidate_name, VAULT / '算法小记/00-索引' / candidate_name]
            require(any(p.is_file() for p in candidates), 'Unresolved link in ' + relative + ': ' + target)
            links_checked += 1

    memo = texts['算法小记/03-算法/动态规划/00-记忆化搜索.md']
    required_headings = ['适用场景', '核心思想', '状态定义', '转移方程', '初始化与边界', '遍历顺序', '空间优化', '复杂度', '常见错误', '典型题目']
    require(all('## ' + heading in memo for heading in required_headings), 'Memoization concept template incomplete')
    require(all(target in '\n'.join(texts.values()) for target in image_map.values()), 'An image is not referenced')

    source_hashes_checked = 0
    credential_scan = 'snapshot assignments redacted; source unavailable for value comparison'
    if source.exists():
        result = subprocess.run(
            ['git', '-c', 'safe.directory=D:/projects/notes', '-C', str(source),
             'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
            check=True, capture_output=True,
        )
        current = {p.decode('utf-8') for p in result.stdout.split(b'\0') if p and (source / p.decode('utf-8')).is_file()}
        require(current == {r['source'] for r in records}, 'Source file set changed since snapshot')
        for record in records:
            require(sha256((source / record['source']).read_bytes()) == record['source_sha256'], 'Source changed since snapshot: ' + record['source'])
            source_hashes_checked += 1
        raw_mysql = (source / '建站记录/docker-mysql.md').read_bytes()
        values = re.findall(rb'MYSQL_ROOT_PASSWORD=([^\s]+)', raw_mysql)
        real_values = [v for v in values if v != b'***' and v != b'<REDACTED>']
        require(len(real_values) == 1, 'Unexpected legacy credential pattern')
        new_payloads = [text.encode('utf-8') for text in texts.values()]
        new_payloads += [MANIFEST.read_bytes(), (HERE / '构建迁移快照.py').read_bytes(), Path(__file__).read_bytes()]
        require(not any(secret in payload for secret in real_values for payload in new_payloads + archived_texts), 'Legacy credential remains in migration artifacts')
        credential_scan = 'passed; legacy credential absent from organized text and snapshot'

    report = {
        'status': 'passed',
        'source_existing_file_count': 53,
        'source_markdown_count': 45,
        'source_png_count': 7,
        'new_markdown_notes': 15,
        'existing_markdown_notes_updated': 2,
        'organized_markdown_files_checked': len(NOTE_PATHS),
        'wikilink_occurrences_checked': links_checked,
        'unresolved_new_or_updated_note_links': 0,
        'image_copies_sha256_match': len(image_map),
        'snapshot_crc_and_53_entry_hashes': 'passed',
        'snapshot_sha256': manifest['snapshot_sha256'],
        'redacted_source_files': 1,
        'source_directory_exists_at_check': source.exists(),
        'unchanged_source_file_hashes_checked': source_hashes_checked,
        'credential_check': credential_scan,
        'operational_examples_executed': False,
        'external_links_rechecked': False,
        'obsidian_rendering_checked': False,
    }
    if REPORT.exists():
        json.loads(REPORT.read_text(encoding='utf-8'))
    with REPORT.open('w', encoding='utf-8', newline='\n') as output:
        json.dump(report, output, ensure_ascii=False, indent=2)
        output.write('\n')
    return report


def bundle() -> dict:
    """Package only files created or modified by this migration, preserving paths."""
    manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
    report = json.loads(REPORT.read_text(encoding='utf-8'))
    require(report['status'] == 'passed', 'Run migration checks before packaging')
    relative_paths = list(NOTE_PATHS) + list(manifest['attachment_mapping'].values())
    relative_paths += [str(path.relative_to(VAULT)).replace('\\', '/') for path in [
        MANIFEST, REPORT, HERE / manifest['snapshot_file'],
        HERE / '构建迁移快照.py', Path(__file__).resolve(),
    ]]
    require(len(relative_paths) == len(set(relative_paths)), 'Duplicate package entry')
    payloads = [(relative, (VAULT / relative).read_bytes()) for relative in relative_paths]
    target = HERE / 'notes迁移成果-2026-10-25.zip'
    with zipfile.ZipFile(target, 'x', compression=zipfile.ZIP_DEFLATED) as package:
        for relative, payload in payloads:
            package.writestr(relative, payload)
    with zipfile.ZipFile(target) as package:
        require(package.testzip() is None, 'Delivery package CRC failure')
        require(set(package.namelist()) == set(relative_paths), 'Delivery package entry mismatch')
        for relative, payload in payloads:
            require(sha256(package.read(relative)) == sha256(payload), 'Delivery package content mismatch')
    return {'package': str(target), 'file_count': len(relative_paths),
            'sha256': sha256(target.read_bytes()), 'crc_and_entry_hashes': 'passed'}


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    if sys.argv[1:] == ['--bundle']:
        result = bundle()
    elif not sys.argv[1:]:
        result = check()
    else:
        raise SystemExit('Usage: python 检查迁移.py [--bundle]')
    print(json.dumps(result, ensure_ascii=False, indent=2))
