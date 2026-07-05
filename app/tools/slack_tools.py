from langchain_core.tools import tool

from app.tools import call_api
from app.config import Config

@tool
def send_slack(message: str):
    """Send a message to the sales Slack channel."""
    return call_api( "https://slack.com/api/chat.postMessage", "POST",
                     {"Authorization": f"Bearer {Config.SLACK_API_TOKEN}"},
                     {
                         "channel": "#all-test",
                         "text": message
                     })