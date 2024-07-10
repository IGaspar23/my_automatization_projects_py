# enviar emails en el servidor de gmail
import smtplib
from email.message import EmailMessage
import imghdr

# statc variables
my_email = "irvinggaspar55@gmail.com"
my_password = "wkig omcx dqcq ikox"
sev_emails=["igaspar.physics@gmail.com","gasparito19@gmail.com"]

#We define connection with the server
"""with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    # Gmail login
    smtp.login(my_email, my_password)
    
    # Issue
    issue= "Email automatization test"
    headers = f"From: {my_email}\r\nTo: {my_email}\r\nSubject: {issue}\r\n"
    messagge = f"{headers}\r\nFist email sent by using python."
    
    # Send
    smtp.sendmail(my_email, my_email, messagge)
"""
# Email structure using email.message library    
msg = EmailMessage()
msg["Subject"] = "Another test for sending emails from python"
msg["From"] = my_email
msg["To"] = sev_emails
msg["Cc"] = sev_emails
msg.set_content("Primer correo usando otro método")

# Load and read the file to attach
"""
with open("C:/Users/irvin/OneDrive/Desktop/Python_Projects/SendEmail/img_python_comments.png", "rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = "Image1" + file_type
    
    # Method to attach the file we opened before
    msg.add_attachment(file_data, maintype = "image", subtype = file_type, filename = file_name)
"""
# To send .xlsx we use 
"""
with open("path for your excel file", "rb") as f:
    file_data = f.read()
    file_type = "vnd.openxmlformat-officedocument.spreadsheetml.sheet"
    file_name = "Archivo de excel"
    
    msg.add_attachment(file_data, maintype = "application", subtype = file_type, filename = file_name)
"""

# Para enviar un archivo con HTML
msg.add_alternative("""
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;"> This is an example using HTML  </h1>
    </body>
</html>                    
""", subtype= "html")


# We connect to the server and send the message
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp2:
    smtp2.login(my_email, my_password)
    smtp2.send_message(msg)