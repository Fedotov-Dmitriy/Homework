def make_change(amount, a, b, c):
    if amount < 0 or a <= 0 or b <= 0 or c <= 0:
        return None
    for x in range(amount // a + 1):
        for y in range(amount // b + 1):
            rem = amount - (x * a + y * b)
            if rem >= 0 and rem % c == 0:
                return x, y, rem // c

    return None


amount = int(input())
name = input()
surname = input()
otchevstvo = input()

name_len = len(name)
surname_len = len(surname)
otchevstvo_len = len(otchevstvo) if otchevstvo != "" else 19

res = make_change(amount, name_len, surname_len, otchevstvo_len)

if res is None:
    print("-42!")
else:
    x, y, z = res
    # Размен в порядке: (имя, фамилия, отчество)
    print(x, y, z)
