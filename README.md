# API Produto - Sistema de Gerenciamento de Produtos

API RESTful desenvolvida em Python com FastAPI para gerenciamento de produtos, seguindo uma arquitetura modular baseada em domínios.

## 📋 Índice

- [Características](#-características)
- [Arquitetura](#-arquitetura)
- [Tecnologias](#-tecnologias)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Executando a Aplicação](#-executando-a-aplicação)
- [Endpoints da API](#-endpoints-da-api)
- [Observabilidade](#-observabilidade)
- [Docker](#-docker)
- [Desenvolvimento](#-desenvolvimento)

## ✨ Características

- ✅ Arquitetura modular baseada em domínios
- ✅ Arquitetura Hexagonal (Router → Service → Repository)
- ✅ API RESTful com FastAPI
- ✅ Banco de dados PostgreSQL com SQLAlchemy
- ✅ Validação de dados com Pydantic
- ✅ Observabilidade completa:
  - 📊 Logging com Grafana/Loki
  - 📈 Métricas com Prometheus
  - 🔍 Distributed Tracing com OpenTelemetry/Tempo
- ✅ Health checks (liveness e readiness)
- ✅ CORS configurável
- ✅ Tratamento de erros centralizado
- ✅ Validação e sanitização de inputs
- ✅ Pool de conexões otimizado

## 🏗️ Arquitetura

A aplicação segue uma **arquitetura modular baseada em domínios**, organizando o código por contexto de negócio ao invés de camadas técnicas.

### Princípios

1. **Modularidade**: Código organizado por Domínio (ex: Cadastro), não por camada técnica
2. **Hexagonal (Simplificado)**: Dentro do módulo, respeitamos as camadas: `Router` → `Service` → `Repository`
3. **Hierarquia**: Módulos complexos possuem submódulos (ex: `cadastro` → `produto`)

### Fluxo de Requisição

```
HTTP Request → Router → Service → Repository → Database
                ↓         ↓          ↓
            Validação  Regras de  Acesso
            (Schemas)  Negócio    aos Dados
```

## 🛠️ Tecnologias

### Core
- **Python 3.11**
- **FastAPI 0.104.1** - Framework web assíncrono
- **SQLAlchemy 2.0.23** - ORM
- **Pydantic 2.5.0** - Validação de dados
- **Uvicorn** - Servidor ASGI

### Banco de Dados
- **PostgreSQL** - Banco de dados relacional
- **psycopg2-binary** - Driver PostgreSQL

### Observabilidade
- **Grafana/Loki** - Agregação de logs
- **Prometheus** - Métricas
- **OpenTelemetry/Tempo** - Distributed tracing

### Outras
- **Docker** - Containerização
- **Alembic** - Migrations (estrutura preparada)

## 📁 Estrutura do Projeto

```
app/
├── main.py                  # Entry Point (Inicializa o FastAPI)
│
├── core/                    # Infraestrutura Global (Shared Kernel)
│   ├── config.py            # Variáveis de Ambiente (Pydantic Settings)
│   ├── database.py          # Conexão SQLAlchemy (SessionLocal)
│   ├── exceptions.py        # Exceções customizadas
│   ├── exception_handlers.py # Handlers de erro globais
│   ├── validators.py        # Validadores e sanitizadores de input
│   │
│   ├── http/                # HTTP Server e Middlewares
│   │   ├── server.py        # Criação do servidor FastAPI
│   │   └── middlewares.py  # Middlewares (Logger, CORS)
│   │
│   └── observability/       # Observabilidade
│       ├── logger/          # Logger com Grafana/Loki
│       ├── metrics/         # Métricas Prometheus
│       └── tracing/        # OpenTelemetry/Tempo
│
└── modules/                 # DOMÍNIOS DE NEGÓCIO
    └── Cadastro/           # [MÓDULO COMPLEXO]
        ├── router.py       # Orquestrador de rotas (/cadastro)
        │
        └── produto/         # -> SUBDOMÍNIO
            ├── router.py   # Controller (Rotas HTTP)
            ├── service.py  # Regras de Negócio
            ├── repository.py # Acesso ao Banco (SQLAlchemy)
            ├── schemas.py  # DTOs (Pydantic)
            └── models.py    # Tabelas do Banco (ORM)
```

## 📦 Pré-requisitos

- Python 3.11+
- PostgreSQL 12+
- Docker e Docker Compose (opcional)

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone <repository-url>
cd ModeloArquiteturaPython_02
```

### 2. Crie um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Servidor
SERVER_HOST=0.0.0.0
SERVER_PORT=8001
ENVIRONMENT=development
DEBUG=True
LOG_LEVEL=INFO

# Banco de Dados
DATABASE_USER=postgres
DATABASE_PASSWORD=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=produto_db
DATABASE_POOL_SIZE=20
DATABASE_MAX_OVERFLOW=40

# CORS
CORS_ORIGINS=http://localhost:3000,http://localhost:8080
CORS_CREDENTIALS=True

# Grafana/Loki (Opcional)
LOKI_ENABLED=True
LOKI_URL=http://172.30.0.45:3100
LOKI_JOB=MONITORAMENTO_PRODUTO

# Tempo/OpenTelemetry (Opcional)
TEMPO_ENABLED=True
TEMPO_ENDPOINT=http://172.30.0.45:4317
```

## ▶️ Executando a Aplicação

### Modo Desenvolvimento (Local)

```bash
# Ative o ambiente virtual
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

# Execute a aplicação
python -m app.main

# Ou com uvicorn diretamente
uvicorn app.main:app --reload --host 0.0.0.0 --port 8001
```

A aplicação estará disponível em: `http://localhost:8001`

### Documentação Interativa

- **Swagger UI**: http://localhost:8001/docs
- **ReDoc**: http://localhost:8001/redoc
- **OpenAPI JSON**: http://localhost:8001/openapi.json

## 📡 Endpoints da API

### Base URL
```
http://localhost:8001/cadastro/produtos
```

### Endpoints Disponíveis

#### Produtos

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/cadastro/produtos` | Lista todos os produtos (com paginação) |
| `GET` | `/cadastro/produtos/{id}` | Obtém um produto específico |
| `POST` | `/cadastro/produtos` | Cria um novo produto |
| `PUT` | `/cadastro/produtos/{id}` | Atualiza um produto |
| `DELETE` | `/cadastro/produtos/{id}` | Deleta um produto |
| `GET` | `/cadastro/produtos/categoria/{categoria}` | Lista produtos por categoria |
| `GET` | `/cadastro/produtos/buscar/termo?termo={termo}` | Busca produtos por termo |

#### Health Checks

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/health` | Liveness probe |
| `GET` | `/ready` | Readiness probe |
| `GET` | `/metrics` | Métricas Prometheus |

### Exemplos de Requisição

#### Criar Produto

```bash
curl -X POST "http://localhost:8001/cadastro/produtos" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Notebook Dell",
    "descricao": "Notebook de alta performance",
    "preco": 4999.99,
    "quantidade": 10,
    "categoria": "Eletrônicos"
  }'
```

#### Listar Produtos

```bash
curl "http://localhost:8001/cadastro/produtos?page=1&page_size=10"
```

#### Buscar Produtos

```bash
curl "http://localhost:8001/cadastro/produtos/buscar/termo?termo=notebook&page=1&page_size=10"
```

## 📊 Observabilidade

A aplicação possui observabilidade completa integrada:

### Logging (Grafana/Loki)

- Logs estruturados enviados para Grafana/Loki
- Suporte a batch logging
- Graceful shutdown
- Configurável via variáveis de ambiente

### Métricas (Prometheus)

- Métricas HTTP (requisições, duração, erros)
- Métricas de banco de dados
- Service Map (dependências entre serviços)
- Health checks
- Endpoint: `/metrics`

### Tracing (OpenTelemetry/Tempo)

- Distributed tracing automático
- Instrumentação de FastAPI e SQLAlchemy
- Visualização de traces no Tempo
- Configurável via variáveis de ambiente

## 🐳 Docker

### Build da Imagem

```bash
docker build -t produto-api .
```

### Executar com Docker Compose

```bash
docker-compose up -d
```

### Variáveis de Ambiente no Docker

O `docker-compose.yml` utiliza o arquivo `.env` para configuração.

## 💻 Desenvolvimento

### Adicionar Novo Módulo

Para adicionar um novo módulo (ex: Financeiro):

1. Criar estrutura:
```bash
app/modules/Financeiro/
├── __init__.py
├── router.py
└── [submodulos]/
```

2. Registrar no `app/main.py`:
```python
from app.modules.Financeiro import router as financeiro_router
app.include_router(financeiro_router)
```

### Padrão de Código

- **Router**: Recebe requisições HTTP, valida inputs
- **Service**: Contém regras de negócio
- **Repository**: Acessa o banco de dados
- **Schemas**: DTOs para validação (Pydantic)
- **Models**: Modelos ORM (SQLAlchemy)

### Validações

- Inputs são validados e sanitizados automaticamente
- Proteção contra SQL injection
- Validação de tipos com Pydantic
- Tratamento de erros centralizado

## 🔒 Segurança

- ✅ Validação e sanitização de inputs
- ✅ Proteção contra SQL injection
- ✅ CORS configurável
- ✅ Tratamento de erros sem expor detalhes em produção
- ✅ Validação de senha de banco em produção

## 📝 Licença

Este projeto é um modelo de arquitetura para referência.

## 🤝 Contribuindo

1. Siga a arquitetura modular proposta
2. Mantenha a separação de responsabilidades (Router → Service → Repository)
3. Adicione validações apropriadas
4. Documente novos endpoints

## 📞 Suporte

Para dúvidas ou problemas, consulte a documentação da API em `/docs` ou abra uma issue.

---

**Desenvolvido com ❤️ usando FastAPI e arquitetura modular**

