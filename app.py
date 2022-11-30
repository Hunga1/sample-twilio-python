import os
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_number = os.environ['TWILIO_PHONE_NUMBER']
client = Client(account_sid, auth_token)

app = Flask(__name__)
registered = set()

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    fromNumber = request.form["From"]
    body = request.form["Body"]
    resp = MessagingResponse()
    if (body.lower() == "register"):
        """Save the number for later"""
        registered.add(fromNumber)
        resp.message("You've been registered.")
    else:
        """Respond to incoming calls with a simple text message."""
        resp.message("The Robots are coming! Head for the hills!")
    return str(resp)

@app.route("/send-message", methods=['POST'])
def send_message():
    for number in registered:
        """Send messages to each registered number"""
        message = client.messages \
            .create(
                body="Test hello from my Python app",
                from_=twilio_number,
                to=number
            )
    return ""

if __name__ == "__main__":
    app.run()
