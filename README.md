# Sample Twilio Python App

A sample messaging app built with the [Twilio Python SDK](https://github.com/twilio/twilio-python) to send and respond to SMS messages.

## Prerequisites

- Python 3.10
- virtualenv
    - `pip3 install virtualenv`
- ngrok http tunnel proxy
    - https://ngrok.com/download
- A Twilio account and phone number
    - https://console.twilio.com/
- Twilio CLI
    - https://www.twilio.com/docs/twilio-cli/getting-started/install
- Your Twilio Account SID, Authentication Token, and phone number saved in the following environment variables
    - TWILIO_ACCOUNT_SID
    - TWILIO_AUTH_TOKEN
    - TWILIO_PHONE_NUMBER

## Install

Create a virtual environment. We named ours `venv`

```
virtualenv venv
```

Activate your virtual environment.

```
source venv/bin/activate
```

Install project dependencies/requirements

```
pip3 install -r requirements.txt
```

When your done installing and running your application, deactivate your virtual environment.

```
deactivate
```

## Run the server (locally)

In a separate terminal, run `ngrok http 8080`.

Save the **Forwarding** URL. This is the URL that external HTTP traffic is proxied to your locally running web application.

With the ngrok Forwarding URL and Twilio phone number in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, run the following Twilio CLI command to update your Twilio phone number's webhook URL. This is the URL that traffic to your phone number will be forwarded to.

```
twilio phone-numbers:update <phone_number> \
--sms-url=<forwarding_url>/sms \
--sms-method=POST
```

Finally, start your application.

```
flask run --port 8080
```

## Interacting with the application

Send an SMS text message to your twilio number to receive a static reply message back.

Text "register" to your twilio number to receive a triggered message back later.

Trigger SMS messages to be sent to all registered numbers with:

```
curl -X POST http://localhost:8080/send-message
```
