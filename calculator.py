first_str = 'skill'
second_str = 'box'

#конкатенация строк
some_string = first_str + second_str
print(some_string) #skillbox

#длина строки
length = len(some_string)
print(length) #8

#первый символ строки
first_symbol = some_string[0]
print(first_symbol) #s

#срез строки с первого по пятый символ
skill_slice = some_string[0:5]
print(skill_slice) #skill

#последний символ строки
last_symbol = some_string[-1]
print(last_symbol) #x

#последние три символа строки 'skillbox'
box_slice = some_string[-3:]
print(box_slice) #box

#поиск подстроки
#если подстрока найдена, метод вернёт позицию её первого элемента, если нет — вернёт -1
ill_substr = some_string.find('ill')
print(ill_substr)

#поиск подстроки с заменой, заменим skill на school
school_box = some_string.replace('skill', 'school')
print(school_box) #schoolbox

#разбить строку по разделителю
student_name = 'Ivan_Ivanovich_Petrov'
list_of_substr = student_name.split('_')
print(list_of_substr) #['Ivan', 'Ivanovich', 'Petrov']