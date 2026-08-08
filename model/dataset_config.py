from pathlib import Path

DATASET_PATH = Path(r"D:\code\datasets\archive2")

TRAIN_AUDIO_DIR = DATASET_PATH / "ASVspoof2019_LA_train" / "flac"
DEV_AUDIO_DIR = DATASET_PATH / "ASVspoof2019_LA_dev" / "flac"
EVAL_AUDIO_DIR = DATASET_PATH / "ASVspoof2019_LA_eval" / "flac"

PROTOCOL_DIR = DATASET_PATH / "ASVspoof2019_LA_cm_protocols"

TRAIN_PROTOCOL = PROTOCOL_DIR / "ASVspoof2019.LA.cm.train.trn.txt"
DEV_PROTOCOL = PROTOCOL_DIR / "ASVspoof2019.LA.cm.dev.trl.txt"
EVAL_PROTOCOL = PROTOCOL_DIR / "ASVspoof2019.LA.cm.eval.trl.txt"