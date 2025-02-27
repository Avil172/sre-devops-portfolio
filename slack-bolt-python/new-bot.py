#from sqlite3 import Timestamp
#import slack
import os
import slack_sdk
import re
from pathlib import Path
from dotenv import load_dotenv
#from flask import Flask, request, Response
from slackeventsapi import SlackEventAdapter
import string
#from datetime import datetime, timedelta
#import time
import logging
import requests
import itertools
import rundeckpython
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


chars = "aemoptions"
results = list(map(''.join, itertools.product(*zip(chars.upper(), chars.lower()))))


@app.message(re.compile('|'.join(results)))
async def message_response(message, say):
    # say() sends a message to the channel where the event was triggered
    global uid_initiator
    print("======================================================================================================================")
    uid_initiator=message['user']
    print(uid_initiator)
    print("===========================================================================================================================")
    if BOT_ID in message['text']:
        await say(
        thread_ts=message['ts'],
        blocks=[
        {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "Troubleshooting options",
            }
        },
        {
            "type": "actions",
            "elements": [
                {
                    "type": "radio_buttons",
                    "options": [
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Restart AEM",
                                "emoji": True
                            },
                            "value": "value-0"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Systemcheck",
                                "emoji": True
                            },
                            "value": "value-1"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Clear Cache",
                                "emoji": True
                            },
                            "value": "value-2"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Create Trouble Ticket",
                                "emoji": True
                            },
                            "value": "value-3"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Snapshot Recovery",
                                "emoji": True
                            },
                            "value": "value-4"
                        },
                        {
                            "text": {
                                "type": "plain_text",
                                "text": "Others",
                                "emoji": True
                            },
                            "value": "value-5"
                        }],
                    "action_id": "radio-actions"
                        }
            ]
        }
        ],
        text=f"Hey there <@{message['user']}>!")


@app.action("radio-actions")
async def action_button_click(body, ack, say):
    # Acknowledge the action
#   ack()
#   say(f"<@{body['user']['id']}> wants to {selection}")
    selection=body['actions'][0]['selected_option']['text']['text']
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    with open('auth_users_list.txt') as f:
        if username in f.read() and uid_initiator == uid_actor:
            if selection == 'Systemcheck':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "systemcheck"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname",
                       }
                    }
                    ])
            elif selection == 'Restart AEM':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "restart-aem"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname",
                       }
                    }
                    ])
            elif selection == 'Clear Cache':
                await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                    {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select app",
                                "emoji": True
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "CC",
                                        "emoji": True
                                    },
                                    "value": "value-0"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "APP",
                                        "emoji": True
                                    },
                                    "value": "value-1"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Helpx",
                                        "emoji": True
                                    },
                                    "value": "value-2"
                                }
                            ],
                            "action_id": "application"
                        },
                        {
                            "type": "static_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select environment",
                                "emoji": True
                            },
                            "options": [
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "dev",
                                        "emoji": True
                                    },
                                    "value": "value-0"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "QA",
                                        "emoji": True
                                    },
                                    "value": "value-1"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Stage",
                                        "emoji": True
                                    },
                                    "value": "value-2"
                                },
                                {
                                    "text": {
                                        "type": "plain_text",
                                        "text": "Prod",
                                        "emoji": True
                                    },
                                    "value": "value-3"
                                }
                            ],
                            "action_id": "environment"
                        }
                        ]}])
            elif selection == 'Snapshot Recovery':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "snapshot-recovery"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname",
                       }
                    }
                    ])
            elif selection == 'Create Trouble Ticket':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "create-trouble-ticket"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname",
                       }
                    }
                    ])
            elif selection == "Others":
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=[
                    {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Pick an action from the dropdown list"
                    },
                    "accessory": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select an item",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Put into service",
                                    "emoji": True
                                },
                                "value": "value-0"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Take out of service",
                                    "emoji": True
                                },
                                "value": "value-1"
                            },
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": "Check bundles",
                                    "emoji": True
                                },
                                "value": "value-2"
                            }
                            ],
                            "action_id": "static_select-action"
                        }}])
        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "unauthorized",
                }}])
    f.close()

@app.action("static_select-action")
async def other_action(body, say):
    selection=body['actions'][0]['selected_option']['text']['text']
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    with open('auth_users_list.txt') as f:
        if username in f.read() and uid_initiator == uid_actor:
            print("===========================================================================")
            print(selection)
            print("===========================================================================")
            if selection == 'Put into service':
               await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "put-into-service"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname",
                       }
                    }
                    ])
            elif selection == 'Take out of service':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "take-out-of-service"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname",
                       }
                    }
                    ])
            elif selection == 'Check bundles':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=[
                    {
                        "dispatch_action": True,
                        "type": "input",
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "check-bundles"
                        },
                        "label": {
                            "type": "plain_text",
                            "text": "Enter Hostname",
                       }
                    }
                    ])
        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "unauthorized",
                }}])
    f.close()

