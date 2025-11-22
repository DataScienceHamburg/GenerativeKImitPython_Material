
#%% packages
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_pymupdf4llm import PyMuPDF4LLMLoader
import os

#%% define loader
directory_path = "./sample_docs" 
os.listdir(directory_path)


#%% Provide a selector that returns a concrete loader instance based on file extension
def select_loader(file_path):
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()
    if ext == ".txt":
        return TextLoader(file_path)
    if ext == ".pdf":
        return PyMuPDF4LLMLoader(file_path, mode="single")
    raise ValueError(f"Unsupported file type: {ext} for {file_path}")

loader = DirectoryLoader(
    path=directory_path,
    glob="**/*",
    loader_cls=select_loader,
    
    use_multithreading=True, 
    
    show_progress=True 
)

#%% Load documents
documents = loader.load()

print(f"Loaded {len(documents)} documents.")

# %%
documents
# %%
