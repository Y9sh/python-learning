# Reading a text file
# ✅ Make a sample text file first, e.g. sample.txt.
# ✅ Open the file with open(filename, 'r').
# ✅ Use .read() or .readlines() to get its content.
# ✅ Print out the content.
# ✅ Close the file (or use with open() for auto close).

import datetime

with open("any.txt","r") as f :
    print(f.read())


with open("examples.txt","w") as f:
    f.write("hello world")
    
with open("examples.txt", "a") as f:
    g = datetime.date.today()
    f.write(f"\nMy name is eman\n{g}")
    
    
    
'''
What im learned? 

with open() --> will open and auto-close 
.read() --> to get content 

"r" --> for read
"w" --> for write
"a" --> write without overwrite file/add more text


'''