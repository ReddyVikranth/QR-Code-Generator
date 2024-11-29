def final_cut(code,size):
    for i in range(size):
        for j in range(size):
            if code[i,j] == 200:
                code[i,j] = 255
