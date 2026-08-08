from uuid import uuid4
from pathlib import Path

def generate_filename(original_filename : str)-> str:
    extension = Path(original_filename).suffix.lower()
    unique_filename= f"{uuid4()}{extension}"
    return unique_filename 