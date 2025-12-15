"""
Router orquestrador do módulo Cadastro
Agrupa todos os submódulos de cadastro (produto, cliente, etc.)
"""
from fastapi import APIRouter

from app.modules.Cadastro.produto import router as produto_router

# Router principal do módulo Cadastro
# Não possui tags próprias - as tags vêm dos submódulos
router = APIRouter(prefix="/cadastro")

# Inclui os routers dos submódulos
router.include_router(produto_router)

