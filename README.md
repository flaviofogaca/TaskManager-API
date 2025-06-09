# TaskManager API

Uma API REST desenvolvida com **FastAPI** para gerenciamento de tarefas, com autenticação via **OAuth2** e geração de **JWT**.

> A autenticação protege as rotas com tokens `Bearer`, garantindo acesso seguro a dados sensíveis.

---

## Funcionalidades

- Listagem de tarefas públicas (`GET /tasks`)
- Rota protegida com autenticação JWT
- Autenticação com `username` e `password` usando `OAuth2PasswordBearer`
- Geração de token com `POST /auth/token`
- Documentação interativa com **Swagger UI** e **ReDoc**

---

## Tecnologias utilizadas

- [Python 3.11+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Python-Jose](https://python-jose.readthedocs.io/)
- [Passlib (bcrypt)](https://passlib.readthedocs.io/)

---

## Como executar localmente

1. Clone o repositório:


git clone https://github.com/seu-usuario/taskmanager-api.git
cd taskmanager-api

2. Crie e Ative um ambiente virtual:


python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows

3. Instale as dependências:


pip install -r requirements.txt

4. Execute a aplicação:


uvicorn main:app --reload

5. Acesse a documentação interativa:

- http://127.0.0.1:8000/docs – Swagger UI
- http://127.0.0.1:8000/redoc – ReDoc

## Teste de autenticação

1. Use o POST /auth/token com os seguintes dados no corpo (x-www-form-urlencoded):

username=flavio
password=123456

2. Copie o Token gerado.

3. Vá até a rota /tasks, clique em Authorize, cole o token com prefixo Bearer.


## Estrutura de pastas

TaskManager-API/
- ├── app/
- │ ├── init.py
- │ ├── auth.py
- │ ├── database.py
- │ ├── models.py
- │ ├── schemas.py
- │ └── tasks.py
- ├── main.py
- ├── tasks.db
- ├── README.md
- └── requirements.txt

## Licença 

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/flaviofogaca/TaskManager-API/blob/main/LICENSE) para mais detalhes.
