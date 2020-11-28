import os
import csv
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage


def read_target_email_address(nama_file):
    try:
        with open("C:\\Users\\Maharani\\Documents\\Assignment Basic Python\\Final Project\\receiver_list.txt", 'r') as file:
            contents = file.readlines()
        return [item.strip() for item in contents]    
    except Exception:
        raise


def send_email_test_with_attachment(list_data_penerima, your_email_password):
    
    fromaddr = 'leda.deluhi95@gmail.com'
    nama_file_pdf = 'UTILITAS AIR.pdf'
    nama_file_image = 'ef.jpg'
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = ','.join(list_data_penerima)
    msg['Subject'] = 'Python Final Project'
    
    body = f'Hallo,\nThis is a simple mail. The mail is sent using Python SMTP library.\nYou can change this message for your purpose.\nThank You'
        
    msg.attach(MIMEText(body, 'plain'))

    # attach pdf
    lampiran1 = MIMEApplication(open("C:\\Users\\Maharani\\Documents\\Assignment Basic Python\\Final Project\\UTILITAS AIR.pdf", 'rb').read())
    lampiran1.add_header('Content-Disposition', 'attachment', filename=nama_file_pdf)
    msg.attach(lampiran1)
    
    # attach image
    fp = open("C:\\Users\\Maharani\\Documents\\Assignment Basic Python\\Final Project\\ef.jpg", 'rb')
    lampiran2 = MIMEImage(fp.read())
    lampiran2.add_header('Content-Disposition', 'attachment', filename=nama_file_image)
    fp.close()
    msg.attach(lampiran2)

    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.set_debuglevel(1)
    server.login(fromaddr, your_email_password)
    # server.sendmail(fromaddr, list_data_penerima, msg.as_string())
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    os.system('cls')
    your_email_password = getpass.getpass('email password ? ')
    try:
        # list_data_penerima = read_file_content('receiver_list.txt')
        # print(list_data_penerima)
        list_data_penerima = read_target_email_address('receiver_list.txt')
        for item in list_data_penerima:
            print(item)
        send_email_test_with_attachment(list_data_penerima, your_email_password)
        print('done.')
    except Exception as e:
        print(f'Something Wrong Has Happen:\n{e}')
    
