#str1 = "racecar"
#print(str(reversed(str1))

#original_string = "Hello, World!"
#reversed_string = ''.join(reversed(original_string))
#print(reversed_string)


def is_palindrome(word):
    is_pal = None
    if word == ''.join(reversed(word)):
        is_pal = True
    else:
        is_pal = False

    return is_pal

word1 = input("Please in put a word:\n")
palindrome=is_palindrome(word1)
print(palindrome)