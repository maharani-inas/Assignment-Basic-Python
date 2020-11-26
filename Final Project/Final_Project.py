import os
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


#The mail addresses and  password
sender_address ='leda.deluhi95@gmail.com'                  
sender_pass =getpass.getpass('email password ? ')                                      

# list of reciver email_id to the mail 
f=open("C:\\Users\\Maharani\\Documents\\Assignment Basic Python\\Final Project\\receiver_list.txt",'r')
li = f.readlines()                                                         
#[item for item in input("Enter Receiver Mail Address :- ").split()] this is used to take user input of receiver mail id


# getting length of list 
length = len(li) 
   
# Iterating the index 
# same as 'for i in range(len(list))' 

# Here we iterate the loop and send msg one by one to the reciver
os.system('cls')
for i in range(length): 
    X = li[i]
    reciver_mail = X
    
    print(reciver_mail)
    
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] =  reciver_mail             
    message['Subject'] =  'Basic Python Final Project'      
     

    mail_content = '''Hallo,
    This is a simple mail. The mail is sent using Python SMTP library.
    You can change this message for your purpose.
    Thank You'''

    
    message.attach(MIMEText(mail_content, 'plain'))
    
    filename = "UTILITAS AIR.pdf"                                                 
    with open("C:\\Users\\Maharani\\Documents\\Assignment Basic Python\\Final Project\\UTILITAS AIR.pdf", "rb") as attachment:
        # MIME attachment is a binary file for that content type "application/octet-stream" is used
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    # encode into base64 
    encoders.encode_base64(part) 
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    # attach the instance 'part' to instance 'message' 
    message.attach(part) 

    filename1="ef.jpg"
    with open("C:\\Users\\Maharani\\Documents\\Assignment Basic Python\\Final Project\\ef.jpg", "rb") as attachment1:
        part1 = MIMEImage(attachment1.read())
    part1.add_header('Content-Disposition', "attachment1; filename= %s" % filename1)
    attachment1.close()
    message.attach(part1) 

    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.starttls() 
    s.login(sender_address, sender_pass) 
    text = message.as_string()
    s.sendmail(sender_address, reciver_mail, text) 
    s.quit() 

    print('Mail Sent')

#source : https://www.fireblazeaischool.in/blogs/sending-multiple-emails-using-python/