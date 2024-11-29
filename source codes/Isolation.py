def isolation(code,length):
    x = 8
    y = 8
    while x > 0:
        code[x,y] = 200
        x -= 1
    x = 8
    while y > 0:
        code[x,y] = 200
        y -= 1
    y = length - 9
    while x > 0:
        code[x,y] = 200
        x -= 1
    x = 8
    while y < length:
        code[x,y] = 200
        y += 1
    y = 8
    x = length - 9
    while x < length:
        code[x,y] = 200
        x += 1
    x = length - 9
    while y > 0:
        code[x,y] = 200
        y -= 1