import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MODEL_NAME = "gpt-4o-mini"

    #OPENAI_API_KEY = 'lallala'

    OPENAI_API_BASE = "https://api.openai.com/v1"

    #LANGCHAIN_API_KEY = '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'

    LANGCHAIN_PROJECT = 'business-ai-service'

    LANGCHAIN_ENDPOINT = 'https://api.smith.langchain.com'

    LANGCHAIN_TRACING_V2 = "true"

    #HUBSPOT_API_KEY = 'pat-eu1-9e3141b7-23cf-4c5a-bfcb-42ecd8ebf5bc'

    #SLACK_API_TOKEN = 'xoxb-11460652193702-11456415326739-DEdFB3n68PS6qwS8de86e71c'

    REST_ADDRESS = "http://localhost"

    EMBEDDINGS_MODEL_NAME = "all-MiniLM-L6-v2"

    #TAVILY_API_KEY = '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'

    SYSTEM_PROMPT_PATH = os.path.join("prompt", "system_prompt.txt")

    POST_SERVICE_PORT = 8080

    USER_SERVICE_PORT = 8081