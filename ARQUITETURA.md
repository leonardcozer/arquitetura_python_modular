# Arquitetura Modular - Documentação

## Estrutura da Aplicação

A aplicação foi reorganizada seguindo uma arquitetura modular baseada em domínios:

```
app/
├── main.py                  # Entry Point (Inicializa o FastAPI)
│
├── core/                    # Infraestrutura Global (Shared Kernel)
│   ├── __init__.py
│   ├── config.py            # Variáveis de Ambiente (Pydantic Settings)
│   ├── database.py          # Conexão SQLAlchemy (SessionLocal)
│   ├── exceptions.py        # Exceções customizadas
│   └── exception_handlers.py # Handlers de erro globais
│
└── modules/                 # DOMÍNIOS DE NEGÓCIO
    ├── __init__.py
    └── Cadastro/            # [MÓDULO COMPLEXO]
        ├── __init__.py
        ├── router.py        # Orquestrador de rotas (/cadastro)
        │
        └── produto/         # -> SUBDOMÍNIO
            ├── __init__.py      # Expõe o router para o módulo Cadastro
            ├── router.py        # Controller (Rotas HTTP)
            ├── service.py       # Regras de Negócio
            ├── repository.py    # Acesso ao Banco (SQLAlchemy)
            ├── schemas.py       # DTOs (Pydantic)
            └── models.py        # Tabelas do Banco (ORM)
```

## Principais Conceitos

### 1. Modularidade
O código é organizado por **Domínio** (ex: Cadastro), não por camada técnica.

### 2. Arquitetura Hexagonal (Simplificada)
Dentro do módulo, respeitamos as camadas:
- **Router** → **Service** → **Repository**

### 3. Hierarquia
Módulos complexos possuem submódulos (ex: `cadastro` → `produto`)

## Fluxo de Requisição

1. **Router** (`router.py`) - Recebe a requisição HTTP
2. **Service** (`service.py`) - Aplica regras de negócio
3. **Repository** (`repository.py`) - Acessa o banco de dados
4. **Models** (`models.py`) - Define as tabelas do banco

## Rotas

As rotas estão organizadas hierarquicamente:

- `/cadastro/produtos` - Lista todos os produtos
- `/cadastro/produtos/{id}` - Obtém um produto específico
- `/cadastro/produtos/categoria/{categoria}` - Lista por categoria
- `/cadastro/produtos/buscar/termo` - Busca produtos

## Migração da Estrutura Antiga

A estrutura antiga ainda existe em:
- `cmd/` - Entry point antigo
- `internal/` - Infraestrutura antiga
- `pkg/` - Utilitários e exceptions antigas
- `config/` - Configurações antigas

**Nota:** A nova estrutura está em `app/` e é totalmente funcional. A estrutura antiga pode ser removida após validação.

## Como Executar

```bash
# Usando o novo entry point
python -m app.main

# Ou
uvicorn app.main:app --reload
```

## Adicionar Novos Módulos

Para adicionar um novo módulo (ex: Financeiro):

1. Criar `app/modules/Financeiro/`
2. Criar `app/modules/Financeiro/router.py` (orquestrador)
3. Criar submódulos conforme necessário
4. Registrar no `app/main.py`:
   ```python
   from app.modules.Financeiro import router as financeiro_router
   app.include_router(financeiro_router)
   ```

## Dependências de Infraestrutura

A infraestrutura (logger, tracing, metrics) ainda está em `internal/infra/` e será migrada gradualmente para `app/core/` conforme necessário.

