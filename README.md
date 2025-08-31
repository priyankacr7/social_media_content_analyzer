***

# Social Media Content Analyzer

This application allows users to upload PDF or image files containing social media posts and extracts the text using PDF parsing and Optical Character Recognition (OCR). It provides basic sentiment analysis to suggest ways to improve engagement.

## Features

- Upload PDFs and common image files via drag-and-drop or file picker.
- Extract text from PDFs preserving formatting using pdfplumber.
- Extract text from images using Tesseract OCR.
- Provide sentiment-based engagement suggestions.
- Display loading indicators for better user experience.
- Handle errors clearly with user-friendly messages.

## Technologies Used

- Python 3.9+
- FastAPI for backend API.
- Uvicorn ASGI server.
- pdfplumber for PDF text extraction.
- pytesseract for OCR on images.
- TextBlob for sentiment analysis.
- Jinja2 templates for HTML rendering.
- Bootstrap 5 for styling and responsive UI.

## Setup Instructions

1. Clone the repository and navigate into it:

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Create and activate a virtual environment:

- Windows PowerShell:

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

- Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Upgrade pip and install dependencies:

```bash
pip install --upgrade pip
pip install fastapi uvicorn pdfplumber pillow pytesseract textblob jinja2
python -m textblob.download_corpora
```

4. Download and install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).  
Make sure to update the Tesseract executable path in `main.py` if different from default:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

5. Run the FastAPI application:

```bash
uvicorn main:app --reload
```

6. Access the web app at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Usage

- Drag and drop or select a PDF/image file containing social media content.
- Wait for the text extraction and sentiment analysis to complete (loading spinner displays).
- View extracted text and receive a simple engagement suggestion based on sentiment.

## Project Structure

```
.
├── main.py               # FastAPI backend app with endpoints
├── templates/            # HTML template files (index.html, result.html)
├── uploads/              # Folder to save uploaded files
└── README.md             # This documentation
```

## Future Improvements

- Integrate advanced NLP or AI models for deeper content analysis.
- Support batch file uploads and processing.
- Enhance UI with previews and richer interactivity.
- Deploy to a cloud platform for public access.

## Author

Priyanka Srivastava  
[GitHub Profile](https://github.com/priyankacr7)

## License

This project is licensed under the MIT License.

***

If you want a ready `requirements.txt`, create a file with:

```
fastapi
uvicorn
pdfplumber
pillow
pytesseract
textblob
jinja2
```

and install dependencies with:

```bash
pip install -r requirements.txt
```

