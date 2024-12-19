import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def send_email(email,file):
    my_email =  # Your email address here
    password =   # Your app password here

    file_path = file
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
            }
            .container {
                width: 80%;
                margin: auto;
                padding: 20px;
                background-color: white;
                border: 1px solid #ddd;
                border-radius: 10px;
            }
            h1 {
                color: #007bff;
            }
            p {
                font-size: 16px;
                color: #333;
            }
            .footer {
                margin-top: 20px;
                font-size: 12px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Lena Bank!</h1>
            <p>Hello,This is your Recent Tranasctions.</p>
            
            <div class="footer">
                <p>You're receiving this email because you signed up on our website.</p>
                <p>&copy; 2024 Our Company, All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """

    message=MIMEMultipart('alternative')
    message["Subject"] = "Bank statement"
    message["From"] = my_email
    message["To"] = email

    html_part = MIMEText(html_content, "html")
    # Attach the PDF file
    attachment = open(file_path, 'rb')  # Open the file in binary mode

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)

    # Add the PDF file as an attachment
    part.add_header('Content-Disposition', f'attachment; filename={file_path.split("/")[-1]}')
    message.attach(part)

    # Close the attachment file
    attachment.close()
    message.attach(html_part)

    try:
        # Set up the SMTP connection
        connection = smtplib.SMTP('smtp.gmail.com', 587)
        connection.starttls()
        
        # Attempt login
        connection.login(my_email, password)
        
        # Send email
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=message.as_string())
        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError as e:
        print("Authentication error:", e)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        connection.quit()
