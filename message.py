import smtplib
from email.message import EmailMessage
import os

# Configuração do email
email_de = '[email]'
email_para = 'luiscmmodesto@gmail.com'
assunto = 'Assunto do Email'
corpo = 'Este é o corpo do email.'

# Criar a mensagem
msg = EmailMessage()
msg['From'] = email_de
msg['To'] = email_para
msg['Subject'] = assunto
msg.set_content(corpo)

# Configuração do servidor SMTP
smtp_server = 'smtp.infomaniak.com'
porta = 587
senha = '[password]'

# Enviar o email
try:
    with smtplib.SMTP(smtp_server, porta) as server:
        server.starttls()  # Inicia a comunicação criptografada
        server.login(email_de, senha)
        server.send_message(msg)
    print('Email enviado com sucesso!')
except Exception as e:
    print(f'Ocorreu um erro ao enviar o email: {e}')
