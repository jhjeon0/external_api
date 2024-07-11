import os
import pymsteams

incoming_webhook_url = os.getenv("INCOMING_WEBHOOK_URL")


def write_to_teams_channel(title: str, msg: str):
    try:
        teams_message = pymsteams.connectorcard(incoming_webhook_url)
        teams_message.title(title)
        teams_message.text(msg)
        teams_message.send()
    except ValueError:
        print("Error-log teams 전송 실패")
