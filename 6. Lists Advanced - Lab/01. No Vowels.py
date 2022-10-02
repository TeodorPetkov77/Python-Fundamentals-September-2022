word = input()
vowels = ['a', 'o', 'u', 'e', 'i', 'A', 'O', 'U', 'E', 'I']

word_no_vowels = "".join([x for x in word if x not in vowels])
print(word_no_vowels)