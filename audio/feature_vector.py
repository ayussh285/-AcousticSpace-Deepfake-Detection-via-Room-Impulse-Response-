import numpy as np

feature_names = [
    "mfcc",
    "mel_spectrogram",
    "chroma",
    "spectral_centroid",
    "spectral_bandwidth",
    "spectral_contrast",
    "zero_crossing_rate",
    "rms"
]

def create_feature_vector(audio):
    features  = []

    for name in feature_names:
        feature = audio[name]
        features.extend(np.mean(feature, axis =1))
        features.extend(np.std(feature, axis =1))

    return np.array(features)