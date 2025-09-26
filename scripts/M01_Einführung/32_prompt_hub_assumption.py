#%%
# Create a LANGSMITH_API_KEY in Settings > API Keys
from langchain import hub
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv('.env')
from pprint import pprint
from rich.markdown import Markdown
from rich.console import Console
console = Console()

#%%
prompt = hub.pull("smithing-gold/assumption-checker", include_model=True)
# %%
model = ChatGroq(model_name="openai/gpt-oss-120b")

#%%
chain = prompt | model | StrOutputParser()

#%% 
user_query = "Wie kann ich die ungenutzten 90% meines Gehirns freischalten, um intelligenter zu werden?"
res = chain.invoke({"question": user_query})
# %%
console.print(Markdown(res), width=50)
# %%
