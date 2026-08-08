from pathlib import Path
import numpy as np
from audio.load_audio import load_audio
from audio.validate_audio import validate_audio
from audio.preprocess_audio import preprocess_audio
from audio.feature_vector import create_feature_vector

def create_dataset(dataset_path):
    X = []
    y = []
    
    classes = {
        "real": 1,
        "fake": 0
    }

    dataset_path = Path(dataset_path)

    for folder_name, label in classes.items():
        folder_path = dataset_path / folder_name

        if not folder_path.exists():
            continue

        for extension in ("*.wav", "*.mp3", "*.flac"):
            for file in folder_path.glob(extension):
                audio = load_audio(file)
                audio = validate_audio(audio)

                if audio is None:
                    continue

                audio = preprocess_audio(audio)
                feature_vector = create_feature_vector(audio)

                X.append(feature_vector)
                y.append(label)

    return np.array(X), np.array(y)
    