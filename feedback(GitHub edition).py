import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

os.system("color a")
os.system("cls")

def send_mail():
    # Логин
    login = " "
    # Пароль
    password = " "
    # Сервер
    url = "smtp.yandex.ru"
    # Кому
    toaddr = " "

    msg = MIMEMultipart()
    # Тема
    print("Внимание!\nДля использования данной функции требуется подключение к Интернету!\n")
    theme = input("Введите тему письма:\n")
    msg['Subject'] = '-=Feedback from MShell=-    ' + theme
    # От кого
    msg['From'] = login
    # Текст письма
    body = input("Введите текст письма:\n")
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP_SSL(url, 465)
    except TimeoutError:
        print('No connect')
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())

    print("\n# Письмо отправлено! Спасибо за отзывчивость! #")
    input("\nНажмите <Enter> чтобы закрыть форму обратной связи")


def main():
    send_mail()

if __name__ == "__main__":
    main()