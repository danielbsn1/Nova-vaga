# Backend API - Nova Vaga

## 🚀 Tecnologias
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Stripe

## 📋 Pré-requisitos
- Python 3.11+
- PostgreSQL

## 🔧 Instalação
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

## ⚙️ Configuração
Configure o `.env` com suas credenciais

## 🗄️ Migrations
```bash
alembic upgrade head
```

## ▶️ Executar
```bash
uvicorn app.main:app --reload
```

API disponível em: http://localhost:8000
Docs: http://localhost:8000/docs
