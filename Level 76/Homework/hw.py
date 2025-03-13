#1.
def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

#2.
def count(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

#3.
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

#4.
def reverse(s):
    return s[::-1]

#5. 
def longest(sentence):
    words = sentence.split()  # Splits sentence into a list of words
    return max(words, key=len) if words else ""
