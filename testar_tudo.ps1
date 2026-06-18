$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot
$env:PYTHONPATH = Join-Path $ProjectRoot "src"
$env:PYTHONUTF8 = "1"

Write-Host "`n1) Executando testes automatizados com pytest..." -ForegroundColor Cyan
python -m pytest -v
if ($LASTEXITCODE -ne 0) {
    Write-Host "`nOs testes automatizados falharam." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "`n2) Executando arquivos de teste da pasta examples..." -ForegroundColor Cyan

$ExampleFiles = Get-ChildItem -Path (Join-Path $ProjectRoot "examples") -Filter "teste*.jss" -File |
    Where-Object { $_.BaseName -match '^teste\d+$' } |
    Sort-Object { [int]($_.BaseName -replace '^teste', '') }

if (-not $ExampleFiles) {
    Write-Host "`nNenhum arquivo teste*.jss foi encontrado na pasta examples." -ForegroundColor Yellow
    exit 1
}

foreach ($File in $ExampleFiles) {
    Write-Host "`n----------------------------------------" -ForegroundColor DarkGray
    Write-Host "Arquivo: $($File.Name)" -ForegroundColor White

    $Source = Get-Content -LiteralPath $File.FullName -Raw
    $Output = $Source | python .\main.py 2>&1

    if ($Output) {
        $Output | ForEach-Object { Write-Host $_ }
    }
    else {
        Write-Host "(sem saida)"
    }
}

Write-Host "`nExecucao dos testes finalizada." -ForegroundColor Green
