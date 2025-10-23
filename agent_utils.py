import os 
from pydantic_ai.agent import Agent 
from pydantic_ai.common_tools.tavily import tavily_search_tool

os.environ['GROQ_API_KEY'] = "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"
TAVILI_API_KEY = "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"
agent  =  Agent(
    "groq:llama-3.1-8b-instant",
    tools=[tavily_search_tool(TAVILI_API_KEY)],
    system_prompt="Search Tavily for the given query and return the results.",
)

def get_search_results(query: str)->str:
    result = agent.run_sync(query)
    return result.output