pub="pub"
auth="author"

def formaturl(url):
    if re.match(".*aws12[25].organization.com$", url) or re.match(".*corp.organization.com$", url):
        if not re.match('(?:http)://', url):
            if pub in url:
                return f"http://{url}:8080/services/systemcheck"
            elif auth in url:
                if re.match(".*corp.organization.com$", url):
                    return f"https://{url}/services/systemcheck"
                else:
                    return f"http://{url}:4502/services/systemcheck"
    return url


def remove(string):
    return string.replace(" ", "")


@app.action("take-out-of-service")
async def systemcheck(body,say):
    await say(
    thread_ts=body['container']['thread_ts'],
    blocks=[
        {
         "type": "section",
         "text": {
            "type": "plain_text",
            "text": "Take out of service is still WIP. Please check back later",
        }}])

@app.action("check-bundles")
async def action_button_click(body, say):
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    user_input_action=body['actions'][0]['value']
    user_input=remove(user_input_action)
    x = re.search(".*aws12[25].organization.com$", user_input)
    y = re.search(".*corp.organization.com$", user_input)
    if uid_initiator == uid_actor:
        if x or y:
            servername=body['actions'][0]['value']
            server_name=remove(servername)
            print("==========================================================================================")
            print(server_name)
            print("============================================================================================")
            hostname=formaturl(server_name)
            print(hostname)
            bundlestatus=rundeckpython.checkbundles(hostname)
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": bundlestatus
                }}])

        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Can't find server"
                }}])
    else:
        await say(
            thread_ts=body['container']['thread_ts'],
            blocks=[
            {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "unauthorized",
            }}])

@app.action("restart-aem")
async def put_in_service(body, say):
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    user_input_action=body['actions'][0]['value']
    user_input=remove(user_input_action)
    x = re.search(".*aws12[25].organization.com$", user_input)
    y = re.search(".*corp.organization.com$", user_input)
    if uid_initiator == uid_actor:
        if x or y:
            servername=body['actions'][0]['value']
            server_name=remove(servername)
            print("==========================================================================================")
            print(server_name)
            print("============================================================================================")
            hostname=formaturl(server_name)
            print(hostname)
            restartservice=rundeckpython.restart(hostname)
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": restartservice
                }}])

        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Can't find server"
                }}])
    else:
        await say(
            thread_ts=body['container']['thread_ts'],
            blocks=[
            {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "unauthorized",
            }}])

@app.action("put-into-service")
async def put_in_service(body, say):
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    user_input_action=body['actions'][0]['value']
    user_input=remove(user_input_action)
    x = re.search(".*aws12[25].organization.com$", user_input)
    y = re.search(".*corp.organization.com$", user_input)
    if uid_initiator == uid_actor:
        if x or y:
            servername=body['actions'][0]['value']
            server_name=remove(servername)
            print("==========================================================================================")
            print(server_name)
            print("============================================================================================")
            hostname=formaturl(server_name)
            print(hostname)
            putinservice=rundeckpython.putinservice(hostname)
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": putinservice
                }}])

        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Can't find server"
                }}])
    else:
        await say(
            thread_ts=body['container']['thread_ts'],
            blocks=[
            {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "unauthorized",
            }}])

@app.action("systemcheck")
async def services_systemcheck(body, say):
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    user_input_action=body['actions'][0]['value']
    user_input=remove(user_input_action)
    x = re.search(".*aws12[25].organization.com$", user_input)
    y = re.search(".*corp.organization.com$", user_input)
    if uid_initiator == uid_actor:
        if x or y:
            servername=body['actions'][0]['value']
            server_name=remove(servername)
            print("==========================================================================================")
            print(server_name)
            print("============================================================================================")
            hostname=formaturl(server_name)
            print(hostname)
            syscheck=rundeckpython.systemcheck(hostname)
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": syscheck
                }}])

        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=[
                {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Can't find server"
                }}])
    else:
        await say(
            thread_ts=body['container']['thread_ts'],
            blocks=[
            {
            "type": "section",
            "text": {
                "type": "plain_text",
                "text": "unauthorized",
            }}])

from flask import Flask, request

flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

if __name__ == "__main__":
    app.start(80)
