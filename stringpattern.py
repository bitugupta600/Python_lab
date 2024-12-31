#97-a, 124-z(small)
#65-A, 91-Z(Big)
''''
for i in range(65,91):
    print(chr(i),end=" ")
    
'''
'''
    ABCDE
    FGHIJ
    KLMNO
    PQRST
    UVWXY

c="A"
r=5
c=5
for i in range(r):
    l=" "*(4*i)
    for j in range(c):
        l+=c
        c=chr(ord(chr)+1)
    print(l)
..........................................
sc=65
r=int(input("Enter row"))
c=int(input("Enter row"))
for i in range(r):
      for j in range(c):
            print(sc,end="")
            sc+=1 
        print()
'''
'''
c = 65
n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(n):
        print(chr(c), end=" ")
        c += 1
    print()
'''

'''
    A
    AB
    ABC
    ABCD

'''
'''
n = int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print()


n=4
for: i=1,5
j=0,1
print(65+0=65: "A" )
#
n=4
i=2,5
j=1,i=2
print(65+1=66->"B")
#
n=4
for i=3,5
j=2,i=3
print->65+2=67->"C")
'''

'''
ABC
ABCD
ABCDE
'''
'''
c = 65  # ASCII value for 'A'
n = int(input("Enter the number of rows: "))

for i in range(n):
    for j in range(i + 1):
        print(chr(c + i), end="")
    print()

'''

'''
    A
   ABC
  ABCDE
 ABCDEFG
'''
'''
n = int(input("Enter the number of rows: "))
c = 65
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(2 * i + 1):
        print(chr(c + j), end="")
    print()



i=int(input("Enter Number"))
orig=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("Armstrong number")
else:
    print("Number is not Arnmstrong")
'''


import re

def check_password_validity(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return False, "Password must contain at least one digit."
    if not re.search(r'[@#$%^&+=!]', password):
        return False, "Password must contain at least one special character (@, #, $, %, ^, &, +, =, !)."
    return True, "Password is valid."
password = input("Enter your password: ")
valid, message = check_password_validity(password)
print(message)













