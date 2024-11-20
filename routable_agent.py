from swarm import Agent

class RoutableAgent:
    def __init__(self, agent: Agent, agent_id: str, agent_description: str):
        self.agent = agent
        self.agent_id = agent_id
        self.agent_description = agent_description

