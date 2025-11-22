#%% packages
from google import genai
from google.genai import types

from IPython.display import HTML, Markdown
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

#%% We can use most of the Gemini models such as 2.5 Flash etc... here 
MODEL_ID = "gemini-2.5-pro"

prompt = """
  Based on the contents of this PDF https://ir.tesla.com/_flysystem/s3/sec/000162828023034847/tsla-20230930-gen.pdf, What 
  are the Total liabilities and Total assets for 2022 and 2023. Lay them out in this format
                   September 30 2023    December 31, 2022
Total Assets         $123               $456
Total Liabilities    $67                $23

Don't output anything else, just the above information
"""

config = {
    "tools": [{"url_context": {}}],
}

response = client.models.generate_content(
    contents=[prompt],
    model=MODEL_ID,
    config=config
)
#%%
Markdown(response.text)
# %%
response.usage_metadata