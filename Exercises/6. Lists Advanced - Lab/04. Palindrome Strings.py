words = input().split(" ")
palindrome_search = input()
palindrome_list = []

for i in words:
    if i == "".join(reversed(i)):
        palindrome_list.append(i)

print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome_search)}"
      f" times")

