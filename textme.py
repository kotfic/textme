from twilio.rest import TwilioRestClient
import os
import argparse


def text_factory(sid, token):
    client = TwilioRestClient(sid, token)

    def _textme(message):
        try:
            TO_NUM = os.environ['MY_PHONE_NUMBER']
            FROM_NUM = os.environ['TWILIO_PHONE_NUMBER']
            return client.messages.create(to=TO_NUM,
                                          from_=FROM_NUM,
                                          body=message)
        except KeyError:
            raise Exception("Must define TWILIO_PHONE_NUMBER and "
                            "MY_PHONE_NUMBER environment variables!")

    return _textme


def get_text_function():
    try:
        ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
        AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

        texter = text_factory(ACCOUNT_SID, AUTH_TOKEN)
    except KeyError:
        # Could potentially read these from stdin instead
        raise Exception("Must define TWILIO_ACCOUNT_SID and "
                        "TWILIO_AUTH_TOKEN environment variables")
        texter = None

    return texter


def main():
    parser = argparse.ArgumentParser(description="To Write")
    parser.add_argument("message",
                        help="Message to send")

    args = parser.parse_args()

    texter = get_text_function()
    texter(args.message)


if __name__ == "__main__":
    main()
