# Notion Slack Bot: Automate Your Workflow with AI
A powerful Slack bot that utilizes OpenAI and Langchain to automate your Notion workflows. Say goodbye to repetitive tasks and hello to increased productivity!

## Features
**Natural Language Interface**: Create and edit Notion pages and databases directly from Slack using natural language.
**Simplified Collaboration**: Streamline team collaboration with interactive workflows.
Technologies Used:

## Technologies Used
* **API Integration**: Integrates with Slack and Notion APIs.
* **Programming Language**: Uses Python for easy deployment and customization.
* **AI & NLP Libraries**: Leverages Langchain and OpenAI for advanced automation and natural language processing.
* **Large Language Model**: Employs the powerful gpt-3.5-turbo model for understanding and responding to complex requests.
* **Text Embedding**: Utilizes the text-embedding-ada-002 model for capturing the meaning and relationships within text.
* **Database Storage**: Stores data in a MongoDB database and a vector database for efficient access and retrieval.

## Installation
(Step-by-step instructions for setting up the project on a local machine)

1. Clone the repository:

        git clone https://github.com/deepakVk18/notion-slack-bot.git
   
2. Set up and activate a virtual environment.

        python -m venv venv
        source venv/Scripts/activate   
   
4. Install dependencies
   
        pip install -r requirements.txt
   
5. Configure the environment variables in the .env file.

        NOTION_API_KEY=
        NOTION_DATABASE_ID=
        NOTION_PAGE_ID=
        NOTION_BOT_USERID=
        
        LANGCHAIN_TRACING_V2=true
        LANGCHAIN_API_KEY=
        LANGCHAIN_PROJECT=
        LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
        
        OPENAI_API_KEY=
        
        SLACK_APP_TOKEN=
        SLACK_BOT_TOKEN=
        SLACK_BOT_USER_ID=
        
        MONGODB_USERNAME=
        MONGODB_PASSWORD=
        MONGODB_ATLAS_INDEX_NAME=
        MONGODB_DATABASE_NAME=
        MONGODB_COLLECTION_NAME=

6. Grant the Slack app necessary permissions and install it in your workspace.
7. Run the application:

       python main.py
   
9. Interact with the bot in your Slack workspace using natural language commands.
