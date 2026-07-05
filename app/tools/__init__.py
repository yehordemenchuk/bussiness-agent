import requests
from langchain_core.tools import tool

from app import Config
from app.logger import logger

def call_api(url: str, method: str = "GET", headers : dict = None, body: dict = None):
    response = (requests.get(url, headers=headers, params=body, timeout=10) if method == "GET"
        else requests.post(url, headers=headers, json=body, timeout=10))

    logger.debug(f'{url} response status code: {response.status_code}')

    logger.debug(f'{url} response body: {response.json()}')

    return response

@tool
def search_in_internet(query: str):
    """This tool MUST be used whenever the user asks about:

                                    - market data
                                    - industry analysis
                                    - company information
                                    - financial information
                                    - news or current events
                                    - any real-world or external factual information

                                    STRICT RULE:
                                    You are NOT allowed to answer these questions from internal knowledge.
                                    You MUST call this tool before producing any answer.

                                    The tool returns web search results for factual grounding.

                                    Input must be a plain string search query."""
    payload = {
        "api_key": Config.TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": 5
    }

    response = call_api("https://api.tavily.com/search", "POST", body=payload)

    logger.debug(f'Response from in internet: {response.json()}')

    return response.json()