file_path = input().split(chr(92))
file_and_ext = file_path[-1].split(".")
file_name = file_and_ext[0]
file_ext = file_and_ext[1]

print(f"File name: {file_name}")
print(f"File extension: {file_ext}")