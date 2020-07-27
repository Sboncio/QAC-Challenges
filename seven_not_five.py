def seven_not_five():
    output = ''
    for i in range(2000, 3200):
        if i % 7 == 0 and i % 5 != 0 :
            output += str(i) +','
    return output
