message = input()
message_encrypted = ""

for letter in message:
    message_encrypted += chr(ord(letter) + 3)

print(message_encrypted)

# https://judge.softuni.org/Contests/Compete/Index/1740#3

# 04. Caesar Cipher

# 4.	 Caesar Cipher
# Write a program that returns an encrypted version of the same text. Encrypt the text by replacing each character with the corresponding character three positions forward in the ASCII table. For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.
# Examples
# Input	Output
# Programming is cool!	Surjudpplqj#lv#frro$
# One year has 365 days.	Rqh#|hdu#kdv#698#gd|v1