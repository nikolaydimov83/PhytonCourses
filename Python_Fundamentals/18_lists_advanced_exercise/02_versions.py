version_int=int(''.join(input().split('.')))
version_int+=1
new_version='.'.join(list(str(version_int)))
print(new_version)
