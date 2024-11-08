import imaplib
import email
import time

# Email server settings
EMAIL = 'your_email@example.com'
PASSWORD = 'your_password'
IMAP_SERVER = 'imap.gmail.com'  # Replace with your email provider's IMAP server

def check_inbox():
    # Connect to the server and go to the inbox
    mail = imaplib.IMAP4_SSL(IMAP_SERVER)
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")  # Select inbox folder

    # Search for all unread emails
    status, response = mail.search(None, 'UNSEEN')
    unread_msg_nums = response[0].split()
    
    # If there are any unread messages, print a message
    if unread_msg_nums:
        print(f"You have {len(unread_msg_nums)} new email(s)!")
    else:
        print("No new emails.")
    
    # Logout and close connection
    mail.logout()

# Run the script every minute
while True:
    check_inbox()
    time.sleep(60)
