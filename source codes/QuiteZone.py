def quite_zone(code,length):
    x = 0
    y = 0
    while y < length:
        code[x,y] = 200
        y += 1
    y -= 1
    while x < length:
        code[x,y] = 200
        x += 1
    x -= 1
    while y >= 0:
        code[x,y] = 200
        y -= 1
    y += 1
    while x >= 0:
        code[x,y] = 200
        x -= 1
    