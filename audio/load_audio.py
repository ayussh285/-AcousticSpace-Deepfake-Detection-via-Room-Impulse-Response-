import librosa
from pathlib import Path

def load_audio(filepath : str | Path):
    audio_data , sampling_rate = librosa.load(filepath, sr = 16000)
    duration = librosa.get_duration(y=audio_data, sr= sampling_rate)

    return  {
        "filepath": Path(filepath),
        "audio_signal": audio_data,
        "duration": duration,
        "sampling_rate": sampling_rate,
        "total_samples": audio_data.size,
    }
