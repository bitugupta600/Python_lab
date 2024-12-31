'''
f=open("f1.txt","r")
#print(f.read(5))
#print(f.readline())
print(f.readlines())
f.close()

import os
#os.rename("f1.txt","file1.txt")

os.remove("file1.txt")
print("Remove successfully...")

#print("Rename successfully...")

import os
#os.mkdir("Test")
#print("Directory created successfully...")
#print(os.getcwd())
#cwd-current working directal
os.chdir("B:\Python Anudip\text")
print(os.getcwd())

#WAP to read an entire text file
file_path='TextFile.txt'
try:
    with open(path,r) as file:
        content=file.read()
        print("File content\n")
        print(content)
except FileNotFoundError:
    print("File Not Found",file_path)
except exception as e:
    print("Error Occurred",e)


file_path = 'f1.txt'

try:
    with open(file_path, 'r') as file:
        content = file.read()  
        print("File content:\n")
        print(content)
except FileNotFoundError:
    print("File Not Found:", file_path)  
except Exception as e:  
    print("An error occurred:", e)

'''
def f_read(fname):
    try:
        with open(fname, 'r') as txt:
            print(txt.read())
    except FileNotFoundError:
        print(f"File Not Found: {fname}")
    except Exception as e:
        print(f"Error Occurred: {e}")
f_read("f2.txt")









