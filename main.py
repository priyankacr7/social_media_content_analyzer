import os
import shutil
import uuid
from fastapi import FastAPI, Request, File, UploadFile, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from PIL import Image
import pdfplumber
import pytesseract
from textblob import TextBlob

# Upload folder
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Configure Tesseract (update if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

app = FastAPI()
templates = Jinja2Templates(directory="templates")

ALLOWED_EXT = {".pdf", ".png", ".jpg", ".jpeg", ".tiff", ".bmp"}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload(request: Request, file: UploadFile = File(...)):
    filename = file.filename or "uploaded_file"
    ext = os.path.splitext(filename)[1].lower()

    if ext not in ALLOWED_EXT:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": f"Unsupported file type: {ext}. Allowed: {', '.join(ALLOWED_EXT)}"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )

    file_id = str(uuid.uuid4())
    saved_path = os.path.join(UPLOAD_DIR, f"{file_id}{ext}")

    try:
        with open(saved_path, "wb") as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "error": f"Could not save file: {str(e)}"},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    try:
        text = ""
        if ext == ".pdf":
            with pdfplumber.open(saved_path) as pdf:
                for page in pdf.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n"
        else:
            img = Image.open(saved_path)
            text = pytesseract.image_to_string(img)
    except Exception as e:
        text = f"[Error extracting text: {str(e)}]"

    if not text.strip():
        text = "[No text found. Try uploading an image or searchable PDF.]"

    # Simple sentiment analysis
    sentiment = TextBlob(text).sentiment
    suggestion = "Neutral post."
    if sentiment.polarity > 0.1:
        suggestion = "Positive sentiment detected. Engage with followers with questions or calls to action."
    elif sentiment.polarity < -0.1:
        suggestion = "Negative sentiment detected. Consider softening language for better engagement."

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "text": text,
            "filename": filename,
            "suggestion": suggestion,
            "polarity": round(sentiment.polarity, 3),
            "subjectivity": round(sentiment.subjectivity, 3),
        },
    )
