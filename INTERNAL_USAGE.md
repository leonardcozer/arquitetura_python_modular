# Uso do Diretório `internal/`

## Resumo

Análise do que ainda está sendo utilizado do diretório `internal/` após a migração para a nova arquitetura.

## Estrutura Atual de `internal/`

```
internal/
└── infra/
    ├── database/
    │   └── banco_dados.py      # ❌ NÃO USADO
    └── http/
        ├── server.py            # ✅ USADO
        └── middlewares.py      # ✅ USADO
```

## Arquivos em Uso

### ✅ `internal/infra/http/server.py`

**Status:** EM USO

**Onde é usado:**
- `app/main.py` (linha 19): `from internal.infra.http.server import create_server`

**Função:**
- Cria a instância do FastAPI com configurações básicas
- Define título, descrição, versão e debug mode

**Pode ser migrado para:** `app/core/http/server.py`

---

### ✅ `internal/infra/http/middlewares.py`

**Status:** EM USO

**Onde é usado:**
- `app/main.py` (linha 20): `from internal.infra.http.middlewares import configure_middlewares, configure_cors`

**Funções:**
- `LoggerMiddleware`: Middleware para logging de requisições HTTP
- `configure_cors`: Configura CORS na aplicação
- `configure_middlewares`: Configura todos os middlewares

**Dependências:**
- Usa `app.core.observability.metrics` (já atualizado)

**Pode ser migrado para:** `app/core/http/middlewares.py`

---

## Arquivos NÃO Usados

### ❌ `internal/infra/database/banco_dados.py`

**Status:** NÃO ESTÁ SENDO USADO

**Motivo:**
- Substituído por `app/core/database.py`
- Não há nenhum import deste arquivo no código
- O arquivo ainda tem imports antigos quebrados:
  - `from internal.infra.metrics.service_map import record_service_call` (linha 14)
  - `from internal.modules.produto.entity import Base as ProdutoBase` (linha 177) - módulo não existe mais

**Ação recomendada:** REMOVER

---

## Resumo de Uso

| Arquivo | Status | Usado em | Ação Recomendada |
|---------|--------|----------|------------------|
| `internal/infra/http/server.py` | ✅ USADO | `app/main.py` | Migrar para `app/core/http/` |
| `internal/infra/http/middlewares.py` | ✅ USADO | `app/main.py` | Migrar para `app/core/http/` |
| `internal/infra/database/banco_dados.py` | ❌ NÃO USADO | - | **REMOVER** |

## Próximos Passos Recomendados

### 1. Migrar HTTP para `app/core/http/`

```bash
# Criar estrutura
app/core/http/
├── __init__.py
├── server.py
└── middlewares.py
```

**Benefícios:**
- Centraliza toda infraestrutura em `app/core/`
- Remove dependência de `internal/`
- Mantém consistência com a nova arquitetura

### 2. Remover `internal/infra/database/banco_dados.py`

**Justificativa:**
- Não está sendo usado
- Tem imports quebrados
- Já foi substituído por `app/core/database.py`

### 3. Remover diretório `internal/` completamente

Após migrar `http/`, o diretório `internal/` pode ser removido completamente.

## Estrutura Proposta Após Migração

```
app/core/
├── config.py
├── database.py
├── exceptions.py
├── exception_handlers.py
├── validators.py
├── http/              # ← NOVO (migrado de internal/infra/http/)
│   ├── server.py
│   └── middlewares.py
└── observability/
    ├── logger/
    ├── metrics/
    └── tracing/
```

## Comandos para Verificação

```bash
# Verificar imports de internal
grep -r "from internal\." app/
grep -r "import.*internal\." app/

# Verificar se banco_dados está sendo usado
grep -r "banco_dados" app/
```

