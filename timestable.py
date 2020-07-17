number = int(input("Please insert a times table: "))

for i in range(number):
    for j in range(number):
        print((i+1)*(j+1), end='\t')
    print('\n')
