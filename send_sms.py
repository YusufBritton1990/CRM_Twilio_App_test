# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_AUTH_KEY']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="It's your boy, Yusuf",
                     from_='+16467982287',
                     to='+16464634065'
                 )

print(message.sid) #This sends the message
