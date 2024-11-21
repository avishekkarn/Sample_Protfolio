from flask import Flask, render_template, request, send_from_directory
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Path to your project files
BASE_DIR = r"A:\programs_code\WEBPAGES\engineer"

# Your email credentials
EMAIL_ADDRESS = "ghostyou9911@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "ghostyou7654"          # Replace with your app password or email password

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for static files (CSS, JS, Images)
@app.route('/<path:filename>')
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)

# Route for handling contact form submissions
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Send the form data to your email
    success = send_email(name, email, message)

    if success:
        return render_template('success.html', name=name)
    else:
        return "There was an issue sending your message. Please try again later."

# Function to send an email
def send_email(name, email, message):
    try:
        # Set up the email
        msg = EmailMessage()
        msg['Subject'] = "New Contact Form Submission"
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_ADDRESS
        msg.set_content(
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Message:\n{message}"
        )

        # Send the email using SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        return True  # Success

    except Exception as e:
        print(f"Error sending email: {e}")
        return False  # Failure

if __name__ == '__main__':
    app.run(debug=True)
