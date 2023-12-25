a=float(input())

positiveNegativeType=''

if a ==0:
    positiveNegative='zero'
elif a<0:
    positiveNegative='negative'
elif a>0:
    positiveNegative='positive'
else:
    positiveNegative='Not a number'

smallLargeType=''

if a>1000000 or a<-1000000:
    smallLargeType='large '
if a*a<1 and a*a>0:
    smallLargeType='small '

print(smallLargeType+positiveNegative)