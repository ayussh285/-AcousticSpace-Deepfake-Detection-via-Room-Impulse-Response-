from app.services.audio_service import save_audio
from app.services.audio_service import delete_audio
from app.ml.extract_feature import extract_features
from app.ml.model_predict import model_predict

def predict_audio(file):
     filepath = save_audio(file)

     try:
          features = extract_features(filepath)
          result = model_predict(features)
          return result
     finally:
          delete_audio(filepath)
     

