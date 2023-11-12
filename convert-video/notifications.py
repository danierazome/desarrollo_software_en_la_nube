import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(usuario, conversion):
    # Configurar el remitente y las credenciales
    rem_email = 'ssierraoxxonv@gmail.com'
    rem_pass = 'qceo xvdw bwyc jtut'

    # Configurar el destinatario y el mensaje
    rec_email = usuario.email
    subj = 'Archivo disponible para la descarga'
    txt_msg = f'Hola, el archivo que cargaste con nombre {conversion.video_name} se encuentra disponible para su descarga desde las {conversion.conversion_date}.'

    try:
        # Iniciar una conexión SMTP con el servidor de correo
        servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
        servidor_smtp.starttls()
        servidor_smtp.login(rem_email, rem_pass)

        # Crear el mensaje MIME
        msg = MIMEMultipart()
        msg["From"] = rem_email
        msg["To"] = rec_email
        msg["Subject"] = subj
        msg.attach(MIMEText(txt_msg, 'plain'))

        # Enviar el correo electrónico
        servidor_smtp.sendmail(rem_email, rec_email, msg.as_string())
        servidor_smtp.quit()
        print("Correo electrónico enviado correctamente")
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {str(e)}")
