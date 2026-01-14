import os
import base64
import time
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# --- API & Script Configuration ---
# Note: The SCOPES have changed to allow sending emails.
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]
API_SERVICE_NAME = "gmail"
API_VERSION = "v1"
CLIENT_SECRETS_FILE = "client_secrets.json"

# --- Spam Configuration ---
YOUR_EMAIL = "bowencactusyt@gmail.com"  # The email to send FROM and TO
EMAIL_SUBJECT = "fart"
EMAIL_BODY = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫"
NUMBER_OF_EMAILS = 2000  # How many emails to send
DELAY_BETWEEN_EMAILS = 0.01  # Seconds to wait between each email


def get_gmail_service():
    """Authenticates the user and returns an authorized Gmail API service object."""
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    # The user needs to authorize the app again for these new Gmail permissions
    credentials = flow.run_local_server(port=0)
    service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)
    return service


def send_spam_email(service, recipient, subject, body):
    """Creates and sends an email message."""
    try:
        message = EmailMessage()
        message.set_content(body)
        message["To"] = recipient
        message["From"] = recipient  # Sending from yourself, to yourself
        message["Subject"] = subject

        # Encode the message in base64url format
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}

        # pylint: disable=E1101
        send_message = (
            service.users().messages().send(userId="me", body=create_message).execute()
        )
        print(f'Sent message to {recipient}. Message ID: {send_message["id"]}')
    except HttpError as error:
        print(f"An error occurred: {error}")
        send_message = None
    return send_message


if __name__ == "__main__":
    print("Starting the Gmail 'Spam Yourself' script...")

    # You will need to re-authorize because the SCOPES (permissions) have changed.
    gmail_service = get_gmail_service()

    print(f"\nPreparing to send {NUMBER_OF_EMAILS} emails to {YOUR_EMAIL}...")

    for i in range(NUMBER_OF_EMAILS):
        print(f"Sending email {i + 1} of {NUMBER_OF_EMAILS}...")
        send_spam_email(gmail_service, YOUR_EMAIL, EMAIL_SUBJECT, EMAIL_BODY)
        # Wait for the specified delay before sending the next one
        time.sleep(DELAY_BETWEEN_EMAILS)

    print("\nScript finished. Check your inbox!")
