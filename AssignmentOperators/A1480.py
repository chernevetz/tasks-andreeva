#Условие задачи: https://informatics.msk.ru/mod/statements/view.php?id=1135&chapterid=1480#1

day_in_month = int(input('Введите день месяца: '))
day_in_week = int(input('Введите день недели начала месяца: '))

res = day_in_month % 7
print(res)
res2 = day_in_month // 7
print(res2)
result_day = res + day_in_week - res2
print(result_day)
