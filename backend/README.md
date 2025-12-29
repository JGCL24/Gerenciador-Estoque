# Backend (FastAPI) - Gerenciador de Estoque

Rápido para rodar:

1. Pré-requisitos: Python 3.10+
2. No PowerShell, dentro da pasta `backend`:

```powershell
# criar e ativar ambiente virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# instalar dependências
pip install -r requirements.txt

# iniciar a API (modo desenvolvimento)
python run.py
```

Ao executar `python run.py` o console exibirá os links da aplicação e da documentação. Exemplo de saída:

```
Starting Gerenciador de Estoque (development mode)
App: http://localhost:8000
Docs: http://localhost:8000/docs
```

- API: `http://localhost:8000`
- Docs: `http://localhost:8000/docs`

Observação: Banco padrão: SQLite em `backend/database.db`.

Você pode executar `python check_prereqs.py` dentro de `backend/` para checar rapidamente se os pacotes Python necessários estão instalados.

**Migração do campo `min_quantity`:** o backend tenta adicionar automaticamente a coluna `min_quantity` em bases antigas; se preferir recriar o DB, apague `backend/database.db` durante desenvolvimento e reinicie a API.

**Verificação de pré-requisitos:** use `scripts\check_prereqs.ps1` (Windows PowerShell) ou `scripts/check_prereqs.sh` (macOS/Linux) para checar se Python / Node / npm estão instalados.
