# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from twilio.rest import Client
# put your own credentials here
account_sid = "YOUR SID"
auth_token = "YOUR TOKEN"
client = Client(account_sid, auth_token)
client.messages.create(
  to="Your own phone",
  from_="Twilio phone",
  body="Tomorrow's forecast in Financial District, San Francisco is Clear.",
  #media_url=""
  )