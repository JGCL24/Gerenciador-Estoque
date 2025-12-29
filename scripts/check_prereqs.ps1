# Check prerequisites for Gerenciador de Estoque (Windows PowerShell)
$ok = $true

Write-Host "Checking prerequisites..." -ForegroundColor Cyan

# Check Python
$py = Get-Command python -ErrorAction SilentlyContinue
if (-not $py) { Write-Host "Python not found. Install Python 3.10+ from https://www.python.org/" -ForegroundColor Red; $ok = $false } else {
  $ver = python -c "import sys; print('.'.join(map(str, sys.version_info[:3])))"
  Write-Host "Python version: $ver"
  $parts = $ver.Split('.') | ForEach-Object {[int]$_}
  if ($parts[0] -lt 3 -or ($parts[0] -eq 3 -and $parts[1] -lt 10)) { Write-Host "Python 3.10+ is required." -ForegroundColor Yellow; $ok = $false }
}

# Check pip
$pip = Get-Command pip -ErrorAction SilentlyContinue
if (-not $pip) { Write-Host "pip not found. Run: python -m ensurepip --upgrade" -ForegroundColor Yellow }

# Check Node
$node = Get-Command node -ErrorAction SilentlyContinue
if (-not $node) { Write-Host "Node.js not found. Install Node.js (LTS >= 16) from https://nodejs.org/" -ForegroundColor Red; $ok = $false } else { $nv = node -v; Write-Host "Node: $nv" }

# Check npm
$npm = Get-Command npm -ErrorAction SilentlyContinue
if (-not $npm) { Write-Host "npm not found. It usually comes with Node.js." -ForegroundColor Red; $ok = $false } else { $nv = npm -v; Write-Host "npm: $nv" }

if ($ok) { Write-Host "All required tools are installed." -ForegroundColor Green } else { Write-Host "Some prerequisites are missing. Follow the messages above to install them." -ForegroundColor Red; exit 2 }
