'''
try:
    x=int(input("Enter a number"))
    if x==2:
        raise IOError
except IOError:
    print("Input any Number other than 2")
else:
    print("The number is:",x)

try:
    x=int(input("Enter a number"))
    r=100/x
except Exception as e:
    print(e)
'''
class Demo(Exception):
    pass
try:
    x=int(input("Enter a number"))
    if x==2:
        raise Demo
except Demo:
    print("Enter any number other than 2")
else:
    print("The number is ",x)
