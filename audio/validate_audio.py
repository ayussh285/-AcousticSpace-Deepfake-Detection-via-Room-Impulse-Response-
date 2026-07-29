from load_audio import load_audio
import numpy as np


audio = load_audio(r"D:\code\Projects\AcousticAI- Deepfake Audio Recognition System\10. Complete Syllabus Of Computer Graphics @GateSmashers .mp3")

ALLOWED_SUFFIX = [".mp3", ".wav", ".flac"]

def validate_audio(audio):
    if not audio["filepath"].is_file():
        return f"File doesnot exist"
    
    if audio["filepath"].suffix not in ALLOWED_SUFFIX:
        return "file type not supported"

    if audio["duration"] < 1 or audio["duration"] > 300:
        return "File should be more than of 1 second and less than 5 minutes"
    
    if not np.any(audio["audio_signal"]):
        return "File can't be empty"
    
    return {
    "valid": True,
    "message": "Audio validation successful"
    }

print(validate_audio(audio))