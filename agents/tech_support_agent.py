
from swarm import Agent
from routable_agent import RoutableAgent

def diagnose_internet_outage(account_number: str, postal_code: str):
    """
    Diagnoses the cause of an internet outage based on the account number and postal code provided.
    If the outage is due to a known issue, the estimated time to resolution will be provided.
    If the outage is not due to a known issue, the customer will be advised to contact technical support for further assistance.

    account_number: the account number of the customer experiencing the outage
    postal_code: the postal code of the location where the internet outage is occurring

    Returns a message with the diagnosis and estimated time to resolution, if applicable
    """

    known_outages = {
        "M5V": "There is a known issue affecting internet service in your area. Cause: severed fiber due to squirrel depredation. Our technicians are working to resolve the issue as quickly as possible. The estimated time to resolution is 2 hours.",
        "M4B": "There is a known issue affecting internet service in your area. Cause: DDOS originating in Russia. Our technicians are working to resolve the issue as quickly as possible. The estimated time to resolution is 1 hour.",
    }

    if postal_code in known_outages:
        return known_outages[postal_code]
    else:
        return "Instruct the customer to: unplug the modem, wait 30 seconds, and plug it back in. Remind customer that it takes up to 5 mins to re-connect after powering up. Stay on the phone with them to make sure this resolves the issue. If issue is still not resolved, schedule an in person technician."

tech_support_agent = RoutableAgent(
    agent=Agent(
        name="John",
        instructions="Your name is John! You are the tech support agent for Rogers Communications. Please greet the customer in a friendly way, and then help them with their tech support issue. After you have resolved their issue, either end the call or transfer to another agent if they still have issues to be resolved.",
        functions=[diagnose_internet_outage],
    ),
    agent_id="tech_support_agent",
    agent_description="Tech Support Agent",
)


