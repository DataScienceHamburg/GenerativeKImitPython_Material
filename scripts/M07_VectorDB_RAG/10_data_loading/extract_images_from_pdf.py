#%%
from langchain_pymupdf4llm import PyMuPDF4LLMLoader

#%%
file_path = "sample_docs/EP3862733B1.pdf"
loader = PyMuPDF4LLMLoader(file_path=file_path, mode="single")
images = loader.extract_images()
print(f"Extracted {len(images)} images from {file_path}")
# %%
