import dis
a = int(input('Введите Натуральное число\n'))
def cubeofnumber(a):
    if a <= 0:
        return "Число не является натуральным"
    else:
        return a**3
print(cubeofnumber(a))
print(dis.dis(cubeofnumber))