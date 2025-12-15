def encrypt(text):
    data = text.encode("utf-8")                
    bits = "".join(f"{b:08b}" for b in data)    

    out = []
    for i in range(0, len(bits), 4):
        d1 = int(bits[i])
        d2 = int(bits[i + 1])
        d3 = int(bits[i + 2])
        d4 = int(bits[i + 3])

       # 1=p1, 2=p2, 3=d1, 4=p4, 5=d2, 6=d3, 7=d4
        p1 = d1 ^ d2 ^ d4
        p2 = d1 ^ d3 ^ d4
        p4 = d2 ^ d3 ^ d4

        out.append(f"{p1}{p2}{d1}{p4}{d2}{d3}{d4}")

    return "".join(out)


def decrypt(bits):

    if any(c not in "01" for c in bits):
        raise ValueError("Вход должен состоять только из '0' и '1'")
    if len(bits) % 7 != 0:
        raise ValueError("Длина должна быть кратна 7")

    for block_start in range(0, len(bits), 7):
        b = bits[block_start:block_start + 7]
        b1, b2, b3, b4, b5, b6, b7 = [int(x) for x in b]

        s1 = b1 ^ b3 ^ b5 ^ b7
        s2 = b2 ^ b3 ^ b6 ^ b7
        s4 = b4 ^ b5 ^ b6 ^ b7
        syn = s1 + 2 * s2 + 4 * s4   # 0 или 1..7

        if syn != 0:
            # возвращаем позицию ошибки
            return block_start + (syn - 1)

    return -1
