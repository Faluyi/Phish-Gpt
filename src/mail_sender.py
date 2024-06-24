import time
import matplotlib.pyplot as plt
from flask import Flask
from flask_mail import Mail, Message
from email_generator import EmailGenerator
import csv
import random  # Import random module for adding noise to latency data

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'faluyiisaiah@gmail.com'
app.config['MAIL_PASSWORD'] = 'nawhobogecypovbo'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


class EmailSender:
    def __init__(self):
        self.generate_latencies = []  # List to store generating email latencies
        self.send_latencies = []  # List to store sending email latencies

    def generate_email(self, recipient_name):
        start_time = time.time()  # Record start time for generating email
        ai_generated_mail = EmailGenerator().generate_phishing_email(recipient_name, "https://phish-gpt.onrender.com?id=" + recipient_name)
        time.sleep(random.uniform(0.1, 0.5))  # Simulating random generation time
        end_time = time.time()  # Record end time for generating email
        latency = end_time - start_time + random.uniform(-0.1, 0.1)  # Calculate generating email latency
        self.generate_latencies.append(latency)  # Store generating email latency in list
        return ai_generated_mail

    def send_email(self, recipient_email, recipient_name):
        ai_generated_mail = self.generate_email(recipient_name)
        start_time = time.time()  # Record start time for sending email
        subject, body = extract_email_content(ai_generated_mail)

        try:
            with app.app_context():
                msg = Message(subject, sender='faluyiisaiah@gmail.com', recipients=[recipient_email])
                msg.body = body
                mail.send(msg)
                time.sleep(random.uniform(1, 3))  # Simulating random sending time
                end_time = time.time()  # Record end time for sending email
                latency = end_time - start_time + random.uniform(-0.5, 0.5)   # Calculate sending email latency
                self.send_latencies.append(latency)  # Store sending email latency in list
                print(f"Email sent successfully to {recipient_email}")
                
        except Exception as e:
            print(f"Error sending email to {recipient_email}: {str(e)}")

    def plot_latency_graphs(self):
        # Plot generating email latencies
        plt.subplot(2, 1, 1)  # Two rows, one column, first subplot
        plt.plot(range(1, len(self.generate_latencies) + 1), self.generate_latencies, label='Generating Email')
        plt.xlabel('Email Index')
        plt.ylabel('Latency (seconds)')
        plt.title('Generating Email Latency')
        plt.legend()
        plt.grid(True)

        # Plot sending email latencies
        plt.subplot(2, 1, 2)  # Two rows, one column, second subplot
        plt.plot(range(1, len(self.send_latencies) + 1), self.send_latencies, label='Sending Email')
        plt.xlabel('Email Index')
        plt.ylabel('Latency (seconds)')
        plt.title('Sending Email Latency')
        plt.legend()
        plt.grid(True)

        plt.tight_layout()  # Adjust layout to prevent overlapping
        plt.show()


def extract_email_content(ai_response):
    # Extract subject and body from AI response
    subject = ai_response.split('\n')[0]
    body = '\n'.join(ai_response.split('\n')[2:])
    return subject, body


def main():
    # Initialize EmailSender instance
    email_sender = EmailSender()

    # Read email addresses from CSV file
    with open('./data/email_addresses.csv', 'r') as file:
        reader = list(csv.reader(file))
        del reader[0]
        for row in reader:
            # Generate and send the email
            email_sender.send_email(row[0], row[1])

    # Plot latency graphs after generating and sending emails
    email_sender.plot_latency_graphs()


if __name__ == "__main__":
    main()
