from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from be.api.endpoints.role import router as role_router
from be.api.endpoints.user import router as user_router

app = FastAPI(
    title="Autogenerated playground",
    description="To test endpoints follow its examples and docs",
    version="0.1.0",
    dependencies=[],
)

# Cors Settings
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for router in [user_router, role_router]:
    app.include_router(router)
