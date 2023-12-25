word = input()
revWord=''
for i in range(0,len(word)):
    revWord+=word[len(word)-i-1]

print (revWord)

