inputTimes=int(input())

for i in range(0,inputTimes):
    currentInput=int(input())
    if (currentInput%2==1):
        print(str(currentInput)+' is odd!')
        break
else:
    print('All numbers are even.')