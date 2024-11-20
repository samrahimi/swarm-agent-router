# Swarm Multi-Agent Customer Service Team   

This is a demo of how you might go about replacing an enterprise call center with LLM-driven agents. It is not production ready, but it is remarkably stable and gives you a very good starting point for a large scale solution. 

Particularly, each of the agent roles follows instructions very well, and uses their tools properly - I also introduced some routing so that any agent can directly transfer you to any other agent.

## Installation

`pip install -r requirements.txt`

`echo 'OPENAI_KEY=your-openai-key' > .env`

## Start

`python3 main.py`