from datetime import datetime, timedelta

#  1 тут еще можно было добавить проверку на коректноть введения дати и дня недели но надеюсь на правильного пользователя
#
# day_of = input("Введите день недели ").lower()
#
# if day_of not in ["субота", "воскресенье"]:
#     print(" Не проспи сегодня на роботу")
# else:
#     print("Можеш поспать по дольше сегодня выходной")
# vacation = input("Введите дату отпуска(в формате ДД-ММ-ГГГГ): ")
# length = int(input("сколько длится ваш отпуск"))
#
# new_date = datetime.strptime(vacation, '%d-%m-%Y')
# length_vacation = new_date + timedelta(days=length)
#
# if datetime.now() < new_date:
#     print("Отпуск впереди не отчаивайся")
# elif datetime.now() <= length_vacation:
#     print("Ура отруск")
# else:
#     print("Отпуск прошел но в переди новый")

# 2 задание
#
# number = 21
# input_number = int(input("Введите число"))
# if input_number < number:
#     print(f"{input_number}->{number - input_number}")
# else:
#     print(f"{input_number}->{(input_number - number) * 2}")
# 3 задание
# number_one = int(input("Введите первое число"))
# number_two = int(input("Введите второе число"))
# sum_number = abs(number_one - number_two)
#
# if sum_number <= 100:
#     print(f"{number_one} {number_two}->хорошо")
# else:
#     print(f"{number_one} {number_two}->плохо")
# 4 задание
#
# test = "Test this message"
# numbers = int(input("Введите номер символа который нужно убрать в предложении 'Test this message'"))
# if 0 <= numbers < len(test):
#     update_test = test[:numbers] + test[numbers + 1:]
#     print(update_test)
# else:
#     print("Введите правильный номер символа")
# 5 задание
# one = int(input("Если первый выключатель включен введите 1 если выключен введите 0 "))
# two = int(input("Если второй выключатель включен введите 1 если выключен введите 0 "))
#
# if one == 1 and two == 1:
#     print("Хорошо")
# elif one == 0 and two == 0:
#     print("Хоршо")
# else:
#     print("Плохо ")
# 6 задание

# word = input("Введите слово")
# update = word[-1:] + word[:-1]
# print(update)
# 7 задание

# one_number = int(input("Введите первое число"))
# two_number = int(input("Введите второе число"))
#
# if one_number == two_number:
#     print(f"{one_number} {two_number} _> {(one_number + two_number) ** 2}")
# else:
#     print(f"{one_number} {two_number} _> {one_number + two_number}")

# 8 задание

# second = int(input("Введите количество секунд"))
# dey = second // 86400
# hour = second % 86400 // 3600
# minutes = second % 3600 // 60
# change_second = second % 60
# print(f"{dey}:{hour:02}:{minutes:02}:{change_second:02} ")
