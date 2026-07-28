from fastapi import APIRouter, UploadFile, File
from app.services.prediction_service import predict_audio

router = APIRouter (
    prefix= "/predict",
    tags= ["Prediction"]
)

@router.post("/")
def predict(file : UploadFile = File(...)):
    result = predict_audio(file)
    return {
        "success": True,
        "message": "Prediction Completed",
        "data": result
    }
        