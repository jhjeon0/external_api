import os
import slack_sdk


bot_token = os.getenv("BOT_TOKEN")
channel_id = os.getenv("CHANNEL_ID")


# warning 때문에 text가 들어가긴 해야함, attachments 선택사항
def send_msg(title: str, msg: str):
    attachments = [
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
    ]
    client = slack_sdk.WebClient(token=bot_token)
    client.chat_postMessage(
        channel=channel_id,
        text=msg,
        attachments=attachments,
    )
