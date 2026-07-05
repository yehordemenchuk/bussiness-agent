from langchain_classic.memory import ConversationBufferMemory
from langchain_core.tracers import LangChainTracer

from app.ai.MemoryManager import MemoryManager
from app.ai.agent import executor, agent
from app.ai.misc import setup_tracer
from app.logger import logger

class Chain:
    def __init__(self):
        setup_tracer()

        self.tracer = LangChainTracer()

        self.memory_manager = MemoryManager()

        self.executor = executor

    def get_agent_response(self, message: str, session_id: int) -> str:
        history = self.memory_manager.get_trimmed_memory(session_id)

        memory = ConversationBufferMemory(memory_key="history", return_messages=True)

        memory.chat_memory.add_messages(history.messages)

        logger.debug(f'History: {memory.chat_memory.messages}')

        result = self.executor.invoke({
            "input": message,
            "history": memory.chat_memory.messages
        })

        answer = result["output"]

        logger.info(f"answer: {answer}")

        self.memory_manager.add(message, answer, session_id)

        return answer