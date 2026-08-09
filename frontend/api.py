import requests
from config import PREDICT_ENDPOINT


def predict_audio(uploaded_file):
    """
    Sends the uploaded audio file to the FastAPI backend.
    Returns:
        (success, response)
    """

    try:
        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                uploaded_file.type
            )
        }

        response = requests.post(
            PREDICT_ENDPOINT,
            files=files,
            timeout=120
        )

        if response.status_code == 200:
            return True, response.json()

        try:
            error = response.json()
            return False, error.get("message", "Prediction failed.")
        except Exception:
            return False, f"HTTP {response.status_code}"

    except requests.exceptions.ConnectionError:
        return False, "Cannot connect to backend.\n\nStart FastAPI server first."

    except requests.exceptions.Timeout:
        return False, "Prediction timed out."

    except Exception as e:
        return False, str(e)