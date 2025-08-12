from pydantic import BaseModel
from agents import (Agent,
                     GuardrailFunctionOutput,
                     OutputGuardrailTripwireTriggered,
                     RunContextWrapper,
                     Runner,
                     output_guardrail
)

import asyncio
from my_config import config


class MessageOutput(BaseModel):
  response : str

class Mathoutput(BaseModel):
   reasoning: str
   is_math: bool
   
   
guardrail_agent = Agent(
   name = "Guardrail Check",
   instructions = "Check if  math output",
   output_type = Mathoutput
)

@output_guardrail 
async def math_guardrail(
    ctx : RunContextWrapper,agent : Agent, output : MessageOutput
  ) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, output.response, context=ctx.context)

    return GuardrailFunctionOutput(
       output_info = result.final_output,
       tripwire_triggered = result.final_output.is_math
    )
  
agent = Agent (
          name =  "costumer support agent  ",
          instructions= "You are a customer support agent. Help users with their questions in a friendly and helpful manner.",
          output_guardrails=[math_guardrail],
          output_type= MessageOutput
    )
    
    
async def main():
    try:
      await Runner.run(
         starting_agent=agent,
         input="what is the answer of 2 * 8 = "
)
      print("guardrail not working")
    except OutputGuardrailTripwireTriggered:
      print("math output")
            


if __name__ =="__main__":
  asyncio.run(main())