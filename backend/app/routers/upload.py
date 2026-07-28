from fastapi import APIRouter, UploadFile, File
from app.services.audio_service import save_audio

router = APIRouter(
    prefix="/upload",
    tags = ["upload"]
)

@router.post("/")
def audio_process(file: UploadFile = File(...)):
    filename = save_audio(file)
    return {
        "success": True,
        "message": "Uploaded Successfully",
        "data": {
            "path": filename  
        }  
    }