from agents import Agent,Runner
from my_config import config
from typing_extensions import TypedDict

class MyDataType(TypedDict):
    num1 : int
    num2 : int
    sum : int

simple_agent= Agent(
    name = "Assistant",
    instructions= " you are a helpfull assistant",
    output_type=MyDataType
)

result = Runner.run_sync(
    starting_agent=simple_agent,
    input="what is 3 plus 8",
    run_config=config 
)

print(result.final_output)
print(type(result.final_output))
