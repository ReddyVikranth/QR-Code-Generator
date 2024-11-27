def base_printer(base,size):
    for i in range(1,8):
        base[1,i] = 0
        base[i,1] = 0
        base[i,7] = 0
        base[7,i] = 0
        base[size-8,i] = 0
        base[size-2,i] = 0
        base[size-i-1,1] = 0
        base[size-i-1,7] = 0
        base[1, size-i-1] = 0
        base[7, size-i-1] = 0
        base[i, size-2] = 0
        base[i, size-8] = 0
    for i in range(3,6):
        base[i,3] = 0
        base[i,4] = 0
        base[i,5] = 0
        base[i,size-4] = 0
        base[i,size-5] = 0
        base[i,size-6] = 0
        base[size - i - 1,3] = 0
        base[size - i - 1,4] = 0
        base[size - i - 1,5] = 0
    for i in range(5):
        base[size-5-i,size-5] = 0
        base[size-5-i,size-9] = 0
        base[size-5,size-5-i] = 0
        base[size-9,size-5-i] = 0
    
    base[size-7,size-7] = 0
