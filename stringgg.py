'''
string = "To change the overall look of your document. To change the look"
count = 1
for i in string:
    if i == " ":
        count=count+1
print(count)

#

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count("To change the overall look of your document. To change the look"))
'''
'''
Write a Python program to remove a newline in Python

String = "\nBest \nDeeptech \nPython \nTraining\n"

#
string = "\nBest \nDeeptech \nPython \nTraining\n"
cs = string.replace("\n"," ".strip())
print(repr(cs))
#

Write a Python program to count and display the vowels of a given text

String=”Welcome to python Training”
#
string = "Welcome to python Training"
vowels = "aeiou"
vowel_count = {v: string.lower().count(v) for v in vowels}
print("Vowel counts in the given text:")
for vowel, count in vowel_count.items():
    if count > 0:
        print(f"{vowel}: {count}")



#Write a Python program to Count all letters, digits, and special symbols from the given string

 #Input = “P@#yn26at^&i5ve”
# Input string
input = "P@#yn26at^&i5ve"
l=d=ss=0
for char in input:
    if char.isalpha():
        l+= 1
    elif char.isdigit():
        d+= 1
    else:
        ss+= 1
print("Letters:",l)
print("Digits:", d)
print("Special Symbols:",ss)


#give a string travers strming 1st postion to last position then if 
1st >= and less than 9 then digit++ elif print alfabet else print special character
l=d=ss=0


# Write a Python program to remove duplicate characters of
a given string.
#Input = “String and String Function”


def rd(i_s):
    r=""
    for char in i_string:
        if char not in r:
            r=r+char
    return r
i_string="Lloyd Institute of Engineering and Technology"
output=rd(i_string)
print("output",output)



input_str="P@#yn26at^&i5ve"
output=""
for char in input_str:
    if '1'<= char <='9':
        output=output+char
    elif 'a'<= char <='z' or 'A' <=char <='Z':
        output=output+char
    else:
        output=output+char
print(output)

input_string = "b1c2d*68#"
output = ""
for char in input_string:
    if '1' <= char <= '9':
        output += str(int(char) + 1)  
    elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':   
        output += char  
    else:
        output += char  
print(output)



#a-letter, b=digit,c=special symbol
input = "P@#yn26at^&i5ve"
a=b=c=0
for char in input:
    if '1' <= char <= '9':
        a+=1
    elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        b+= 1
    else:
        c+= 1
print("Letters:",a)
print("Digits:", b)
print("Special Symbols:",c)
'''

#a-digit, b=letter,c=special symbol
#input = "P@#yn26at^&i5ve"
input = "bitu%$##@^@&JFeyfe62054"
a=b=c=0
for char in input:
    if '0' <= char <= '9':
        a+=1
    elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        b+=1
    else:
        c+=1
print("digit:",a)
print("letter:", b)
print("Special Symbols:",c)








