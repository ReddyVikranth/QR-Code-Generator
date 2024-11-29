def timing_strips(code,length):
    x = 7
    y = 7
    while y < length - 9:
        code[x,y] = 0
        y += 2
    y = 7
    x = length - 10
    while x > 8:
        code[x,y] = 0
        x -= 2
    