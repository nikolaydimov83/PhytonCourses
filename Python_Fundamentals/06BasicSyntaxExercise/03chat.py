numberOfMessages=int(input())
for i in range(numberOfMessages):
    messageCode=int(input())
    if messageCode==88:
        print('Hello')
    elif messageCode==86:
        print('How are you?')
    elif messageCode<88:
        print('GREAT!')
    else:
        print('Bye.')
    