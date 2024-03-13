import controller
from fastapi import APIRouter


router = APIRouter()
router.include_router(controller.router, tags=["toxicity"])
