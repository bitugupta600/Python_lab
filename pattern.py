'''
n=int(input("Enter the number of rows:"))
for i in range(n+1):
    for j in range(i):
        print("*",end=" ")
    print()

enter the number 5
*
**
***
****
*****
'''
'''
n=int(input("Enter the number of rows:"))
for i in range(n+1):
    for j in range(n-i):
        print("*",end="")
    print()


*****
****
***
**
*

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j<=n-i:
            print(" ",end="")
        else:
            print("*",end="")
    print()
'''

'''
n = int(input("Enter the number of rows: "))
for i in range(n):  
    for k in range(1, n - i):  
        print(" ", end="")
    for j in range(2 * i + 1):  
        print("*", end="")
    print()  

'''

'''
1
12
123
1234
12345
'''
'''
n=int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end="")
    print()


i=0,1,2,3,4

i=0,j=0
i=1,j=0,1

1
22
333
4444
55555
'''

'''
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()
'''
'''
1
10
101
1010
10101


n=int(input("Enter Number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j%2, end="")
    print()
'''

'''
n=int(input("Enter Number"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if(j%2==0):
            print(0,end="")
        else:
            print(1,end="")
    print()

'''
'''
1
23
456
78910
'''
k=1
n=int(input("Enter the number of rows:"))
for i in range(n+1):
    for j in range(i):
        print(k,end="")
        k=k+1
    print()
    

'''
Initialize Variables:

Set k = 1 (starting number to print).
Take input from the user: n (number of rows).
Outer Loop for Rows:

Use a loop variable i to iterate from 0 to n (inclusive):
This controls the number of rows.
Inner Loop for Columns:

Use a nested loop variable j to iterate from 0 to i-1:
This controls the number of numbers printed on each row.
Print Numbers:

Inside the inner loop:
Print the current value of k without moving to the next line.
Increment k by 1.
New Line:

After the inner loop, move to the next line to start a new row.
End:

Exit the loops after printing all rows.

'''

for i in range(1,10,2)












    
