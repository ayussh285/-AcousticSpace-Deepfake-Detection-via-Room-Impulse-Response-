from fastapi import APIRouter, UploadFile, File
from backend.app.services.audio_service import save_audio
from backend.app.schemas.response import APIResponse

router = APIRouter(
    prefix="/upload",
    tags = ["upload"]
)

@router.post("/")
def audio_process(file: UploadFile = File(...)):
    filename = save_audio(file)
    
    return APIResponse(
        success=True,
        message="Uploaded Successfully",
        data={"path": str(filename)}
    )