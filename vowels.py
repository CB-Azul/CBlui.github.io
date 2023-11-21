VOWELS = ('a', 'e', 'i', 'o', 'u')

def count_vowels(word):
    vowel_count = 0
    for letter in word:
        if letter in VOWELS:
            vowel_count += 1
    return vowel_count

 
word = "hello world"
count_vowel = count_vowels(word)
print(count_vowel)

