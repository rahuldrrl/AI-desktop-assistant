import socket

def enable_port_587():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific port
    server_socket.bind(('localhost', 587))  # You can replace 'localhost' with your actual IP address

    # Start listening for incoming connections
    server_socket.listen(1)

    print("Listening on port 587...")

    while True:
        # Accept incoming connection
        client_socket, address = server_socket.accept()

        # Handle the incoming data or connection here
        # For example, you can read the data sent by the client:
        data = client_socket.recv(1024)
        print("Received:", data.decode())

        # You can also send data back to the client if needed:
        # client_socket.sendall(b"Hello from server")

        # Close the client socket
        client_socket.close()

# Call the function to enable port 587
enable_port_587()

#
# import smtplib
# from email.message import EmailMessage
#
#
# def send_email(sender_email, sender_password, receiver_email, subject, message):
#     try:
#         # Create EmailMessage object
#         email = EmailMessage()
#         email['From'] = sender_email
#         email['To'] = receiver_email
#         email['Subject'] = subject
#         email.set_content(message)
#
#         # Connect to SMTP server
#         with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#             smtp.starttls()  # Start TLS encryption
#             smtp.login(sender_email, sender_password)
#             smtp.send_message(email)
#
#         print("Email sent successfully!")
#
#     except Exception as e:
#         print(f"An error occurred: {e}")
#
#
# # Example usage
# if __name__ == "__main__":
#     sender_email = 'bkashishh07@gmail.com'  # Enter your email address
#     sender_password = 'kozgadvdbmuutbgo'  # Enter your email password
#     receiver_email = 'bkashishh077@gmail.com' # Enter recipient's email address
#     subject = 'Test Email'
#     message = 'This is a test email sent from Python.'
#
#     send_email(sender_email, sender_password, receiver_email, subject, message)
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
    sender_password = 'kozgadvdbmuutbgo'  # Enter your email password
    receiver_email = 'bkashishh077@gmail.com' # Enter recipient's email address
    subject = 'Test Email'
    message = 'This is a test email sent from Python.'

    send_email(sender_email, sender_password, receiver_email, subject, message)
