
#%% packages
import os
from autogen import ConversableAgent
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#%% LLM config
llm_config = {
    "config_list": [
        {"model": "llama-3.3-70b-versatile",
         "api_key": os.getenv("GROQ_API_KEY"),
         "base_url": "https://api.groq.com/openai/v1"}
    ]
}


#%% setup up the agent: Jack, the flat earther
jack_flat_earther = ConversableAgent(
    name="Jack",
    llm_config=llm_config,
    system_message="""
    Du glaubst fest, dass die Erde flach ist.
    Du versuchst andere von deiner Meinung zu überzeugen.
    Mit jeder Antwort, wirst du frustrierter und unverständlicher, dass die andere Person es nicht versteht.
    Du bist stichhaltigen Argumenten gegenüber offen.  
    """,
    human_input_mode="NEVER"
)
#%% set up the agent: Alice, the scientist
alice_scientist = ConversableAgent(
    name="Alice",
    system_message="""
    Du bist rational denkende Wissenschaftlerin und bist davon überzeugt, dass die Erde nahezu rund ist.
    Antworte freundlich, kurz und bündig.
    Du bist stichhaltigen Argumenten gegenüber offen.  
    """,
    llm_config=llm_config,
    human_input_mode="NEVER"
)

#%% start the conversation
result = jack_flat_earther.initiate_chat(
    recipient=alice_scientist,
    message="Hallo, wie weit ist es bis zum Rand der Erde von Hamburg?",
    max_turns=4
)
# %%
alice_scientist.initiate_chat(recipient=jack_flat_earther,
                              message="Wie weit ist es von Hamburg bis zum äußeren Bereich der Erdscheibe?", max_turns=1)
# %%
