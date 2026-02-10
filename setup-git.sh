#!/bin/bash

echo "🚀 Configurando projeto Nova Vaga..."

# Inicializar git
git init

# Criar branch develop
git checkout -b develop

# Adicionar todos os arquivos
git add .

# Commit inicial
git commit -m "chore: initial commit"

# Criar branch main
git checkout -b main

echo "✅ Git configurado!"
echo ""
echo "📋 Próximos passos:"
echo "1. Criar repositório no GitHub"
echo "2. git remote add origin https://github.com/seu-usuario/nova-vaga.git"
echo "3. git push -u origin main"
echo "4. git push -u origin develop"
echo ""
echo "🔒 Configure proteção de branches no GitHub:"
echo "   Settings → Branches → Add rule"
echo "   - Branch: main"
echo "   - ✓ Require pull request reviews before merging"
echo "   - ✓ Require status checks to pass"
echo ""
echo "   - Branch: develop"
echo "   - ✓ Require status checks to pass"
