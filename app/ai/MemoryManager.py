from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, trim_messages

from app.persist import db
from app.persist import UserMessage, BotMessage
from app.ai.aux import count_tokens_from_messages

class MemoryManager:
    def add(self, question: str, answer: str, session_id: int):
        user_message = UserMessage(message=question, session_id=session_id)
        bot_message = BotMessage(message=answer, session_id=session_id)

        db.session.add(user_message)
        db.session.add(bot_message)

        db.session.commit()


    def get_messages(self, session_id: int):
        res = []

        user_messages = db.session.query(UserMessage).filter_by(session_id=session_id).all()

        res.extend(HumanMessage(user_message.message) for user_message in user_messages)

        ai_messages = db.session.query(BotMessage).filter_by(session_id=session_id).all()

        res.extend(AIMessage(ai_message.message) for ai_message in ai_messages)

        return res


    def get_trimmed_memory(self, session_id: int):
        messages = self.get_messages(session_id)

        trimmed_messages = trim_messages(
            messages,
            token_counter=lambda msgs: count_tokens_from_messages(msgs),
            max_tokens=500,
            strategy='last'
        )

        trimmed_history = InMemoryChatMessageHistory()

        trimmed_history.add_messages(trimmed_messages)

        return trimmed_history