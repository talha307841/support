from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load API keys from the environment variables
load_dotenv()

# Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

print(f"TWILIO_ACCOUNT_SID: {TWILIO_ACCOUNT_SID}")
print(f"TWILIO_AUTH_TOKEN: {TWILIO_AUTH_TOKEN}")
print(f"TWILIO_PHONE_NUMBER: {TWILIO_PHONE_NUMBER}")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def make_call(to_phone_number):
    """Make a call to the specified phone number."""
    call = client.calls.create(
        to=to_phone_number,
        from_=TWILIO_PHONE_NUMBER,
        url='https://twenty-snakes-write.loca.lt/twilio-webhook'  # Your public localtunnel URL
    )
    print(f"Call initiated: {call.sid}")

if __name__ == "__main__":
    # Replace with the phone number you want to call
    recipient_phone_number = input("Enter the phone number to call (in E.164 format): ")
    make_call(recipient_phone_number)
