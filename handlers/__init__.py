from aiogram import Router

from handlers.start import router as start_router
from handlers.notes import router as notes_router

router = Router()
router.include_router(start_router)
router.include_router(notes_router)
