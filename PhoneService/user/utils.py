import os
from twilio.rest import Client
import random

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

def generateOTP():
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    OTP = ''
    for i in range(5):
        rand_idx = random.randrange(len(test_list))
        OTP += str(rand_idx)
    return OTP


def send_otp_code(phone_number):
    client = Client(account_sid, auth_token)

    message = client.messages.create(body='Hello there from Twilio SMS API', from_='', to=phone_number)
