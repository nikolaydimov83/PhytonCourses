word_list=input().split(' ')
palindrome=input()
count=0
palindromes=[]
for word in word_list:
     reversed_word=list(word)
     reversed_word.reverse()
     if word==''.join(reversed_word):
          palindromes.append(word)
          if palindrome==word:
               count+=1

print(palindromes)
print(f"Found palindrome {count} times")