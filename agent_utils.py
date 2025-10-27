import os 
from pydantic_ai.agent import Agent 
from pydantic_ai.common_tools.tavily import tavily_search_tool

os.environ['GROQ_API_KEY'] = ""
TAVILI_API_KEY = ""
agent  =  Agent(
    "groq:llama-3.1-8b-instant",
    tools=[tavily_search_tool(TAVILI_API_KEY)],
    system_prompt="Search Tavily for the given query and return the results.",
)

def get_search_results(query: str)->str:
    result = agent.run_sync(query)
    return result.output
