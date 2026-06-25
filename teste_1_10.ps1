$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ProjectRoot
$env:PYTHONPATH = Join-Path $ProjectRoot "src"
$env:PYTHONUTF8 = "1"

Write-Host "`nExecutando testes 1 a 10 da pasta examples..." -ForegroundColor Cyan

for ($i = 1; $i -le 10; $i++) {
    $FilePath = Join-Path $ProjectRoot "examples\teste$i.jss"

    Write-Host "`n----------------------------------------" -ForegroundColor DarkGray
    Write-Host "Arquivo: teste$i.jss" -ForegroundColor White

    if (-not (Test-Path $FilePath)) {
        Write-Host "(arquivo nao encontrado)" -ForegroundColor Yellow
        continue
    }

    $Output = python .\main.py $FilePath 2>&1

    if ($Output) {
        $Output | ForEach-Object { Write-Host $_ }
    }
    else {
        Write-Host "(sem saida)"
    }
}

Write-Host "`nFinalizado." -ForegroundColor Green
