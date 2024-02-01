# Enviando E-mails SMTP com Python
import os
import pathlib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
import smtplib
from dotenv import load_dotenv  # type: ignore

load_dotenv()

# Caminho arquivo HTML
FILE_PATH = pathlib.Path(__file__).parent / 'Aula185.html'


# Dados do remetente e destinatário
remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente


# Configurações do SMTP
smtp_server = os.getenv('SMTP_SERVER', '')
smtp_port = os.getenv('SMTP_PORT', '')
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')


# Mensagem de texto
with open(FILE_PATH, 'r', encoding='utf-8') as file:
    mensagem = file.read()
    template = Template(mensagem)
    texto_email = template.substitute(nome='João')


# Transformar nossa mensagem em MIMEMultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Teste de envio de e-mail com Python'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)


# Envia o e-mail
with smtplib.SMTP(smtp_server, smtp_port) as server:  # type: ignore
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')
