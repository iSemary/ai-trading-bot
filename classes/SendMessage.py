import requests
from dotenv import load_dotenv
import os
import json


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

    def sendQuestionButtons(self, buttons):
# Loading the telegram token from the .env file.
        load_dotenv()
        telegramToken = os.getenv("TELEGRAM_BOT_TOKEN")
        url = f"https://api.telegram.org/bot{telegramToken}/sendMessage"
        headers = {"Content-Type": "application/json"}

        # Creating a list of dictionaries.
        loopedButtons = []
        for button in buttons:
            loopedButton = {
                "text": button,
                "callback_data": "button_1"
            }
            loopedButtons.append(loopedButton)

        data = {
            "chat_id": self.chatID,
            "text": self.message,
            "reply_markup": {
                "inline_keyboard": [loopedButtons]
            }
        }
        # Converting the data to a json format.
        data = json.dumps(data)
        # Sending the data to the telegram API.
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print("Button Message Sent successfully!")
        else:
            print("Error sending message:", response.text)
