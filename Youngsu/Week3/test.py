for i in range(-10**10, 10**10):
    for j in range(-10**10, 10**10):
        for k in range(-10**10, 10**10):
            if i**3 + j**3 + k**3 == 33:
                print(i,j,k)