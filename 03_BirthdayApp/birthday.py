import datetime

def print_header():
    print('--------------------------')
    print('------bobRzDay App--------')
    print('--------------------------')
    print()

def get_birthday_from_user():
    print('Введите дату выпуска кожаного мешка')
    year = int(input('Год [ГГГГ]: '))
    month = int(input('Месяц [ММ]: '))
    day = int(input('День [ДД]: '))

    birthday = datetime.datetime(year, month, day)
    print('Ваш ДР был: ' + str(birthday))
    return birthday

def compute_days_between_dates(original_date, now):
    date1 = now
    date2 = datetime.datetime(now.year,original_date.month, original_date.day)
    dt = date1 - date2
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days

def print_birthday_information(days):
    if days < 0:
     print('Ваш ДР через {} дней!'.format(-days))
    elif days > 0:
        print('В этом году у вас уже был ДР! {} дней назад. Угомонись старый мешок'.format(days))
    else:
        print('С Днюхой, УАССЯЯ!!!')

def main():
    print_header()
    bday = get_birthday_from_user()
    now = datetime.datetime.now()
    number_of_days = compute_days_between_dates(bday, now)
    print_birthday_information(number_of_days)

main()