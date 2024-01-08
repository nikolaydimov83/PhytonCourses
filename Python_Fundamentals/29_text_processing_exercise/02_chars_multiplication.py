words=input().split(' ')
length_short=min(len(words[0]),len(words[1]))
length_long=max(len(words[0]),len(words[1]))
longer_word=''
shorter_word=''
sum=0
if len(words[0])==length_long:
   longer_word=words[0] 
   shorter_word=words[1]
else:
   longer_word=words[1]
   shorter_word=words[0]

for i in range(length_long):
   if i<length_short:
     sum+=ord(longer_word[i])*ord(shorter_word[i])
   else:
      sum+=ord(longer_word[i])
print(sum)
       