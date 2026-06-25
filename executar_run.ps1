$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot
$env:PYTHONPATH = Join-Path $ProjectRoot "src"
$env:PYTHONUTF8 = "1"

$RunDir = Join-Path $ProjectRoot "run"

Write-Host "`nExecutando todos os arquivos .jss em: run\" -ForegroundColor Cyan

$Files = Get-ChildItem -Path $RunDir -Filter "*.jss" -File | Sort-Object Name

if (-not $Files) {
    Write-Host "`nNenhum arquivo .jss encontrado na pasta run\." -ForegroundColor Yellow
    exit 1
}

foreach ($File in $Files) {
    Write-Host "`n----------------------------------------" -ForegroundColor DarkGray
    Write-Host "Arquivo: $($File.Name)" -ForegroundColor White

    $Output = python .\main.py $File.FullName 2>&1

    if ($Output) {
        $Output | ForEach-Object { Write-Host $_ }
    }
    else {
        Write-Host "(sem saida)"
    }
}

Write-Host "`nFinalizado." -ForegroundColor Green
