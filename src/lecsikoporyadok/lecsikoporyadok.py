a = input('Введите первое слово\n')
b = input('Введите второе слово\n')
def obratniylecsikoporyadok(a,b):
    if a == b:
        print("Слова одинаковые")
    if a > b:
        return b
    else:
        return a
print(obratniylecsikoporyadok(a,b))