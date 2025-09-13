a = int(input("Введите Число\n"))
name = len(input("Введите ваше имя\n"))
surname = len(input("Введите вашу фамилию\n"))
otchestvo = len(input("Введите ваше отчество если оно есть\n"))
if otchestvo == 0:
    otchestvo = 19    
kolichestvoname = kolichestvosurname = kolichestvootchestvo = 0
buffer = a
while a >= min(name,surname,otchestvo):
    if a >= otchestvo:
        a = a - otchestvo
        kolichestvootchestvo+=1
    if a >= surname:
        a = a - surname
        kolichestvosurname+=1
    if a >= name:
        a = a - name
        kolichestvoname+=1
if (kolichestvoname*name)+(kolichestvootchestvo*otchestvo)+(kolichestvosurname*surname) == buffer:
    print("Ваш размен(Количество монет номиналом Фамилия,Имя,Отчество) =",kolichestvosurname,kolichestvoname,kolichestvootchestvo)
else:
    print('-42!')

