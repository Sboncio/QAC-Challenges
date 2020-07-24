def addition(number, loops):
    end_num = 0
    for i in range(1,loops+1):
        concat_num = ""
        for j in range(i):
            concat_num += str(number)
        end_num += int(concat_num)
    return end_num

print(addition(9,5))