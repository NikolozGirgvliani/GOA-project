def most_frequent_word(sentence):
    words = sentence.split()
    most_frequent = ''
    max_count = 0

    for word in words:
        count = words.count(word)
        if count > max_count:
            most_frequent = word
            max_count = count
    
    return most_frequent

sentence = input("Enter a sentence: ")
result = most_frequent_word(sentence)
print(f"The most frequent word is: {result}")
