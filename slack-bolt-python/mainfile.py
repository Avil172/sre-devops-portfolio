#from sqlite3 import Timestamp
#import slack
import os
import slack_sdk
import aem
from pathlib import Path
from dotenv import load_dotenv
#from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
#from datetime import datetime, timedelta
#import time
import re
import logging
#from slack_bolt import App
from slack_bolt.async_app import AsyncApp
from slack_bolt.adapter.flask import SlackRequestHandler
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

app = AsyncApp(
    token=os.environ.get("SLACK_TOKEN"),
    signing_secret=os.environ.get("SIGNING_SECRET")
)

client = slack_sdk.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']

print("=====================================================")
print(BOT_ID)
print("=====================================================")

app.message(re.compile('|'.join(aem.results)))(aem.message_response)
app.action("radio-actions")(aem.action_button_click)
app.action("static_select-action")(aem.other_action)
app.action("take-out-of-service")(aem.take_out_of_service)
app.action("check-bundles")(aem.check_bundles)
app.action("restart-aem")(aem.restart)
app.action("put-in-service")(aem.put_in_service)
app.action("systemcheck")(aem.services_systemcheck)

from flask import Flask, request

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

#@flask_app.route("/slack/events", methods=["POST"])
#def slack_events():
#    return handler.handle(request)

if __name__ == "__main__":
    app.start(80)
