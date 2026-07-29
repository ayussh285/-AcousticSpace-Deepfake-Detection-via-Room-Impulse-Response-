from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_FOLDER = BASE_DIR / "uploads"

ALLOWED_EXTENSIONS = {
    ".wav",
    ".mp3",
    ".flac"
}

MAX_FILE_SIZE = 20 * 1024 * 1024