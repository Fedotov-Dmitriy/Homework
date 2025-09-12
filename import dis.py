import dis
a = int(input('Введите натуральное число\n'))
def cubeofanumber(a):
    return a**3
print('Куб вашего числа =',cubeofanumber(a))
print(dis.dis(cubeofanumber))