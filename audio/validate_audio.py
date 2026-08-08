import numpy as np

ALLOWED_SUFFIX = {".mp3", ".wav", ".flac"}

def validate_audio(audio):
    if not audio["filepath"].is_file():
        return None
    
    if audio["filepath"].suffix.lower() not in ALLOWED_SUFFIX:
        return None

    if audio["duration"] < 1 or audio["duration"] > 300:
        return None
    
    if not np.any(audio["audio_signal"]):
        return None
    
    return audio
