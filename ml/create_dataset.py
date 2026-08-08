from pathlib import Path
import numpy as np

from audio.load_audio import load_audio
from audio.validate_audio import validate_audio
from audio.preprocess_audio import preprocess_audio
from audio.feature_vector import create_feature_vector

from model.dataset_config import (
    TRAIN_AUDIO_DIR,
    TRAIN_PROTOCOL
)

LABELS = {
    "bonafide": 1,
    "spoof": 0
}

def create_dataset():

    X = []
    y = []

    with open(TRAIN_PROTOCOL, "r") as protocol:
        lines = protocol.readlines()

    print(f"Processing {len(lines)} training samples...")

    for idx, line in enumerate(lines):

        try:
            parts = line.strip().split()

            file_id = parts[1]
            label = parts[-1]

            audio_path = TRAIN_AUDIO_DIR / f"{file_id}.flac"

            if not audio_path.exists():
                continue

            audio = load_audio(audio_path)
            audio = validate_audio(audio)

            if audio is None:
                continue

            audio = preprocess_audio(audio)
            feature_vector = create_feature_vector(audio)

            X.append(feature_vector)
            y.append(LABELS[label])

            if (idx + 1) % 100 == 0:
                print(f"{idx + 1}/{len(lines)} files completed")

        except Exception as e:
            print(f"Skipped {idx}: {e}")

    return np.array(X), np.array(y)