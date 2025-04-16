import smtplib
from email.message import EmailMessage


def send_email(sender_email, sender_password, receiver_email, subject, message):
    try:
        # Create EmailMessage object
        email = EmailMessage()
        email['From'] = sender_email
        email['To'] = receiver_email
        email['Subject'] = subject
        email.set_content(message)

        # Connect to SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()  # Start TLS encryption
            smtp.login(sender_email, sender_password)
            smtp.send_message(email)

        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    sender_email = 'bkashishh07@gmail.com'  # Enter your email address
    sender_password = 'kmlamdibgonscago'  # Enter your email password
    receiver_email = 'sandeepatalagini@gmail.com' # Enter recipient's email address
    subject = 'Test Email'
    message = 'This is a test email sent from Python.'

    send_email(sender_email, sender_password, receiver_email, subject, message)
