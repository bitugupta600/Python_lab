'''
a=16
try:
    x=int(input("Enter number"))
    b=a/x
    print(b)
except ValueError:
    print("This is not a valid Number")
except ZeroDivisionError:
    print("Division By Zero")


except ValueError:
    print("This is not a valid number")
except ZeroDivisionError:
    print("Divided by zero")



a = 16
try:
    x = int(input("Enter a number: "))
    b = a / x
# except ValueError:
#     print("This is not a valid number")
# except ZeroDivisionError:
#     print("Divided by zero")
except (ValueError, ZeroDivisionError):
    print("There is an exception..")
else:
    print(b)
'''

a=16
try:
    x=int(input("Enter a number"))
    b=a/x
    print(b)
finally:
    print("End of the program")
    
    
