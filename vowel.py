def vowel_swapper(str_input):
    swap = {'a': '4', 'e':'3','i':'!','u':'|_|','O':'000'}
    str_input = str_input.replace('o', 'ooo')
    for i in range(len(str_input)):
        if str_input[i].lower() in swap:
            str_input = str_input[:i] + swap.get(str_input[i].lower()) + str_input[i+1:]
    return str_input

print(vowel_swapper("Everything's Available"))
