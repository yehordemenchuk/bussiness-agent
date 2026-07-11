import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MODEL_NAME = "gpt-4o-mini"

    OPENAI_API_KEY = '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'

    OPENAI_API_BASE = "https://api.openai.com/v1"

    LANGCHAIN_API_KEY =

    LANGCHAIN_PROJECT = 'business-ai-service'

    LANGCHAIN_ENDPOINT = 'https://api.smith.langchain.com'

    LANGCHAIN_TRACING_V2 = "true"

    HUBSPOT_API_KEY =

    SLACK_API_TOKEN =

    REST_ADDRESS = "http://localhost"

    EMBEDDINGS_MODEL_NAME = "all-MiniLM-L6-v2"

    TAVILY_API_KEY =

    SYSTEM_PROMPT_PATH = os.path.join("prompt", "system_prompt.txt")

    POST_SERVICE_PORT = 8080

    USER_SERVICE_PORT = 8081