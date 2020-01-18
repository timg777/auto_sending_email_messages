import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import os

os.system('clear')

from_ = input('Text your email addr: ')
pswd = input('Enter your password: ')
to_ = input('Text receiver email addr: ')
subj_ = input('Enter subject: ')

msg = MIMEMultipart()

mess_res = input('Would you like to add message? [Y/n] ')

if mess_res.lower() == 'y':
    mess = input('Text your message here (if you want to add endlines, just text backslash + n) --> ')
else:
    mess = ''

message = mess
password = pswd
msg['From'] = from_
msg['To'] = to_
msg['Subject'] = subj_

server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()

server.login(msg['From'], password)

file_res = input('Would you like to add some files? [Y/n]')

if file_res.lower() == 'y':
    count_files = int(input('How much files do you want to add? '))
    files_paths = [input('Enter file path: ') for iter in range(count_files)]

    for path in files_paths:
        msg.attach(MIMEText(message, 'plain'))
        file = MIMEApplication(open(path, 'rb').read())
        file.add_header('Content-Depisotion', 'attachment', filename=path)
        msg.attach(file)

pic_res = input('Would you like to add some pictures? [Y/n] ')

if pic_res == 'y':
    count_pic = int(input('How much pictures do you want to add? '))
    pics_paths = [input('Enter pic path: ') for iter in range(count_pic)]

    for path in pics_paths:
        img = MIMEImage(open(path, 'rb').read(), _subtype="jpg")
        img.add_header('Content-Disposition', 'attachment', filename='')
        msg.attach(img)

count_messages = int(input('How much messages would you like to send? '))

for item in range(count_messages):
    server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email(-s) to " + msg['To'])
