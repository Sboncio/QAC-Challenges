def factorials(discover):
    factorials = list()
    for i in range(2, discover):
        if discover % i == 0:
            factorials.append(i)
    return factorials

