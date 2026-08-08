from backend.app.services.audio_service import save_audio
from backend.app.services.audio_service import delete_audio
from model.predict_model import predict
import time

def predict_audio(file):
     filepath = save_audio(file)

     try:
          start = time.perf_counter()
          result = predict(filepath)
          end = time.perf_counter()
          result["processing_time_ms"] = round((end - start) * 1000, 2)
          result["filename"] = file.filename
          return result
     
     finally:
          delete_audio(filepath)
     