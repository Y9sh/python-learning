#🎯 Student Record – Enhancement
# Extend yesterday’s student record to include:
# GPA input
# Auto-calculate “Pass” if GPA >= 2.5 else “Fail”
# Display full details clearly for each student.

def system_banner():
    banner = '''---Welcome to Student Record System---'''
    print(banner)

def flow_system():
    student = []
    c = input("How many students?: ")
    integer = int(c)
#while integer > 0 :
    for _ in range(integer):
        #print(count)
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        marks = input("Enter student marks: ")
        gpa = float(input("Enter GPA: "))
        
        if gpa >= 2.5:
            result = "Pass"
        else:
            result ="Fail"
            
        student.append({"name" : name , "age" : age, "marks": marks , "GPA": gpa,"result" : result})
        #count+=1
    
    #if count >= integer:
    for full in student: 
        print(f'{full["name"]} : {full["age"]} : {full["marks"]} : {full["GPA"]} : {full["result"]}')
            #print(full)
            
        #break


#pipeline
system_banner()
flow_system()

'''
⚠️ Minor suggestions to refine :
🔹 a. Remove unused comments to keep code clean.
🔹 b. count isn’t used outside loop – you can simplify further by removing it entirely if unneeded.
🔹 c. Consider input validation for GPA, age, and marks in future improvements to avoid user entry errors.

Explain for b. : 
for count in range(integer) already increments automatically each loop.
You don’t use count outside the loop, so you could write:
--
for _ in range(integer):
    ...
----
Using _ is Pythonic when the variable is unused. It improves readability by showing: “I don’t need the loop index here, just looping n times.”

'''