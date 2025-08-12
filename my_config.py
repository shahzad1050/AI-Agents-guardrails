from agents import OpenAIChatCompletionsModel, RunConfig,AsyncOpenAI
from dotenv import load_dotenv
import os
  
load_dotenv()
_: bool = load_dotenv()

gemini_api_key = os.environ["GEMINI_API_KEY"]


client= AsyncOpenAI(
    api_key="AIzaSyA8-12akKkDprulXQ_ZRtE9KLqya4pwElE",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)


config =  RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True
)