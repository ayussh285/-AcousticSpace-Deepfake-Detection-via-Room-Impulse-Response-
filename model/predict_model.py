import joblib
from pathlib import Path
from audio.load_audio import load_audio
from audio.validate_audio import validate_audio
from audio.preprocess_audio import preprocess_audio
from audio.feature_vector import create_feature_vector
from fastapi import HTTPException

LABELS = {
    1: "Real",
    0: "Fake"
}

MODEL_PATH = Path("trained_models") / "random_forest_v1.joblib"
MODEL = joblib.load(MODEL_PATH)

def predict(audio_path):
    audio = load_audio(audio_path)
    audio = validate_audio(audio)
    if audio is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid audio file."
    )
    audio = preprocess_audio(audio)
    feature_vector = create_feature_vector(audio)
    print(feature_vector.shape)

    feature_vector = feature_vector.reshape(1, -1)
    prediction = MODEL.predict(feature_vector)
    probabilities = MODEL.predict_proba(feature_vector)
    print(MODEL.classes_)
    confidence = probabilities[0][prediction[0]]
    print("Prediction:", prediction)
    print("Probabilities:", probabilities)

    confidence_percent = round(confidence * 100, 2)

    if confidence_percent >= 90:
        confidence_level = "Very High"
    elif confidence_percent >= 75:
        confidence_level = "High"
    elif confidence_percent >= 60:
        confidence_level = "Medium"
    else:
        confidence_level = "Low"

    return {
    "prediction": LABELS[prediction[0]],
    "confidence": float(confidence),
    "confidence_level": confidence_level,
    "duration": audio["duration"],
    "sampling_rate": audio["sampling_rate"],
    "model": "Random Forest V1"
}

if __name__ == "__main__":
    result = predict(
        "dataset/real/Audio1.wav"   # use one of your actual files
    )

    print(result)