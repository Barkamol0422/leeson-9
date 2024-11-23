a=input('Do you have medical cause. Y or N: ')
if a=='Y':
    print('You are allowed!')
else:
    b=int(input('Enter your attendance score: '))
    if b>75:
        print('You are allowed')
    else:
        print('You are not allowed')