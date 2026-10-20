<#
.SYNOPSIS
  校验 Obsidian 仓库中的 WikiLink 是否都能解析。
.DESCRIPTION
  默认以脚本上一级目录（仓库根）为根，扫描全部 .md 文件中的 [[...]] 链接：
  - 含 "/" 的目标：按仓库相对路径解析，自动补 .md 后缀。
  - 纯文件名目标：按全库唯一文件名解析，多个同名文件视为歧义。
  输出未解析清单，末尾打印 "unresolved links: N"；N > 0 时退出码为 1，否则为 0。
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string]$Root
)

if (-not $Root) {
    $Root = Split-Path -Parent $PSScriptRoot
}
$Root = (Resolve-Path -LiteralPath $Root).Path

$files = Get-ChildItem -Recurse -File -Filter *.md -Path $Root

$byName = @{}
foreach ($f in $files) {
    $key = [IO.Path]::GetFileNameWithoutExtension($f.Name).ToLowerInvariant()
    if (-not $byName.ContainsKey($key)) { $byName[$key] = @() }
    $byName[$key] += $f.FullName
}

$pattern = '\[\[([^\]\|#]+)(#[^\]\|]+)?(\|[^\]]+)?\]\]'
$unresolved = @()

foreach ($f in $files) {
    $rel = $f.FullName.Substring($Root.Length).TrimStart('\')
    $text = [IO.File]::ReadAllText($f.FullName)
    foreach ($m in [regex]::Matches($text, $pattern)) {
        $target = $m.Groups[1].Value.Trim().TrimEnd('\')
        if ($target -eq '' -or $target -match '^[a-zA-Z][a-zA-Z0-9+.-]*://') { continue }

        if ($target.Contains('/')) {
            $p = Join-Path $Root ($target.Replace('/', '\'))
            if (-not $p.EndsWith('.md')) { $p += '.md' }
            if (-not (Test-Path -LiteralPath $p)) {
                $unresolved += ("{0} -> {1}" -f $rel, $target)
            }
        }
        else {
            $key = $target.ToLowerInvariant()
            if (-not $byName.ContainsKey($key)) {
                $unresolved += ("{0} -> {1}" -f $rel, $target)
            }
            elseif ($byName[$key].Count -gt 1) {
                $unresolved += ("{0} -> {1} (ambiguous: {2} matches)" -f $rel, $target, $byName[$key].Count)
            }
        }
    }
}

foreach ($u in $unresolved) { Write-Output $u }
Write-Output ("unresolved links: " + $unresolved.Count)
if ($unresolved.Count -gt 0) { exit 1 }
exit 0

