#Условие: https://informatics.msk.ru/mod/statements/view.php?id=1135&chapterid=1483#1

hour_1, minute_1, second_1 = map(int, input('Введите первое время(...часы ...минуты ...секунды: )'). split())
hour_2, minute_2, second_2 = map(int, input('Введите второе время(...часы ...минуты ...секунды: )'). split())

result_second = (hour_2 - hour_1) * 3600 + (minute_2 - minute_1) * 60 + (second_2 - second_1)

print(f'Прошло {result_second} сек')