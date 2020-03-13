from string import Template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content =template_file.read()
    return Template(template_file_content)

def send_mail(email,email_to,email_sub,password,name, rule,campaign,schedule,condition,action):
    # host = ['smtp.gmail.com','smtp-mail.outlook.com','smtp.mail.yahoo.com']
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(email, password=password)

    message_template = read_template('/home/happyshappy/PycharmProjects/tyroo_rbe/message.txt')

    msg = MIMEMultipart()
    message = message_template.substitute(PERSON_NAME = name,RULE_NAME =rule,CAMPAIGN = campaign,SCHEDULE= schedule,CONDITION = condition,ACTION= action )
    msg['From'] = email
    msg['To'] = email_to
    msg['Subject'] = email_sub
    msg.attach(MIMEText(message,'plain'))
    s.send_message(msg)
    del msg
print("done !")