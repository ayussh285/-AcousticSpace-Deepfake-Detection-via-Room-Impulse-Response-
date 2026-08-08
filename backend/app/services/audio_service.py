from fastapi import UploadFile, HTTPException
from backend.app.utils.filename import generate_filename
from backend.app.utils.logger import logger
from pathlib import Path
from backend.app.config.settings import (
    UPLOAD_FOLDER,
    ALLOWED_EXTENSIONS,
)
 
def save_audio(file: UploadFile) -> Path:
    extension = Path(file.filename).suffix.lower()

    if  extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code= 400,
            detail= "Only mp3, wav and flac allowed"
        )
            
    UPLOAD_DIR = UPLOAD_FOLDER
    UPLOAD_DIR.mkdir(parents= True, exist_ok=True)

    filename = generate_filename(file.filename)
    filepath = UPLOAD_DIR / filename
    logger.info(f"Uploading file : {file.filename}")
    with open(filepath, "wb") as f:
        f.write(file.file.read())
    logger.info(f"File saved at {filepath}")
    return filepath  

def delete_audio(filepath : Path)-> None:
    if filepath.exists():
       filepath.unlink()

       logger.info(f"Deleted file successfully : {filepath.name}")
