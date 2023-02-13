import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import PASSWORD

def send_email(addr_to, msg_subj, msg_text):
    addr_from = "nikmarooo@mail.ru"                         # Отправитель
    password = PASSWORD                                  # Пароль
    msg = MIMEMultipart()                                   # Создаем сообщение
    msg['From'] = addr_from                              # Адресат
    msg['To'] = addr_to                                # Получатель
    msg['Subject'] = msg_subj                               # Тема сообщения
    body = msg_text                                         # Текст сообщения
    msg.attach(MIMEText(body, 'plain'))                     # Добавляем в сообщение текст
    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)        # Создаем объект SMTP
    #server.starttls()                                      # Начинаем шифрованный обмен по TLS
    server.login(addr_from, password)                       # Получаем доступ
    server.send_message(msg)                                # Отправляем сообщение
    server.quit()                                           # Выходим


addr_to = 'antonsuhodolski@mail.ru'
send_email(addr_to, "ДЗ 20-го занятия", "Текст сообщения")