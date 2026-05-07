#💛 Mini Student Record System v2
# ✔ Use what you’ve learned:
# Functions
# Loops
# Lists & Dictionaries
# Inputs

#Make a mini program to:
# Ask how many students to input
# For each student, input:
# name,age,marks
# Store all data in a list of dictionaries
# After input is done, print each student’s record.

def system_banner():
    banner = '''---Welcome to Student Record System---'''
    print(banner)

def flow_system():
    student = []
    c = input("How many students?: ")
    integer = int(c)
#while integer > 0 :
    for count in range(integer):
        print(count)
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        marks = input("Enter student marks: ")

        student.append({"name" : name , "age" : age, "marks": marks})
        #count+=1
    
    #if count >= integer:
    for full in student: 
        print(f'{full["name"]} : {full["age"]} : {full["marks"]}')
            #print(full)
            
        #break


#pipeline
system_banner()
flow_system()


'''
Mistake and Overlooked :

You’re creating student = [] inside the loop, so it resets to an empty list every time ➔ only last data stays.

Realizes : 
for ___ in range(integer): 

_____ <--- any word inside this is works for count index number 
'''