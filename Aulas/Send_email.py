import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Teste<p>
    """
    
    msg = email.message.Message()
    msg['Subject'] = 'Teste'
    msg['From'] = '...@gmail.com'
    msg['To'] = '...@gmail.com'
    password = ''
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    s.quit()

enviar_email()