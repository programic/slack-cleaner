import os
from slack_cleaner2 import *

def print_stuff(s):
    print('users', s.users)
    print('public channels', s.channels)
    print('private channels', s.groups)
    print('instant messages', s.ims)
    print('multi user direct messages', s.mpim)

def delete_from_channel(s):
    for msg in s.c['bot-alerts-red'].msgs():
        msg.delete(replies=True, files=True)

def delete_from_ims(s):
    for c in s.ims:
        if c.name == 'j.doe':
            for msg in c.msgs():
                if msg.user == s.myself:
                    msg.delete(replies=True, files=True)

def main():
    s = SlackCleaner(os.getenv('SLACK_TOKEN'))

    print_stuff(s)
    # delete all messages from a channel
#     delete_from_channel(s)
    # Delete all messages between you and another user (ims)
#     delete_from_ims(s)

if __name__ == '__main__':
    main()