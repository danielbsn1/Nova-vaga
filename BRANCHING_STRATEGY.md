# Estratégia de Branches

## Branches Principais

### `main` (Produção)
- Código em produção
- Apenas aceita PRs de `develop`
- Requer aprovação de code review
- CI/CD deve passar
- Deploy automático para produção

### `develop` (Desenvolvimento)
- Código em desenvolvimento
- Aceita PRs de `feature/*` e `bugfix/*`
- Requer CI/CD passar
- Deploy automático para staging

## Branches de Trabalho

### `feature/*` - Novas funcionalidades
```bash
git checkout develop
git pull origin develop
git checkout -b feature/nome-da-feature
```

### `bugfix/*` - Correções
```bash
git checkout develop
git pull origin develop
git checkout -b bugfix/nome-do-bug
```

### `hotfix/*` - Correções urgentes em produção
```bash
git checkout main
git pull origin main
git checkout -b hotfix/nome-do-hotfix
```

## Fluxo de Trabalho

### 1. Nova Feature
```bash
# Criar branch
git checkout -b feature/login

# Desenvolver e commitar
git add .
git commit -m "feat: adicionar login"

# Push
git push origin feature/login

# Abrir PR para develop
```

### 2. Release para Produção
```bash
# Após testes em develop, abrir PR de develop → main
# Após aprovação e merge, deploy automático para produção
```

### 3. Hotfix
```bash
# Criar branch de main
git checkout -b hotfix/corrigir-bug-critico

# Corrigir e commitar
git add .
git commit -m "fix: corrigir bug crítico"

# Push
git push origin hotfix/corrigir-bug-critico

# Abrir PR para main E develop
```

## Commits Semânticos

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Documentação
- `style:` Formatação
- `refactor:` Refatoração
- `test:` Testes
- `chore:` Manutenção
