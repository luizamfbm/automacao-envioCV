import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def enviar_email():
    
    corpo_email = """
    <p>Parágrafo 1</p>
    <p>Segue seu e-mail automático com um anexo.</p>
    """

    msg = MIMEMultipart()
    msg['From'] = '@email.com'
    msg['To'] = '@email.com'
    msg['Subject'] = "Assunto"
    password = ''  # Insira sua senha de aplicativo aqui 

    msg.attach(MIMEText(corpo_email, 'html'))

    filename = "arquivo.pdf"
    attachment = open(filename, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header('Content-Disposition', f'attachment; filename={filename}')

    msg.attach(part)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

    print('Email enviado')

enviar_email()
