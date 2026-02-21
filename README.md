# Nova Vaga - Plataforma de Vagas e Freelancers

## 🐳 Executar com Docker

### Pré-requisitos
- Docker
- Docker Compose

### Iniciar aplicação

```bash
# Subir todos os containers
docker-compose up -d

# Ver logs
docker-compose logs -f

# Parar containers
docker-compose down

# Parar e remover volumes (limpa banco de dados)
docker-compose down -v
```

### Acessar aplicação
- Backend API: http://localhost:8000
- Documentação API: http://localhost:8000/docs
- PostgreSQL: localhost:5432

### Comandos úteis

```bash
# Reconstruir containers após mudanças
docker-compose up -d --build

# Executar migrations manualmente
docker-compose exec backend alembic upgrade head

# Acessar shell do backend
docker-compose exec backend bash

# Acessar PostgreSQL
docker-compose exec postgres psql -U bancoaps -d novavaga

# Ver logs de um serviço específico
docker-compose logs -f backend
docker-compose logs -f postgres
```

## 🔧 Desenvolvimento Local (sem Docker)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

## 📝 Variáveis de Ambiente

Copie `.env.example` para `.env` e configure suas chaves:

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas credenciais reais do Stripe e outras configurações.
