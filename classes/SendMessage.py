import requests
from dotenv import load_dotenv
import os


class SendMessage:
    def __init__(self, chatID, message):
        self.chatID = chatID
        self.message = message

    def send(self):
        load_dotenv()
        telegramToken = os.getenv("TELEGRAM_BOT_TOKEN")
        url = f"https://api.telegram.org/bot{telegramToken}/sendMessage"
        data = {
            "chat_id": self.chatID,
            "text": self.message
        }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Message Sent successfully!")
        else:
            print("Error sending message:", response.text)
