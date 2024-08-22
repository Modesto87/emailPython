import smtplib
from email.message import EmailMessage
import os

# Configuration du email
email_de = '[email]'
email_para = 'luiscmmodesto@gmail.com'
assunto = 'sujet du email'
corpo = 'text du email'

# Creer une message
msg = EmailMessage()
msg['From'] = email_de
msg['To'] = email_para
msg['Subject'] = assunto
msg.set_content(corpo)

# serveur SMTP
smtp_server = 'smtp.infomaniak.com'
porta = 587
senha = '[password]'

# Envoyer
try:
    with smtplib.SMTP(smtp_server, porta) as server:
        server.starttls()
        server.login(email_de, senha)
        server.send_message(msg)
    print('Email envoyé')
except Exception as e:
    print(f'il y a un probleme pour envoyer: {e}')
