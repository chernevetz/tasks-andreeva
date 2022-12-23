#Условие: https://informatics.msk.ru/mod/statements/view.php?id=1135&chapterid=1482#1

price = float(input('Введите цену товара в виде вещественного числа: '))

ruble = price // 1
coin = round(price % ruble * 100, 2)

print(int(ruble), int(coin))