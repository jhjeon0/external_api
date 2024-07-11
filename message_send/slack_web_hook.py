import json
import os
import requests


web_hook_url = os.getenv("WEB_HOOK_URL")
user_name = os.getenv("USER")


def send_msg(title: str, msg: str):
    slack_data = {
        "username": user_name,  # 보내는 사람 이름
        "icon_emoji": ":satellite:",
        "attachments": [
            {
                "color": "#9733EE",
                "fields": [
                    {
                        "title": title,
                        "value": msg,
                        "short": "false",
                    }
                ],
            }
        ],
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(web_hook_url, data=json.dumps(slack_data), headers=headers)

    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
