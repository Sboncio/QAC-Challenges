def timestable(max):
    table = ''

    for i in range(max):
        for j in range(max):
            table += str(((i+1)*(j+1))) + '\t'
        table += '\n'
        
    return table

number = int(input("Please insert a times table: "))
print(timestable(number))