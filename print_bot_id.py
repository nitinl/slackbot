import os
import pprint
from slackclient import SlackClient


BOT_NAME = 'dude'

slack_client = SlackClient(os.environ.get('SLACKBOT_API_TOKEN'))

pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        # pp.pprint(users)
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print "could not find bot user with the name " + BOT_NAME