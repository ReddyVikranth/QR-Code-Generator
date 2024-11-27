def data_type_printer(code,size,type):
    if type == 1:
        code[size-2,size-2] = 255
        code[size-2,size-3] = 255
        code[size-3,size-2] = 255
        code[size-3,size-3] = 0
    elif type == 2:
        code[size-2,size-2] = 255
        code[size-2,size-3] = 255
        code[size-3,size-2] = 0
        code[size-3,size-3] = 255
    elif type == 3:
        code[size-2,size-2] = 255
        code[size-2,size-3] = 0
        code[size-3,size-2] = 255
        code[size-3,size-3] = 255
    else:
        code[size-2,size-2] = 0
        code[size-2,size-3] = 255
        code[size-3,size-2] = 255
        code[size-3,size-3] = 255
    