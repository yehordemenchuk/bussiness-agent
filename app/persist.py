from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class Session(db.Model):
    __tablename__ = 'session'
    session_id = Column(Integer, primary_key=True, index=True)
    user_messages = relationship('UserMessage', backref='session', lazy=True)
    bot_messages = relationship('BotMessage', backref='session', lazy=True)

class BotMessage(db.Model):
    __tablename__ = 'bot_message'
    id = Column(Integer, primary_key=True)
    message = Column(String(200), nullable=False)
    session_id = Column(Integer, ForeignKey('session.session_id'), nullable=False)

class UserMessage(db.Model):
    __tablename__ = 'user_message'
    id = Column(Integer, primary_key=True)
    message = Column(String(200), nullable=False)
    session_id = Column(Integer, ForeignKey('session.session_id'), nullable=False)