# Migração de Observabilidade

## Resumo

Os arquivos de observabilidade foram movidos de `internal/infra/` para `app/core/observability/` seguindo a nova arquitetura modular.

## Estrutura Nova

```
app/core/observability/
├── __init__.py
├── logger/
│   ├── __init__.py
│   └── zap.py              # Logger com suporte ao Grafana/Loki
├── metrics/
│   ├── __init__.py
│   ├── prometheus.py       # Métricas do Prometheus
│   └── service_map.py      # Service Map (Node Graph)
└── tracing/
    ├── __init__.py
    └── opentelemetry_setup.py  # OpenTelemetry/Tempo
```

## Arquivos Movidos

### Logger
- `internal/infra/logger/zap.py` → `app/core/observability/logger/zap.py`
- Funcionalidades: Grafana/Loki integration, batch logging, graceful shutdown

### Metrics
- `internal/infra/metrics/prometheus.py` → `app/core/observability/metrics/prometheus.py`
- `internal/infra/metrics/service_map.py` → `app/core/observability/metrics/service_map.py`
- Funcionalidades: HTTP metrics, database metrics, service map, health checks

### Tracing
- `internal/infra/tracing/opentelemetry_setup.py` → `app/core/observability/tracing/opentelemetry_setup.py`
- Funcionalidades: OpenTelemetry/Tempo integration, FastAPI/SQLAlchemy instrumentation

## Imports Atualizados

### Antes
```python
from internal.infra.logger.zap import configure_logging
from internal.infra.metrics.prometheus import setup_metrics
from internal.infra.tracing.opentelemetry_setup import setup_tracing
```

### Depois
```python
from app.core.observability.logger import configure_logging
from app.core.observability.metrics import setup_metrics
from app.core.observability.tracing import setup_tracing
```

## Arquivos Atualizados

1. **app/main.py** - Imports atualizados para nova estrutura
2. **app/core/database.py** - Import de service_map atualizado
3. **app/modules/Cadastro/produto/service.py** - Import de tracing atualizado
4. **internal/infra/http/middlewares.py** - Imports de metrics atualizados
5. **app/core/observability/logger/zap.py** - Imports internos atualizados

## Diretórios Removidos

- `internal/infra/logger/` ✅ Removido
- `internal/infra/metrics/` ✅ Removido
- `internal/infra/tracing/` ✅ Removido

## Estrutura Restante em internal/infra/

Ainda permanecem em `internal/infra/`:
- `http/` - Server e middlewares (ainda em uso)
- `database/banco_dados.py` - Não está sendo usado, pode ser removido no futuro

## Benefícios

1. **Organização**: Observabilidade centralizada em `app/core/observability/`
2. **Consistência**: Segue o padrão da nova arquitetura modular
3. **Manutenibilidade**: Mais fácil de encontrar e manter
4. **Escalabilidade**: Fácil adicionar novos tipos de observabilidade

## Próximos Passos (Opcional)

1. Migrar `internal/infra/http/` para `app/core/http/`
2. Remover `internal/infra/database/banco_dados.py` se não for mais necessário
3. Considerar migrar toda infraestrutura para `app/core/`

