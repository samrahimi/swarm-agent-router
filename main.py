from swarm import Agent
from swarm import Swarm
from swarm.repl import run_demo_loop
from  dotenv import load_dotenv
from agent_router import AgentRouter
from routable_agent import RoutableAgent

from agents.billing_agent import billing_agent
from agents.tech_support_agent import tech_support_agent
from agents.internet_sales_agent import internet_sales_agent
load_dotenv()
# Define the moderator agent
moderator =Agent(
    name="Moderator", 
    instructions="You are the moderator and we send users to you when they act inappropriately and get out of line. Your job is to examine what the user said that was offensive, and then you must give them an annoying moral lecture and chastise them so they don't do it agian",
)


# Define the operator agent. This agent is the first point of contact for all customer inquiries, but does not have any specific functions. Its only job is to transfer you to one of the other agents who can help you
operator= RoutableAgent(
    agent= Agent(
        name="Operator",
        instructions="You are the switchboard operator for Rogers Communications. Based on the user's request, you must transfer the user to the appropriate agent, and include a brief note about why the user is calling so that the agent can be prepared to assist them.",    
    ),
    agent_id="operator",
    agent_description="Initial point of contact for all customer inquiries",
)

# The agent router automatically handles transfers between RoutableAgents - just pass in a list of them and optionally a moderator
agent_router = AgentRouter([operator, billing_agent, tech_support_agent, internet_sales_agent], moderator)



run_demo_loop(operator.agent, stream=True, debug=True)