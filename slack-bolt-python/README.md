# slack-bolt
shortcuts

```python
async def services_systemcheck(body, say):
    username=body['user']['username']
    userid=(body['user']['id'])
    user_input_action=body['actions'][0]['value']  # in case user is writing something into a text box
    parent_user=body['message']['parent_user_id']  # in case action is coming from another action
    selection=body['actions'][0]['selected_option']['text']['text']  # in case user selects one option from multiple selections, eg- radio buttons
```
