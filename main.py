from fastapi import FastAPI 
from backend.app.exceptions.handlers import register_exception_handlers
from backend.app.routers.upload import router as upload_router
from backend.app.routers.health import router as health_router
from backend.app.routers.predict import router as predict_router

app = FastAPI( 
    title="Deepfake Audio Detection API",
    version="1.0.0"
)

register_exception_handlers(app)
app.include_router(upload_router)
app.include_router(health_router)
app.include_router(predict_router)
