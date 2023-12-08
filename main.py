from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import os

from core.language_model import agent_executor
from core.logging import logger


load_dotenv()
SLACK_BOT_TOKEN=os.getenv('SLACK_BOT_TOKEN')
SLACK_APP_TOKEN=os.getenv('SLACK_APP_TOKEN')
SLACK_BOT_USER_ID=os.getenv('SLACK_BOT_USER_ID')

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def handle_mentions(body, say):
    """
    Event listener for mentions in Slack.
    When the bot is mentioned, this function processes the text and sends a response.

    Args:
        body (dict): The event data received from Slack.
        say (callable): A function for sending a response to the channel.
    """
    text = body["event"]["text"]

    mention = f"<@{SLACK_BOT_USER_ID}>"
    text = text.replace(mention, "").strip()

    logger.info(f'User sent Message to the bot: {text}')

    response = agent_executor.invoke({'input': text})

    logger.info(f"Bot Response: {response.get('output')}")

    say(response.get('output'))

def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

if __name__=='__main__':
    main()