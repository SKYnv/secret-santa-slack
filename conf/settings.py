import os

PORT = os.getenv("PORT", 80)
DATABASE_URL = os.getenv('DATABASE_URL')
SLACK_BOT_TOKEN = os.getenv('SLACK_BOT_TOKEN')