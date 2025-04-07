import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

# Get credentials from GitHub Secrets
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

# Sample HTML report
""" html_content =
<html>
<head>
    <style>
        table { width: 100%; border-collapse: collapse; font-family: Arial, sans-serif; }
        th, td { border: 1px solid black; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h2>Daily Monitoring Report</h2>
    <table>
        <tr><th>Metric</th><th>Value</th></tr>
        <tr><td>Total Nodes</td><td>50</td></tr>
        <tr><td>Live Nodes</td><td>48</td></tr>
        <tr><td>Service Unhealthy</td><td>2</td></tr>
    </table>
</body>
</html>"""
Your account No. XXXXXXXX2081 has been credited with RS.220000.00 on 07-04-25

# Function to send email
def send_email():
    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    msg["Subject"] = "HDFC BANK"

    msg.attach(MIMEText(html_content, "html"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    server.quit()
    print("✅ Email sent successfully!")

send_email()
