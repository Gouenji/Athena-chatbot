import os
from slackclient import SlackClient


BOT_NAME = 'athena'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


if __name__ == "__main__":
    os.system(str("export SLACK_BOT_TOKEN='xoxb-131118821488-etvjp2jrYDMHMG3EaE3sZ6MA'"))
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                #print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
        os.system("export BOT_ID=\'"+str(user.get('id'))+"\'")
    else:
        print("could not find bot user with the name " + BOT_NAME)
