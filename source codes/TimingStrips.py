def timing_strips(code,length):
    x = 7
    y = 7
    while x < length - 8:
        code[x,y] = 0
        x += 2
    x = 7
    y = 7
    while y < length - 8:
        code[x,y] = 0
        y += 2
    