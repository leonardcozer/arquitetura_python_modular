"""
Router orquestrador do módulo Cadastro
Agrupa todos os submódulos de cadastro (produto, cliente, etc.)
"""
from fastapi import APIRouter

from app.modules.Cadastro.produto import router as produto_router

# Router principal do módulo Cadastro
router = APIRouter(prefix="/cadastro", tags=["Cadastro"])

# Inclui os routers dos submódulos
router.include_router(produto_router)

