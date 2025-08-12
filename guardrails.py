from agents import Agent,GuardrailFunctionOutput,InputGuardrailTripwireTriggered,RunContextWrapper,input_guardrail,Runner

from my_config import config
import asyncio 


@input_guardrail
async def math_guardrail(
    context: RunContextWrapper, agent: Agent, input: str 
) -> GuardrailFunctionOutput:
    print(f"guardrail is running with {input}")
    return GuardrailFunctionOutput(
        output_info="Math output",
        tripwire_triggered=True
)


agent = Agent(  
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[math_guardrail]
)
async def main():
  try:
      result = await Runner.run(
       starting_agent=agent,
       input="Hello, what is 7 + 5 =  ",
        run_config=config 
)
      print(result.final_output)

 
  except InputGuardrailTripwireTriggered as e:
       print("Guardrail blocked the input:", e)




if __name__ == "__main__":
     asyncio.run(main())

