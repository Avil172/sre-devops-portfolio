import itertools
import re
import rundeckpython
import rich_messages
#import rundecktwo

chars = "aemoptions"
results = list(map(''.join, itertools.product(*zip(chars.upper(), chars.lower()))))
BOT_ID="U0340590727"

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

async def message_response(message, say):
    # say() sends a message to the channel where the event was triggered
    if BOT_ID in message['text']:
        await say(
        thread_ts=message['ts'],
        blocks=rich_messages.initial_troubleshooting_block,
        text=f"Hey there <@{message['user']}>!")


async def action_button_click(body, say):
    selection=body['actions'][0]['selected_option']['text']['text']
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    if uid_actor == body['message']['parent_user_id']:
        if selection == 'Systemcheck':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=rich_messages.systemcheck_block)
        elif selection == 'Restart AEM (In development)':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=rich_messages.restart_aem_block)
        elif selection == 'Clear Cache (In development)':
                await say(
                thread_ts=body['container']['thread_ts'],
                blocks=rich_messages.clear_cache_block)
        elif selection == 'Snapshot Recovery (In development)':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=rich_messages.snapshot_recovery_block)
        elif selection == 'Create Trouble Ticket (In development)':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=rich_messages.create_trouble_ticket_block)
        elif selection == "Others (In development)":
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=rich_messages.others_block)
        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=rich_messages.unauthorized_block)

async def other_action(body, say):
    selection=body['actions'][0]['selected_option']['text']['text']
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    with open('auth_users.txt') as f:
        if uid_actor == body['message']['parent_user_id']:
            print("===========================================================================")
            print(selection)
            print("===========================================================================")
            if selection == 'Put into service (In development)':
                selection=selection
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=rich_messages.put_in_service_block)
            elif selection == 'Take out of service (In development)':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=rich_messages.take_out_of_service_block)
            elif selection == 'Check bundles (In development)':
                await say(
                    thread_ts=body['container']['thread_ts'],
                    blocks=rich_messages.check_bundles_block)
        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=rich_messages.unauthorized_block)
    f.close()

async def take_out_of_service(body,say):
    await say(
    thread_ts=body['container']['thread_ts'],
    blocks=rich_messages.take_outof_service_action)

async def check_bundles(body, say):
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    user_input_action=body['actions'][0]['value']
    user_input=remove(user_input_action)
    x = re.search(".*aws12[25].organization.com$", user_input)
    y = re.search(".*corp.organization.com$", user_input)
    if uid_actor == body['message']['parent_user_id']:
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
                blocks=rich_messages.bundlestatus_action)

        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=rich_messages.cant_find_server_block)
    else:
        await say(
            thread_ts=body['container']['thread_ts'],
            blocks=rich_messages.unauthorized_block)

matches = ["stage", "prod"]

async def restart(body, say):
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    user_input_action=body['actions'][0]['value']
    user_input=remove(user_input_action)
    x = re.search(".*aws12[25].organization.com$", user_input)
    y = re.search(".*corp.organization.com$", user_input)
    if uid_actor == body['message']['parent_user_id']:
        if x or y:
            servername=body['actions'][0]['value']
            server_name=remove(servername)
            print("==========================================================================================")
            print(server_name)
            print("============================================================================================")
            hostname=formaturl(server_name)
            print(hostname)
            file1=open("auth_users.txt", "r")
            readfile=file1.read()
            if username in readfile:
                restartservice=rundeckpython.restart(server_name)
                print("==========================================================================================")
                print(server_name)
                print("============================================================================================")
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
                if any(x in server_name for x in matches):
                    print("==========================================================================================")
                    print(server_name)
                    print("============================================================================================")
                    await say(
                        thread_ts=body['container']['thread_ts'],
                        blocks=rich_messages.restricted_to_ops)
                else:
                    print("==========================================================================================")
                    print(server_name)
                    print("============================================================================================")
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
            file1.close()

        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=rich_messages.cant_find_server_block)
    else:
        await say(
            thread_ts=body['container']['thread_ts'],
            blocks=rich_messages.initiate_new_conversation_block)

async def put_in_service(body, say):
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    user_input_action=body['actions'][0]['value']
    user_input=remove(user_input_action)
    x = re.search(".*aws12[25].organization.com$", user_input)
    y = re.search(".*corp.organization.com$", user_input)
    if uid_actor == body['message']['parent_user_id']:
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
                }}]
                )
        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=rich_messages.cant_find_server_block)
    else:
        await say(
            thread_ts=body['container']['thread_ts'],
            blocks=rich_messages.unauthorized_block)

async def services_systemcheck(body, say):
    username=body['user']['username']
    uid_actor=(body['user']['id'])
    user_input_action=body['actions'][0]['value']
    user_input=remove(user_input_action)
    x = re.search(".*aws12[25].organization.com$", user_input)
    y = re.search(".*corp.organization.com$", user_input)
    if uid_actor == body['message']['parent_user_id']:
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
                }}]
                )
        else:
            await say(
                thread_ts=body['container']['thread_ts'],
                blocks=rich_messages.cant_find_server_block)
    else:
        await say(
            thread_ts=body['container']['thread_ts'],
            blocks=rich_messages.initiate_new_conversation_block)
