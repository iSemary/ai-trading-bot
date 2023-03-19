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

    def sendQuestionButtons(self):
        load_dotenv()
        telegramToken = os.getenv("TELEGRAM_BOT_TOKEN")
        url = f"https://api.telegram.org/bot{telegramToken}/sendMessage"
        headers = {"Content-Type": "application/json"}
        data = {
            "chat_id": self.chatID,
            "text": self.message,
            "reply_markup": {
                "inline_keyboard": [
                    [
                        {
                            "text": "Button 1",
                            "callback_data": "button_1"
                        },
                        {
                            "text": "Button 2",
                            "callback_data": "button_2"
                        }
                    ],
                    [
                        {
                            "text": "Button 3",
                            "callback_data": "button_3"
                        }
                    ]
                ]
            }
        }

        data = json.dumps(data)
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print("Button Message Sent successfully!")
        else:
            print("Error sending message:", response.text)
