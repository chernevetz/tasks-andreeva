#Условие: https://informatics.msk.ru/mod/statements/view.php?id=1135&chapterid=1481#1

ruble, coin = map(int, input('Введите цену товара(... рублей ... копеек): ').split())
amount = int(input('Введите количество товара: '))

result_ruble = (ruble * amount) + (coin * amount) // 100
result_coin = (coin * amount) % 100

print(f'Потрачено:{result_ruble} руб {result_coin} коп')
