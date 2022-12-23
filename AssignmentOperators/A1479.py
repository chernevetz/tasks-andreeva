#Условие задачи: https://informatics.msk.ru/mod/statements/view.php?id=1135&chapterid=1479#1

string = int(input('Введите количество строк на странице: '))
string_number = int(input('Введите номер строки в тексте: '))

result_page = string_number // string + 1
result_string = string_number - (result_page - 1) * string

print(f'Номер страницы:{result_page}')
print(f'Номер строки:{result_string}')