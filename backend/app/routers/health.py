from fastapi import APIRouter
from backend.app.schemas.response import APIResponse

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)

@router.get("/")
def health():
    return APIResponse (
        success=True,
        message="API Running",
        data={"status": "healthy"}
    )