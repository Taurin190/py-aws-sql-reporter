import boto3
from botocore.exceptions import ClientError
import config.mail as m


class SESSender:
    def __init__(self, config):
        self.config = config

    def send(self):
        CHARSET = "UTF-8"
        client = boto3.client('ses', region_name=self.config['aws_region'])

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        self.config['recipient'],
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': CHARSET,
                            'Data': m.BODY_HTML,
                        },
                        'Text': {
                            'Charset': CHARSET,
                            'Data': m.BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': self.config['subject'],
                    },
                },
                Source=self.config['sender'],
                # If you are not using a configuration set, comment or delete the
                # following line
                # ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response)
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
