import io
from pathlib import Path
from PyPDF2 import PdfReader

def load_file(file) -> str:
    """
    Load a PDF or text file and return its text content.
    file: uploaded file from Streamlit file_uploader
    """
    if file is None:
        return ""
    
    # Handle PDF
    if file.type == "application/pdf":
        try:
            pdf = PdfReader(file)
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            return text.strip()
        except Exception as e:
            raise ValueError(f"Error reading PDF: {e}")
    
    # Handle plain text
    elif file.type in ["text/plain", "application/octet-stream"]:
        try:
            return file.read().decode("utf-8").strip()
        except Exception as e:
            raise ValueError(f"Error reading text file: {e}")
    
    else:
        raise ValueError("Unsupported file type. Only PDF or TXT allowed.")
