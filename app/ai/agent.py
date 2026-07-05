from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

from app.ai.misc import read_txt
from app.config import Config
from app.tools import search_in_internet
from app.tools.retriever_tools import retriever_tool

MAX_LENGTH = 2048

SYSTEM_PROMPT = read_txt(Config.SYSTEM_PROMPT_PATH)

llm = ChatOpenAI(
            model_name=Config.MODEL_NAME,
            openai_api_key=Config.OPENAI_API_KEY,
            openai_api_base=Config.OPENAI_API_BASE,
            temperature=0.7,
            max_tokens=MAX_LENGTH,
)

tools = [
    search_in_internet,
    retriever_tool
]

prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        MessagesPlaceholder("history"),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

agent = create_tool_calling_agent(llm, tools, prompt)

executor = AgentExecutor(
    agent=agent,
    tools=tools
)