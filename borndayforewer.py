# МОДУЛЬ 2


def year_day(message, right_answer):
    answer = input(message)
    while answer != right_answer:
        print("Не верно")
        answer = input(message)
        return answer


year_day('Ввведите год рождения А.С.Пушкина:', '1799')
year_day('В какой день июня родился Пушкин?', '6')
print('Верно')
