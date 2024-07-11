import requests
import json
import os


workflows_url = os.getenv("WORKFLOWS_URL")


def write_to_teams_channel_use_workflows(title: str, msg: str):
    data = json.dumps(
        {
            "type": "message",
            "attachments": [
                {
                    "contentType": "text/plain",
                    "contentUrl": "null",
                    "content": {
                        "type": "AdaptiveCard",
                        "version": "1.2",
                        "body": [
                            {"type": "TextBlock", "text": f"TITLE: {title}" + msg}
                        ],
                    },
                }
            ],
        }
    )
    headers = {
        "Content-Type": "application/json",
    }

    return requests.request("POST", workflows_url, headers=headers, data=data)
