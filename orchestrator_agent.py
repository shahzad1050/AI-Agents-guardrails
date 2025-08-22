from agents import Agent, Runner
import asyncio
from dotenv import load_dotenv
from my_config import config 

load_dotenv()

spanish_agent = Agent(
    name="Spanish agent",
    instructions="You translate the user's message to Spanish"
)

french_agent = Agent(
    name="French agent",
    instructions="You translate the user's message to French"
)

orchestrator_agent = Agent(
    name="orchestrator_agent",
    instructions=(
        "You are a translation agent. Use the tools provided to translate the user's message."
        "If asked for Spanish or French translation, call the appropriate tool."
    ),
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish"
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French"
        ),
    ]
)

async def main():
    result = await Runner.run(
        orchestrator_agent,
        input="Say 'Hello, how are you?' in Spanish."
    )
    print(result.final_output)

asyncio.run(main())