import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://singhsayan10-1755085339562.atlassian.net/rest/api/3/issue"

    EMAIL = "YOUR_MAIL_ID"
    API_TOKEN = "YOUR_API_TOKEN_HERE"  

    auth = HTTPBasicAuth(EMAIL, API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "text": "Order entry fails when selecting supplier.",
                                "type": "text"
                            }
                        ]
                    }
                ]
            },
            "project": {
                "key": "SCRUM"  # <-- replace with your project key
            },
            "issuetype": {
                "id": "10004"  # <-- replace with correct Jira issue type ID
            },
            "summary": "Main order flow broken"
        },
        "update": {}
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    print("Jira API Status:", response.status_code)
    print("Jira API Response:", response.text)

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
