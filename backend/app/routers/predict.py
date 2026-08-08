from fastapi import APIRouter, UploadFile, File
from backend.app.services.prediction_service import predict_audio
from backend.app.schemas.response import APIResponse

router = APIRouter (
    prefix= "/predict",
    tags= ["Prediction"]
)

@router.post("/", response_model= APIResponse)
def predict(file : UploadFile = File(...)):
    result = predict_audio(file)
    return APIResponse(
        success=True,
        message="Prediction Completed",
        data=result
)
        