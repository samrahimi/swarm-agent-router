    
from swarm import Agent
from routable_agent import RoutableAgent


class AgentRouter:
    """
    AgentRouter automates the process of transferring users between agents... Just make your agents (and optionally a moderator agent)
    and pass them to the AgentRouter. The AgentRouter will take care of the rest. 

    Note: agents must have agent_id, agent_description, and name attributes set in order to be routable

    """
    def transfer_to_agent(self,agent_id, notes="Routing to agent."):
        """
        Called by one agent to transfer the user to another agent. Please make sure that the agent_id is in the list of available agents 
        """

        print(f"Transferring to agent {agent_id}.  Notes: {notes}")
        return self.available_agents[agent_id]



    def transfer_to_moderator(self, reason, notes, is_serious_offense=False):
        """
        If a user is being rude or offensive, we transfer them to the moderator. The moderator will explain what they did wrong and give them proper punishment.
        reason: The reason why the user is being transferred to the moderator (i.e. "user is being rude")
        notes: Anything relevant about the context or the offending behavior (i.e. "user told me to fuck off when i explained that his iPhone 5 was out of warranty")
        is_serious_offense: if the user's behavior is so incredibly bad that you believe they should be permanently banned from calling Samsung support, set this flag (moderator will decide if indeed such a punishment is required) 
        """

        print(f"Transferring to moderator.  Reason: {reason}. Notes: {notes}")
        return self.moderator


    def __init__(self, routable_agents: list[RoutableAgent],  moderator: Agent=None):
        self.moderator = moderator
        self.available_agents = {}

        self.available_agents_text = """
        Available Agents
        ----------------
        agent_id, name, agent_description
        """
        # Create a dictionary of available agents with matching document 
        for routable_agent in routable_agents:
            self.available_agents[routable_agent.agent_id] = routable_agent.agent 
            self.available_agents_text += f"{routable_agent.agent_id}, {routable_agent.agent.name}, {routable_agent.agent_description}\n"

        # append available agents text to the instructions of each agent
        for agent_id in self.available_agents:
            self.available_agents[agent_id].instructions += self.available_agents_text

            # all agents can transfer to the moderator to handle abusive customers (if a moderator was provided)
            if (self.moderator):
                self.available_agents[agent_id].functions.append(self.transfer_to_moderator)

            # all agents can transfer to other agents
            self.available_agents[agent_id].functions.append(self.transfer_to_agent)
        
        # if a moderator was provided, set them up with the list of available agents and the ability to transfer to them
        if self.moderator:
            self.moderator.instructions += self.available_agents_text
            self.moderator.functions.append(self.transfer_to_agent)


