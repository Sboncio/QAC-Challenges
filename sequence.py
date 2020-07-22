def order_words(sentence):
    list_of_words = sentence.split(" ")
    words = set(list_of_words)
    words = sorted(words)
    return words

