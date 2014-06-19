# practice using the Twilio-Python library

from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC1129772057963f5acc9fa6c10d8602f3"
auth_token  = "c43707deeb3db61b336b0f9423891792"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Testing message from Curtis' Twilio account",
    to="+15555555555",    # personal phone number
    from_="+15555555555") # Twilio number
print message.sid