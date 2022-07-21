# import requests
#
# b = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
# pb = 'https://api.privatbank.ua/p24api/exchange_rates?json&date=02.06.2022'
# response = requests.get(b)
# space = " "
# currencies = ['UAH']
# currency_text = f'Все валюты:\n1 - Українська гривня {space} (UAH)\n'
#
# for key, wallet in enumerate(response.json(), 2):
#     currencies.append(wallet['cc'])
#     currency_text += f"{key} - {wallet['txt']} ({wallet['cc']})\n"
# print(currency_text)
#
# while True:
#     try:
#         hand_over_num = int(input('Какую валюту надо сдать: ')) - 1
#         get_num = int(input('Какую валюту нужно получить: ')) - 1
#         if hand_over_num < 0 or get_num < 0:
#             raise IndexError
#         if hand_over_num == get_num:
#             print('Валюты одинаковы!!! Такого не может быть, выберете другую валюту')
#             continue
#
#         hand_over = currencies[hand_over_num]
#         get = currencies[get_num]
#         break
#     except (ValueError, IndexError):
#         print('Введите правильную валюту!!!')
#
# while True:
#     try:
#         amount = int(input('Какую сумму хотите получить: '))
#         if amount < 0:
#             raise ValueError
#         break
#     except ValueError:
#         print('Введите правильную валюту!!!')
#
# response = requests.get(pb)
# available_currencies = {'UAH': [1.0, 1.0]}
# for r in response.json()['exchangeRate']:
#     if 'saleRate' and 'purchaseRate' in r:
#         available_currencies[r['currency']] = [r['saleRate'], r['purchaseRate']]
#
# try:
#     amount *= available_currencies[get][0] / available_currencies[hand_over][1]
#     print(f'Вам необходимо сдать: {round(amount, 2)} {hand_over}')
# except KeyError:
#     print('Сейчас невозможно работать с этой валютой!!!')


# books = [
#     'Физика',
#     'Химия',
#     'Алгебра',
#     'Геометрия',
#     'Литература',
#     'Биология',
#     'Зоология',
#     'История',
#     'Право',
#     'Информатика',
#     'Рисование',
# ]
#
# schedule = {
#     'monday': (
#         'Физика',
#         'Зоология',
#         'История',
#         'Право',
#         'Рисование',
#     ),
#     'tuesday': (
#         'Физика',
#         'Химия',
#         'Алгебра',
#         'Геометрия',
#     ),
#     'wednesday': (
#         'История',
#         'Право',
#         'Информатика',
#         'Рисование',
#         'Зоология',
#         'Геометрия',
#     ),
#     'thursday': (
#         'Геометрия',
#         'Литература',
#         'Биология',
#         'Зоология',
#     ),
#     'friday': (
#         'Право',
#         'Физика',
#         'Зоология',
#         'Литература',
#         'Информатика',
#     ),
# }
#
#
# def collect_the_bag():
#     schedule_tuple = tuple(schedule.keys())
#     current_books = []
#     books_string = "Введите номер книги\n"
#     for key, value in enumerate(books):
#         books_string += f"{key + 1} - {value}\n"
#
#     while True:
#         try:
#             day = int(input('1 - Понедельник\n2 - Вторник\n3 - Среда\n4 - Четверг\n5 - Пятница\nВыберете день: '))
#             current_schedule = schedule_tuple[schedule_tuple[day - 1]]
#         except IndexError:
#             print('Введите нормальный день недели')
#             continue
#         except ValueError:
#             print('День недели должен быть числом')
#             continue
#
#         while len(current_books) < len(current_schedule):
#             try:
#                 book = int(input(books_string))
#                 current_book = books[book - 1]
#             except IndexError:
#                 print('Введите правильный номер книги')
#                 continue
#             except ValueError:
#                 print('Введите НОМЕР книги')
#                 continue
#
#             if current_book in current_schedule:
#                 if current_book in current_books:
#                     print(f"{current_book} уже в рюкзаке. Олух ты, Санёк! Давай еще раз)")
#                 else:
#                     current_books.append(current_book)
#                     print("Хорошо Саня, угадал. Все таки задатки ума присутствуют")
#             else:
#                 print("Олух ты, Санёк! Давай еще раз)")
#         print(f"Удачи тебе, Санёк. Вот твои книги {current_books}")
#         break
#
#
# collect_the_bag()

# lowercase_letters = list("abcdefghijklmnopqrstuvwxyz")
# uppercase_letters = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# digits = tuple("0123456789")
# symbols = tuple("*-#")
# errors = {
#     'short': "Пароль должен быть не короче 8 символов",
#     'long': "Пароль должен быть не длинее 12 символов",
#     'uppercase': "В пароле должны быть буквы вверхнего регистра",
#     'lowercase': "В пароле должны быть буквы нижнего регистра",
#     'digits': f"В пароле должны быть цифры {digits}",
#     'symbols': f"В пароле должны быть символы {symbols}"
# }
#
# for a, b in errors.items():
#     print(b)
#
#
# password = input('Введите пароль: ')
#
#
# if 8 <= len(password) <= 12:
#     errors.pop('short')
#     errors.pop('long')
# elif len(password) > 12:
#     errors.pop('short')
# elif len(password) < 8:
#     errors.pop('long')
#
#
# for let in password:
#     if let in lowercase_letters:
#         errors.pop('lowercase', None)
#     if let in uppercase_letters:
#         errors.pop('uppercase', None)
#     if let in digits:
#         errors.pop('digits', None)
#     if let in symbols:
#         errors.pop('symbols', None)
#
#
# if errors:
#     for a, b in errors.items():
#         print(f"!ERROR! {b} !ERROR!")
# else:
#     print('Пароль идеален ( ･_･)♡')

def memoize_func(func):
    from datetime import datetime

    def wrapper(a, b):
        start_time = datetime.now()
        func(a, b)
        end_time = datetime.now()
        print(f"[*] Время выполнения: {end_time - start_time} секунд.")

    return wrapper


def lines(func):
    def inner(*args):
        func(*args)
        print('-' * 60)

    return inner


zero = 0


@lines
@memoize_func
def numbers_sum(a, b):
    for number in list(range(a, b)):
        number += zero
    print(f"Аргументы: {a, b}\n{number}")
    return zero


numbers_sum(3, 1000005)
numbers_sum(3, 1000005)
numbers_sum(3, 1000004)
numbers_sum(3, 1000002)
numbers_sum(3, 1000005)
numbers_sum(3, 1000003)
numbers_sum(3, 1000004)
numbers_sum(3, 1000005)
numbers_sum(3, 1000007)
numbers_sum(3, 1000008)
numbers_sum(3, 1000007)
