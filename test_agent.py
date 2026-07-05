from app.ai.agent import executor
from app.logger import logger

def get_agent_response(message: str) -> str:
    result = executor.invoke({
        "input": message
    })

    logger.debug(result)

    return result['output']

def parse_agent_response(response: dict) -> str:
    messages = response.get('messages', [])

    if not messages:
        return ''

    logger.debug(messages[-1])

    agent_message = messages[-1].content

    return agent_message

print('Ai response: ' + get_agent_response(input('Введите сообщение для нашей обработки: ')))