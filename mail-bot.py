import smtplib  

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('Benutzername', 'Passwort')
server.sendmail('Sender','Empfänger', 'Email-text' )