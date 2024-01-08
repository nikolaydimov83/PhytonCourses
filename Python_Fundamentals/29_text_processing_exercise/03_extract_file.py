file_exten=input().split('\\')
file_name, extension=file_exten[len(file_exten)-1].split('.')

print(f"File name: {file_name}")
print(f"File extension: {extension}")