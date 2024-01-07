banned=input().split(', ')
text=input()

for banned_word in banned:
    text=text.replace(banned_word, '*'*len(banned_word))
print(text)