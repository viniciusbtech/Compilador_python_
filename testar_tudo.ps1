$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot
$env:PYTHONPATH = Join-Path $ProjectRoot "src"

Write-Host "`n1) Executando testes automatizados com pytest..." -ForegroundColor Cyan
python -m pytest -v
if ($LASTEXITCODE -ne 0) {
    Write-Host "`nOs testes automatizados falharam." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "`n2) Executando casos manuais e comparando respostas..." -ForegroundColor Cyan
python .\scripts\run_lexer_cases.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "`nAlgum caso manual falhou." -ForegroundColor Red
    exit $LASTEXITCODE
}

Write-Host "`nTodos os testes passaram." -ForegroundColor Green
