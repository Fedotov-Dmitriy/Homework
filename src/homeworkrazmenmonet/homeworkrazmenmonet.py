a = int(input("Введите Число\n"))
name_length = len(input("Введите ваше имя\n"))
surname_length = len(input("Введите вашу фамилию\n"))
otchestvo_length = len(input("Введите ваше отчество если оно есть\n"))
if otchestvo_length == 0:
    otchestvo_length = 19
name_count = 0
surname_count = 0
otchestvo_count = 0
buffer = a
while a >= min(name_length, surname_length, otchestvo_length):
    if a >= otchestvo_length:
        a = a - otchestvo_length
        otchestvo_count += 1
    if a >= surname_length:
        a = a - surname_length
        surname_count += 1
    if a >= name_length:
        a = a - name_length
        name_length += 1
if (name_length * name_count) + (otchestvo_length * otchestvo_count) + (
    surname_length * surname_count
) == buffer:
    print(
        "Ваш размен(Количество монет номиналом Фамилия,Имя,Отчество) =",
        surname_length,
        name_length,
        otchestvo_length,
    )
else:
    print("-42!")
