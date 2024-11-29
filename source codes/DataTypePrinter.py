def data_type_printer(code,size,type):
    if type == 1:
        code[size-2,size-2] = 200
        code[size-2,size-3] = 200
        code[size-3,size-2] = 200
        code[size-3,size-3] = 0
    elif type == 2:
        code[size-2,size-2] = 200
        code[size-2,size-3] = 200
        code[size-3,size-2] = 0
        code[size-3,size-3] = 200
    elif type == 3:
        code[size-2,size-2] = 200
        code[size-2,size-3] = 0
        code[size-3,size-2] = 200
        code[size-3,size-3] = 200
    else:
        code[size-2,size-2] = 0
        code[size-2,size-3] = 200
        code[size-3,size-2] = 200
        code[size-3,size-3] = 200
    