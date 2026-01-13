
# Frontend (React + Vite)

## Como rodar

1. Pré-requisito: Node.js e npm instalados
2. Dentro da pasta `frontend`:

```bash
npm install
npm run dev
```

O frontend estará disponível em: http://localhost:5173

Para conectar com a API backend, crie um arquivo `.env` na pasta `frontend` com:

```
VITE_API_URL=http://localhost:8000/api
```

## Observações de integração

- O cadastro de produto exige o campo `id_admin_cadastrou` (atualmente fixo como 1 no frontend, ajuste para usar o id do admin logado quando implementar autenticação).
- Para registrar movimentação, o frontend busca o estoque do produto antes de criar a movimentação.
- Atualização e exclusão de produto não estão implementadas na API backend.
