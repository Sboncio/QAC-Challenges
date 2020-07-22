def order_words(sentence):
    list_of_words = sentence.split(" ")
    words = set(list_of_words)
    words = sorted(words)
    output = ""
    for word in words:
        output += word + " "
    return output

