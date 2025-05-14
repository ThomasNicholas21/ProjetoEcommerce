# 🛒 E-commerce - Django

Este é um projeto de e-commerce desenvolvido com **Python** e **Django**, utilizando **MySQL** como banco de dados e **Docker** para orquestração dos serviços. O sistema conta com gestão de pedidos, carrinho de compras com sessões, controle de estoque via signals e um painel administrativo customizável via Django Admin.

---

## 📦 Funcionalidades

- Carrinho de compras com sessões
- Atualização automática de estoque via Django Signals
- Painel administrativo customizável
- Sistema de pedidos com status e controle
- Template base com componentes reutilizáveis (partials)
- Context processors para informações globais
- Filtros personalizados com Template Tags
- Estrutura pronta para integração futura com gateway de pagamento

---

## 📹 Demonstração

[▶️ Assista no YouTube](https://youtu.be/CKzkPdsArB4"target="_blank) — (Ctrl + clique para abrir em nova aba)

---

## 🚀 Tecnologias Utilizadas

- Python 3.11+
- Django 4.2.x
- MySQL 8.x
- Docker & Docker Compose
- HTML/CSS com Django Templates
- Django Signals
- Context Processors & Template Tags

---

## ⚙️ Como Executar o Projeto

### 1. Clonar o Repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

---

### 2. Configurar Arquivo `.env`

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```env
DB_ENGINE="django.db.backends.mysql"
MYSQL_DATABASE=seu_banco
MYSQL_USER=seu_usuario
MYSQL_PASSWORD=sua_senha
MYSQL_ROOT_PASSWORD=rootpassword

SECRET_KEY="sua_secret_key"
# 0 False, 1 True
DEBUG="1"
# Comma Separated values
ALLOWED_HOSTS="127.0.0.1, 0.0.0.0, localhost"
```

---

### 3. Construir e Subir os Containers

```bash
docker-compose up --build
```

#### *Obs:* Ao executar o container, através de scripts, irá rodar `collectstatic`, `makemigrations`, `migrate` e `runserver`
---

### 4. Criar Superusuário

```bash
docker-compose run --rm application python manage.py createsuperuser
```

---

### 5. Scripts disponíveis

```bash
docker-compose run --rm application collectstatic.sh
docker-compose run --rm application makemigrations.sh
docker-compose run --rm application migrate.sh
```

---

### 6. Acessar a Aplicação

- 🛍️ **Frontend**: [http://localhost:8000](http://localhost:8000)
- 🔐 **Admin**: [http://localhost:8000/admin](http://localhost:8000/admin)

---



## 👨‍💻 Autor

Desenvolvido por **Thomas Nicholas** — [Linkedin](https://www.linkedin.com/in/thomaas-nicholas/) | [GitHub](https://github.com/ThomasNicholas21)

---

## 🐳 Observações

- Este projeto é focado em fins educacionais e MVP.

---
