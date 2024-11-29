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
        base[size-6-i,size-6] = 0
        base[size-6-i,size-10] = 0
        base[size-6,size-6-i] = 0
        base[size-10,size-6-i] = 0
    
    base[size-8,size-8] = 0

    for i in range(5):
        base[2,i+2] = 200
        base[6,i+2] = 200
        base[i+2,2] = 200
        base[i+2,6] = 200
        base[2,size-7+i] = 200
        base[6,size-7+i] = 200
        base[i+2,size-3] = 200
        base[i+2,size-7] = 200
        base[size-3,i+2] = 200
        base[size-7,i+2] = 200
        base[size-3-i,2] = 200
        base[size-3-i,6] = 200

    for i in range(3):
        base[size-7,size-7-i] = 200
        base[size-9,size-7-i] = 200
        base[size-7-i,size-7] = 200
        base[size-7-i,size-9] = 200
         