import os
from slack_cleaner2 import *

s = SlackCleaner(os.getenv('SLACK_TOKEN'))

def print_stuff():
  print('users', s.users)
  print('public channels', s.channels)
  print('private channels', s.groups)
  print('instant messages', s.ims)
  print('multi user direct messages', s.mpim)

def delete_from_channel():
  for msg in s.c['bot-alerts-red'].msgs():
    msg.delete(replies=True, files=True)

def delete_from_ims():
  for c in s.ims:
    if c.name == 'j.doe':
      for msg in c.msgs():
        if msg.user == s.myself:
          msg.delete(replies=True, files=True)


print_stuff()

# delete all messages from a channel channels
# delete_from_channel()

# Delete all direct messages between you and another user
# delete_from_ims()