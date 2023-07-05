import os
import africastalking
from dotenv import load_dotenv

load_dotenv()


def SendSms(message, phone):
    # Initialize SDK
    username = "Patazone"
    api_key = os.environ.get('AFRICASTALKING_API_KEY')
    africastalking.initialize(username, api_key)

    mobile = phone[-9:]
    sender = "Patazone"

    # Initialize a service e.g. SMS
    sms = africastalking.SMS

    try:
        # Thats it, hit send and we'll take care of the rest.

        response = sms.send(message, ["+254" + mobile])
        print(response)
    except Exception as e:
        print('Encountered an error while sending: %s' % str(e))
