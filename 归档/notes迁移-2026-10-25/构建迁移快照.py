"""Archive current notes files without Git history; redact legacy MySQL assignments.

Run once with Python 3; existing output files are never overwritten.
The default paths refer to this one-off migration, not a general backup service.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import zipfile

SOURCE = Path('D:/projects/notes')
VAULT = Path('D:/Users/maris/Documents/Obsidian Vault')
OUTPUT = Path(__file__).resolve().parent
ARCHIVE = OUTPUT / 'notes现存文件快照.zip'
MANIFEST = OUTPUT / '文件迁移清单.json'


def organized_targets(relative: str) -> tuple[list[str], str]:
    if relative.startswith('软硬件/AD笔记/images/'):
        return ['硬件开发/Altium Designer/附件/'], 'attachment'
    if relative.startswith('软硬件/AD笔记/'):
        number = int(relative.split('/')[-1].split('.')[0])
        if 3 <= number <= 7:
            name = '01-工程与原理图库'
        elif 8 <= number <= 19:
            name = '02-原理图绘制与检查'
        elif 24 <= number <= 28:
            name = '03-PCB封装与板框'
        elif number in (30, 31, 32, 33, 34, 37, 38):
            name = '04-PCB布局与布线'
        else:
            raise ValueError('Unexpected AD source: ' + relative)
        return ['硬件开发/Altium Designer/' + name + '.md'], 'merged-note'
    if relative.startswith('软硬件/ESP32/'):
        return ['硬件开发/ESP32/ESP32入门与ST7735显示.md'], 'merged-note'
    if relative.startswith('双系统问题记录/'):
        return ['系统与运维/Windows与Ubuntu双系统问题.md'], 'merged-note'
    if relative == '建站记录/docker-mysql.md':
        return ['系统与运维/Docker部署MySQL.md'], 'redacted-and-organized'
    if relative == '建站记录/frp内网穿透.md':
        return ['系统与运维/frp内网穿透.md'], 'organized-note'
    if relative.startswith('建站记录/'):
        return ['系统与运维/00-系统与运维索引.md'], 'merged-reference'
    if relative == '算法/dp/记忆优化搜索.md':
        return [
            '算法小记/03-算法/动态规划/00-记忆化搜索.md',
            '算法小记/00-索引/算法资料入口.md',
        ], 'concept-extracted-practice-list-snapshot-only'
    if relative == '算法/target.md':
        return ['算法小记/00-索引/算法资料入口.md'], 'merged-reference'
    if relative == '算法/线段树/线段树.md':
        return ['算法小记/00-索引/线段树路线图.md'], 'empty-note-reuses-existing-roadmap'
    if relative == '目标饭店/目标饭店.md':
        return ['生活记录/想去的餐厅.md'], 'organized-note'
    if relative.startswith('软件链接/'):
        return [], 'snapshot-only-unverified-bookmark'
    if relative == 'README.md':
        return ['笔记总览.md'], 'replaced-empty-index'
    if relative == 'show':
        return [], 'snapshot-only-empty-file'
    raise ValueError('Unmapped current file: ' + relative)


def build() -> dict:
    if ARCHIVE.exists() or MANIFEST.exists():
        raise FileExistsError('Snapshot or manifest already exists; refusing to overwrite')
    result = subprocess.run(
        ['git', '-c', 'safe.directory=D:/projects/notes', '-C', str(SOURCE),
         'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
        check=True, capture_output=True,
    )
    paths = sorted(set(p.decode('utf-8') for p in result.stdout.split(b'\0') if p))
    records = []
    ignored_deleted = 0
    # Prepare every record before creating the archive, so unknown input fails early.
    payloads = []
    for relative in paths:
        path = SOURCE / relative
        if not path.exists():
            ignored_deleted += 1
            continue
        if not path.is_file() or path.is_symlink():
            raise ValueError('Only regular current files are allowed: ' + relative)
        raw = path.read_bytes()
        payload = raw
        redacted_assignments = 0
        if relative == '建站记录/docker-mysql.md':
            payload, redacted_assignments = re.subn(
                rb'(?<=MYSQL_ROOT_PASSWORD=)[^\s]+', b'<REDACTED>', raw,
            )
            if redacted_assignments != 2:
                raise ValueError('Unexpected number of legacy MySQL assignments')
            if any(value != b'<REDACTED>' for value in re.findall(
                rb'MYSQL_ROOT_PASSWORD=([^\s]+)', payload,
            )):
                raise ValueError('Legacy MySQL assignment redaction failed')
        destinations, disposition = organized_targets(relative)
        entry = 'notes/' + relative
        payloads.append((entry, payload))
        records.append({
            'source': relative,
            'source_bytes': len(raw),
            'source_sha256': hashlib.sha256(raw).hexdigest(),
            'snapshot_entry': entry,
            'snapshot_bytes': len(payload),
            'snapshot_sha256': hashlib.sha256(payload).hexdigest(),
            'redacted': raw != payload,
            'password_assignments_redacted': redacted_assignments,
            'organized_targets': destinations,
            'disposition': disposition,
        })
    with zipfile.ZipFile(ARCHIVE, 'x', compression=zipfile.ZIP_DEFLATED) as snapshot:
        for entry, payload in payloads:
            snapshot.writestr(entry, payload)
    with zipfile.ZipFile(ARCHIVE) as snapshot:
        if snapshot.testzip() is not None:
            raise ValueError('Snapshot CRC check failed')
        if len(snapshot.namelist()) != len(records):
            raise ValueError('Snapshot member count mismatch')
        for record in records:
            payload = snapshot.read(record['snapshot_entry'])
            if hashlib.sha256(payload).hexdigest() != record['snapshot_sha256']:
                raise ValueError('Snapshot entry hash mismatch: ' + record['source'])
            if not record['redacted'] and record['source_sha256'] != record['snapshot_sha256']:
                raise ValueError('Unexpected snapshot content change: ' + record['source'])
    manifest = {
        'schema_version': 1,
        'migration_date': '2026-10-25',
        'source_directory': str(SOURCE),
        'scope': 'current-working-tree-only; no .git history; deleted entries are not restored',
        'source_existing_file_count': len(records),
        'deleted_tracked_entries_ignored': ignored_deleted,
        'markdown_count': sum(r['source'].endswith('.md') for r in records),
        'png_count': sum(r['source'].endswith('.png') for r in records),
        'snapshot_file': ARCHIVE.name,
        'snapshot_sha256': hashlib.sha256(ARCHIVE.read_bytes()).hexdigest(),
        'snapshot_crc_check': 'passed',
        'snapshot_entry_hash_check': 'passed',
        'redacted_file_count': sum(r['redacted'] for r in records),
        'files': records,
    }
    with MANIFEST.open('x', encoding='utf-8', newline='\n') as output:
        json.dump(manifest, output, ensure_ascii=False, indent=2)
        output.write('\n')
    return {key: value for key, value in manifest.items() if key != 'files'}


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print(json.dumps(build(), ensure_ascii=False, indent=2))
