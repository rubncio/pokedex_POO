from fastapi import FastAPI
from routers import combate_router, movimiento_router, pokemon_router

app=FastAPI()

app.include_router(combate_router.router, movimiento_router.router, pokemon_router.router)