#%% preparation
# 1. Install Poppler for Windows and set its bin path:
# Example: C:\poppler-24.02.0\Library\bin
# Add to PATH or set POPPLER_PATH env var.
# 2. Install Tesseract OCR and optionally set:
# TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
# python deps: pip install: pdf2image pillow pytesseract


#%% packages
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
import os
from typing import List, Optional

from pdf2image import convert_from_path
import pytesseract


pdf_path = Path(__file__).parent / "PDF_mit_Bild.pdf"


def ocr_pdf_with_tesseract(
    path: Path,
    dpi: int = 200,
    languages: str = "eng+deu",
    poppler_path: Optional[str] = None,
) -> List[str]:
    if os.environ.get("TESSERACT_CMD"):
        pytesseract.pytesseract.tesseract_cmd = os.environ["TESSERACT_CMD"]

    if poppler_path is None:
        poppler_path = os.environ.get("POPPLER_PATH")

    images = convert_from_path(str(path), dpi=dpi, poppler_path=poppler_path)
    texts: List[str] = []
    for img in images:
        if img.mode != "RGB":
            img = img.convert("RGB")
        txt = pytesseract.image_to_string(img, lang=languages)
        texts.append(txt or "")
    return texts


loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

# Fallback to OCR if extracted text seems empty (e.g., scanned/image PDF)
total_chars = sum(len((d.page_content or "").strip()) for d in docs)
if total_chars < 20:
    ocr_texts = ocr_pdf_with_tesseract(pdf_path)
    for i, d in enumerate(docs):
        if i < len(ocr_texts):
            d.page_content = ocr_texts[i]

print(f"Loaded {len(docs)} page(s) from {pdf_path.name}")
if docs:
    first = docs[0]
    meta_preview = {k: first.metadata.get(k) for k in ("page", "source")}
    text_preview = (first.page_content or "").strip().replace("\n", " ")
    print("First page metadata:", meta_preview)
    print("First 300 chars:", text_preview[:300])

# %%
