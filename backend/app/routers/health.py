from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
def health():

    return {
        "success": True,
        "message": "API Running",
        "data":{
            "status": "healthy"
        }
    }