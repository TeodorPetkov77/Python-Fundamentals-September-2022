banned_words = input().split(", ")
input_text = input()

for b_word in banned_words:
    while b_word in input_text:
        input_text = input_text.replace(b_word, "*" * len(b_word))

print(input_text)