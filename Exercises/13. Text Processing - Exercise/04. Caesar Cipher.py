message = input()
message_encrypted = ""

for letter in message:
    message_encrypted += chr(ord(letter) + 3)

print(message_encrypted)
