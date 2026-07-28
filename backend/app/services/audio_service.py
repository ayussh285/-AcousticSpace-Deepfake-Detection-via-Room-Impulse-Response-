import os
from fastapi import UploadFile, HTTPException
from app.utils.filename import generate_filename
from app.utils.logger import logger
from pathlib import Path
from app.config.settings import (
    UPLOAD_FOLDER,
    ALLOWED_EXTENSIONS,
)
 
def save_audio(file: UploadFile):
     
    extension = Path(file.filename).suffix.lower()

    if  extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code= 400,
            detail= "Only mp3, wav and flac allowed"
        )
            
    
    UPLOAD_DIR = UPLOAD_FOLDER

    UPLOAD_DIR.mkdir(exist_ok=True)

    filename = generate_filename(file.filename)
    filepath = UPLOAD_DIR / filename
    logger.info(f"Uploadling file : {file.filename}")
    with open(filepath, "wb") as f:
        f.write(file.file.read())
    logger.info(f"File saved at {filepath}")
    return filename     

def delete_audio(filepath : str):
    filepath = Path(filepath)
    if filepath.exist():
       filepath.unlink()

       logger.info(f"Deleted file successfully : {filepath.name}")
