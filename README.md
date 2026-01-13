
# Arena Pinheiro - Backend

Sistema de gerenciamento para Arena Pinheiro, desenvolvido em Python com FastAPI e PostgreSQL. O sistema gerencia campos, reservas, comandas, produtos, estoque, compras, pagamentos e usuários.
Todas as tabelas possuem IDs automáticos (SERIAL) como chave primária. Os campos string são validados para evitar SQL injection.

---

## Índice
- Tecnologias Utilizadas
- Pré-requisitos
- Instalação
- Configuração
- Como Executar
- Estrutura do Projeto
- Documentação da API
- Funcionalidades
- Solução de Problemas

---

## 🛠️ Tecnologias Utilizadas
- FastAPI
- Uvicorn
- PostgreSQL
- psycopg2-binary
- Pydantic
- bcrypt (hash seguro de senhas)
- python-dotenv (carregamento automático do .env)
- Python 3.8+

---

## 📦 Pré-requisitos
- Python 3.8 ou superior
- PostgreSQL 12 ou superior
- pip

---

## 🚀 Instalação

1. Clone o projeto ou extraia o ZIP
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/macOS
   ```
3. Instale as dependências:
   ```bash
   pip install -r backend/requirements.txt
   pip install python-dotenv
   ```
4. Configure o banco de dados PostgreSQL:
    - Crie o banco:
       ```sql
       CREATE DATABASE arena_pinheiro;
       ```
    - Importe o script de tabelas (IDs automáticos, campos validados):
       ```bash
       psql -U postgres -d arena_pinheiro -f backend/Arena_Pinheiro.sql
       ```
5. Crie o arquivo `.env` na raiz do projeto:
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=arena_pinheiro
   DB_USER=postgres
   DB_PASSWORD=sua_senha
   API_HOST=0.0.0.0
   API_PORT=8000
   ```

---

## ⚙️ Configuração
- O backend carrega automaticamente as variáveis do `.env` usando python-dotenv.
- IDs de todas as entidades são gerados automaticamente pelo banco (SERIAL/IDENTITY). Não é necessário informar IDs ao cadastrar.
- Senhas são armazenadas com hash seguro (bcrypt). Os campos nome e senha de usuário aceitam até 255 caracteres.
- Todos os campos string relevantes são validados para evitar SQL injection e entradas maliciosas.

---


## 🎯 Como Executar

Execute o backend a partir da raiz do projeto:
```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Acesse:
- http://localhost:8000/docs — Documentação Swagger
- http://localhost:8000 — Mensagem de boas-vindas

---

## Estrutura do Projeto
```
Pinheiro-Arena/
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── run.py
│   ├── Arena_Pinheiro.sql
│   ├── requirements.txt
│   ├── routers/
│   └── schemas/
├── .env
├── README.md
```

---

## 📚 Documentação da API
- Swagger UI: http://localhost:8000/docs
- Todos os endpoints podem ser testados diretamente na interface.

---

## ✨ Funcionalidades
- CRUD completo para todas as entidades
- IDs automáticos (não informar ao cadastrar)
- Validação automática de dados (Pydantic)
- Validação de campos string para evitar SQL injection
- Documentação automática (Swagger/OpenAPI)
- CORS configurado
- Health check endpoint
- Senhas de usuários com hash seguro (bcrypt)

---


## 🐛 Solução de Problemas

- **Erro de conexão:** Verifique se o PostgreSQL está rodando e se o `.env` está correto.
- **Erro de autenticação:** Verifique usuário/senha no `.env`.
- **Erro de tabelas:** Execute novamente o script SQL.
- **Erro de encoding:** O backend já está configurado para UTF-8.
- **Porta ocupada:** Altere a porta no comando uvicorn e no `.env`.
- **Erro de valor muito longo:** Os campos nome e senha de usuário aceitam até 255 caracteres.

---


## 📝 Notas Importantes
- Não é necessário informar IDs ao cadastrar entidades.
- O arquivo `.env` não deve ser versionado (já está no .gitignore).
- Use o modo `--reload` apenas em desenvolvimento.
- Para produção, implemente autenticação JWT, HTTPS, logs e validação extra.
- Sempre valide entradas do usuário para evitar SQL injection e outros ataques.

---

## 👨‍💻 Desenvolvido com
- FastAPI
- PostgreSQL
- Python 3.8+
- HTML5/CSS3/JavaScript
- Pydantic
- Uvicorn

---

**Para dúvidas, consulte http://localhost:8000/docs quando a API estiver rodando.**
