def characters_length(code,length,size):
    binary = bin(length)[2:].zfill(8)
    binary = reversed(binary)
    x = size - 4
    y = size - 2
    for data in binary:
        if data == '1':
            code[x,y] = 0
        else:
            code[x,y] = 200
        if y == size - 2:
            y -= 1
        else:
            x -= 1
            y += 1
