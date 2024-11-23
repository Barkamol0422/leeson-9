a=int(input('Enter number of units'))
if a<50:
    amount=a*2.6
    tax=25
elif a<100:
    amount=a*3.25
    tax=35
elif a<200:
    amount=a*5.26
    tax=45
else:
    amount=a*8.45
    tax=75
total=amount+tax
print(total)
