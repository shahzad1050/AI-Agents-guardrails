from agents import Agent, handoff,RunContextWrapper,Runner
from pydantic import BaseModel
from dotenv import load_dotenv


_:bool = load_dotenv()

class RefundData(BaseModel):
    reason : str


billing_agent = Agent(name="billing_agent")
refund_agent  = Agent(name ="refund_agent")


async def on_handoff_func(ctx:RunContextWrapper,input_data:RefundData):
   print(f"refund_data called with {input_data}")

triage_agent = Agent(name ="Triage_agent",
                    handoffs=[billing_agent,
                              handoff(refund_agent,on_handoff= on_handoff_func,
                                      input_type = RefundData
                                      )
                                      ])

result = Runner.run_sync(triage_agent,"i want to refund my laptop it is not working fine please call refund agent")

print(result.final_output)