import smtplib
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
print('Mailing system')
print('Login:-')
email=input('Enter email...')
password=input('Enter password...')
if(server.login(email,password)):
    to=input('Enter the receiver email...')
    msg=input('Enter msg...')
    server.sendmail(email,to,msg)
    print('Mail sent')
else:
    print('Wrong email or password')

