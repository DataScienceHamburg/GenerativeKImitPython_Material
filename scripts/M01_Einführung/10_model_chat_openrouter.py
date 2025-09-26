#%% packages
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv(usecwd=True))
# %%
# %% OpenAI models
MODEL_NAME = 'gpt-4o-mini'
model = ChatOpenAI(model_name=MODEL_NAME,
                   temperature=0.5,
                   api_key=os.getenv('OPENROUTER_API_KEY'),
                   base_url="https://openrouter.ai/api/v1")

# %%
res = model.invoke("What is a LangChain?")
# %% find out what is in the result
res.model_dump()
# %% only print content
print(res.content)
# %%
