from agents import OpenAIChatCompletionsModel, RunConfig,AsyncOpenAI#
import os

gemini_api_key ="AIzaSyCAPDgBRSrSJuJdZbtgQGOK72-O8Nk2WQE"

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set")

client= AsyncOpenAI(
    api_key=gemini_api_key,
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