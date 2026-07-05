import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MODEL_NAME = "gpt-4o-mini"



    OPENAI_API_BASE = "https://api.openai.com/v1"

    LANGCHAIN_PROJECT = 'business-ai-service'

    LANGCHAIN_ENDPOINT = 'https://api.smith.langchain.com'

    LANGCHAIN_TRACING_V2 = "true"

    REST_ADDRESS = "http://localhost"

    EMBEDDINGS_MODEL_NAME = "all-MiniLM-L6-v2"

    SYSTEM_PROMPT_PATH = os.path.join("prompt", "system_prompt.txt")

    POST_SERVICE_PORT = 8080

    USER_SERVICE_PORT = 8081