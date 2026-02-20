#!/bin/bash

echo " Configurando projeto Nova Vaga..."


git init

git checkout -b develop
s
git add .

git commit -m "chore: initial commit"


git checkout -b main

echo " Git configurado!"
echo ""
echo " Próximos passos:"
echo ". Criar repositório no GitHub"
echo ". git remote add origin https://github.com/seu-usuario/nova-vaga.git"
echo ". git push -u origin main"
echo ". git push -u origin develop"
echo ""
echo " Configure proteção de branches no GitHub:"
echo "   Settings → Branches → Add rule"
echo "   - Branch: main"
echo "   -  Require pull request reviews before merging"
echo "   - Require status checks to pass"
echo ""
echo "   - Branch: develop"
echo "   -  Require status checks to pass"
