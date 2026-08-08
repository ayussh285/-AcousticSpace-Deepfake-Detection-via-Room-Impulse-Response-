import numpy as np
import librosa
import noisereduce as nr

def audio_normalization(audio):
    raw_signal = audio["audio_signal"]
    max_amp = np.max(np.abs(raw_signal))
    if max_amp != 0 :
        normalized_signal = raw_signal / max_amp
    else:
        normalized_signal= raw_signal

    audio["normalized_signal"]= normalized_signal
    return audio

def trim_signal(audio):
    trimmed_audio, _ = librosa.effects.trim(audio["normalized_signal"], top_db=60)

    audio["trimmed_signal"]= trimmed_audio
    audio["trimmed_samples"] = trimmed_audio.size
    audio["trimmed_duration"] = ( trimmed_audio.size /audio["sampling_rate"])
    return audio

def remove_noise(audio):
    denoised_signal = nr.reduce_noise(y= audio["trimmed_signal"], sr= audio["sampling_rate"])
    audio["denoised_signal"]= denoised_signal
    return audio

def extract_mfcc(audio):
    mfcc_matrix = librosa.feature.mfcc(y=audio["denoised_signal"], sr= audio["sampling_rate"], n_mfcc=13)
    audio["mfcc"]= mfcc_matrix
    audio["mfcc_shape"] = mfcc_matrix.shape
    return audio

def extract_mel_spectrogram(audio):
    mel_spectrogram = librosa.feature.melspectrogram(y=audio["denoised_signal"], sr= audio["sampling_rate"], n_mels=128)
    audio["mel_spectrogram"]= mel_spectrogram
    audio["mel_spectrogram_shape"] = mel_spectrogram.shape
    return audio

def extract_chroma(audio):
    chroma = librosa.feature.chroma_stft(y=audio["denoised_signal"], sr= audio["sampling_rate"])
    audio["chroma"]= chroma
    audio["chroma_shape"] = chroma.shape
    return audio

def extract_spectral_centroid(audio):
    spectral_centroid = librosa.feature.spectral_centroid(y=audio["denoised_signal"], sr= audio["sampling_rate"])
    audio["spectral_centroid"]= spectral_centroid
    audio["spectral_centroid_shape"] = spectral_centroid.shape
    return audio

def extract_spectral_bandwidth(audio):
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=audio["denoised_signal"], sr= audio["sampling_rate"])
    audio["spectral_bandwidth"]= spectral_bandwidth
    audio["spectral_bandwidth_shape"] = spectral_bandwidth.shape
    return audio

def extract_spectral_contrast(audio):
    spectral_contrast = librosa.feature.spectral_contrast(y=audio["denoised_signal"], sr= audio["sampling_rate"])
    audio["spectral_contrast"]= spectral_contrast
    audio["spectral_contrast_shape"] = spectral_contrast.shape
    return audio

def extract_zero_crossing_rate(audio):
    zero_crossing_rate = librosa.feature.zero_crossing_rate(y=audio["denoised_signal"])
    audio["zero_crossing_rate"]= zero_crossing_rate
    audio["zero_crossing_rate_shape"] = zero_crossing_rate.shape
    return audio

def extract_rms(audio):
    rms = librosa.feature.rms(y=audio["denoised_signal"])
    audio["rms"]= rms
    audio["rms_shape"] = rms.shape
    return audio

def preprocess_audio(audio):
    audio = audio_normalization(audio)
    audio = trim_signal(audio)
    audio = remove_noise(audio)
    audio = extract_mfcc(audio)
    audio = extract_mel_spectrogram(audio)
    audio = extract_chroma(audio)
    audio = extract_spectral_centroid(audio)
    audio = extract_spectral_bandwidth(audio)
    audio = extract_spectral_contrast(audio)
    audio = extract_zero_crossing_rate(audio)
    audio = extract_rms(audio)
    return audio

 