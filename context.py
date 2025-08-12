
from agents import Agent, Runner, function_tool, RunContextWrapper
from my_config import config
from dataclasses import dataclass


@dataclass
class UserInfo:
    name: str
    designation: str

local_context = UserInfo(name="shahzad", designation="IT Expert")
"""alwsys use fetch user data of tools the given name and designation is there init """
@function_tool
async def fetch_user_data(wrapper: RunContextWrapper):

    context: UserInfo = wrapper.context
    return f"User name is {context.name} and designation is {context.designation}"


context_agent = Agent(
    name="Context Agent",
    instructions= "You are a helpful agent. Always use the available tools to answer questions. "
    "When asked about the user's name or designation, use the 'fetch_user_data' tool.",
    tools=[fetch_user_data]
)

result =Runner.run_sync(
    starting_agent=context_agent,
        input="what is user name and designation",
        run_config=config,
        context=local_context
    )


print(result.final_output)


