# Limpeza de Arquivos e Diretórios Obsoletos

## Diretórios Removidos

Os seguintes diretórios foram removidos após a migração para a nova arquitetura:

### ✅ Removidos

1. **`cmd/`** - Entry point antigo
   - Substituído por: `app/main.py`
   - Dockerfile e docker-compose.yml atualizados

2. **`config/`** - Configurações antigas
   - Substituído por: `app/core/config.py`

3. **`pkg/`** - Pacote de utilitários e exceptions
   - `pkg/apperrors/` → Substituído por: `app/core/exceptions.py` e `app/core/exception_handlers.py`
   - `pkg/utils/input_validators.py` → Substituído por: `app/core/validators.py`

4. **`internal/modules/`** - Módulos antigos
   - `internal/modules/produto/` → Substituído por: `app/modules/Cadastro/produto/`

## Diretórios Mantidos

### ⚠️ Ainda em Uso

**`internal/infra/`** - Infraestrutura ainda está sendo usada:
- `internal/infra/http/` - Server e middlewares (usado em `app/main.py`)
- `internal/infra/logger/` - Logger com Loki (usado em `app/main.py`)
- `internal/infra/metrics/` - Métricas Prometheus (usado em `app/main.py`)
- `internal/infra/tracing/` - OpenTelemetry/Tempo (usado em `app/main.py`)
- `internal/infra/database/banco_dados.py` - Não está sendo usado, mas mantido por segurança

**Nota:** A infraestrutura em `internal/infra/` pode ser migrada gradualmente para `app/core/` no futuro, mas por enquanto está funcionando corretamente.

## Arquivos Atualizados

1. **Dockerfile** - Atualizado para usar `app.main` em vez de `cmd.api.main`
2. **docker-compose.yml** - Atualizado para usar `app.main` em vez de `cmd.api.main`
3. **internal/infra/http/server.py** - Import atualizado para `app.core.config`
4. **internal/infra/database/banco_dados.py** - Import atualizado para `app.core.config`

## Estrutura Final

```
app/                          # Nova estrutura modular
├── main.py
├── core/                     # Infraestrutura global
│   ├── config.py
│   ├── database.py
│   ├── exceptions.py
│   ├── exception_handlers.py
│   └── validators.py
└── modules/                  # Domínios de negócio
    └── Cadastro/
        └── produto/

internal/infra/              # Infraestrutura (ainda em uso)
├── http/
├── logger/
├── metrics/
└── tracing/
```

## Próximos Passos (Opcional)

1. Migrar `internal/infra/` para `app/core/` gradualmente
2. Remover `internal/infra/database/banco_dados.py` se confirmado que não é usado
3. Limpar `__pycache__/` se necessário

