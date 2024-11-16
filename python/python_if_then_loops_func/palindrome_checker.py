def is_palindrome(word):
    if word == word[::-1]:
        print(f"{word} is a palindrome")
    else: 
        print(f"{word} is not a palindrome")

is_palindrome("hello")
is_palindrome("racecar")

"""version 2"""
def a_palindrome(word):
    return word == word[::-1]

word = input(str("provide word to check if palindrome: "))
print(a_palindrome(word))