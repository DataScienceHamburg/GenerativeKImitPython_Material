
#%% (1) Packages
from langchain_community.document_loaders import WebBaseLoader

#%% (2) URL Handling
# Load text directly from a URL (Project Gutenberg example)
url = "https://www.gutenberg.org/cache/epub/2852/pg2852.txt"

#%% (3) Load a single document from the web
web_loader = WebBaseLoader(web_path=url)
doc = web_loader.load()

#%% (4) Understand the document
# Metadata
doc[0].metadata

# %% Page content
doc[0].page_content

# %%
