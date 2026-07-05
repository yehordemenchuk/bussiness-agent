from app.tools import call_api
from app.config import Config
from langchain_core.tools import tool

@tool
def get_posts():
    return call_api(f'{Config.REST_ADDRESS}:{Config.POST_SERVICE_PORT}/api/v1/posts/')

@tool
def get_users():
    return call_api(f'{Config.REST_ADDRESS}:{Config.USER_SERVICE_PORT}/api/v1/users/')