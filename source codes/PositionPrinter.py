def position_printer(code,size):
    x = size - 2
    y = size - 2
    while True:
        if code[x,y] != 0 or code[x,y] != 200:
            return [x,y]
        