import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
import os
import dotenv

dotenv.load_dotenv()

def send_test_email(sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password):
    print("Connecting to SMTP server...")
    try:
        # Create SMTP session for sending the email with SSL
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(smtp_server, smtp_port, context=context)
        print("Connected to SMTP server.")

        print("Logging in with SMTP credentials...")
        server.login(smtp_username, smtp_password)  # Login with SMTP credentials
        print("Logged in successfully.")

        # Create a multipart message and set headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Test Email"

        # Add body to email
        body = "This is a test email to verify SMTP credentials."
        message.attach(MIMEText(body, "plain"))

        print("Sending test email...")
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)  # Send the email
        print("Test email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing SMTP connection...")
        server.quit()  # Terminate the SMTP session
        print("SMTP connection closed.")

# Replace these values with your SMTP credentials and email addresses
sender_email = os.getenv("EMAIL_FROM")
receiver_email = os.getenv("RECEIVER_EMAIL")
smtp_server = os.getenv("EMAIL_HOST")
smtp_port = os.getenv("EMAIL_PORT")
smtp_username = os.getenv("EMAIL_USER")
smtp_password = os.getenv("EMAIL_PASSWORD")

# Send a test email
send_test_email(sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password)
