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

#%% prompt template
messages = [
    ("system", "Du bist ein Filmexperte. Verwende strikt das vorgegebene Schema. {format_instructions}"),
    ("user", "Handlung: {plot}")
]

prompt_template = ChatPromptTemplate.from_messages(messages).partial(format_instructions=parser.get_format_instructions())

#%% model
MODEL_NAME="openai/gpt-oss-120b"
model = ChatGroq(model=MODEL_NAME, temperature=0)

#%% chain
chain = prompt_template | model | parser

def get_movies_from_plot(plot: str) -> dict:
    """
    Get movie recommendations based on a plot description.
    
    Args:
        plot (str): The plot description to search for movies
        
    Returns:
        dict: Dictionary containing movies with their details
    """
    try:
        # Invoke the chain with the plot
        chain_inputs = {"plot": plot}
        result = chain.invoke(chain_inputs)
        
        # Convert to dictionary format
        movies_dict = {
            "total_movies": len(result.movies),
            "movies": []
        }
        
        for movie in result.movies:
            movie_data = {
                "title": movie.title,
                "main_characters": movie.main_characters,
                "director": movie.director,
                "release_year": movie.release_year
            }
            movies_dict["movies"].append(movie_data)
        
        return movies_dict
        
    except Exception as e:
        return {
            "error": str(e),
            "total_movies": 0,
            "movies": []
        }

#%% TEST
# get_movies_from_plot(plot="detective")

#%% Example usage (for testing)
if __name__ == "__main__":
    # Test the function
    result = get_movies_from_plot("detective")
    print("Function result:")
    print(result)
