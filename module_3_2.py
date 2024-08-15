def checking_of_correction (recipient, sender):
    check_a = '@' in recipient and '@' in sender
    check_end = ('com' in recipient or 'ru' in recipient or 'net' in recipient) and ('com' in sender or 'ru' in sender or 'net' in sender)
    check = 0
    if check_a == check_end:
        check = True
    else:
        check = False
    return check_end

def send_email (message, recipient, *, sender = 'university.help@gmail.com'):
    check = checking_of_correction(recipient, sender)
    if check == False:
        print (f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    else:
        if recipient == sender:
            print (f'Нельзя отправить письмо самому себе!')
        elif recipient != sender and sender != 'university.help@gmail.com':
            print (f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print ('Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')



send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
