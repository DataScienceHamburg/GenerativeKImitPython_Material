#%% pakete
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#%% output structure
class MyMovieOutput(BaseModel):
    title: str
    main_characters: str
    director: str
    release_year: str

class MyMoviesOutput(BaseModel):
    movies: list[MyMovieOutput]

#%% output parser
parser = PydanticOutputParser(pydantic_object=MyMoviesOutput)
# %% prompt template
messages = [
    ("system", "Du bist ein Filmexperte. Gib mir nur Arthouse Filme, die kommerziell floppten. Verwende strikt das vorgegebene Schema. {format_instructions}"),
    ("user", "Handlung: {plot}")
]

prompt_template = ChatPromptTemplate.from_messages(messages).partial(format_instructions=parser.get_format_instructions())


#%% model
MODEL_NAME="openai/gpt-oss-120b"
model = ChatGroq(model=MODEL_NAME, temperature=0)

#%% chain
chain = prompt_template | model | parser
#%% invoke chain
chain_inputs = {"plot": "mars, botanik"}
res = chain.invoke(chain_inputs)
res
# %%
for movie in res.movies:
    print(movie.title)
    print(movie.main_characters)
    print(movie.director)
    print(movie.release_year)
    print("-"*100)
