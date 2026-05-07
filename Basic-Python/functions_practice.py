# A main menu function that decides what user wants.
# Separate functions to:
# Add student data
# Calculate GPA
# Adding multiple students in a loop
# Displaying summary at the end
# Display results

def add_student(students):
        name = input("Name: ")
        gpa = float(input("GPA: "))
        students.append({'name':name, 'gpa':gpa})
        #return students

def cat_gpa(student):

    if student['gpa'] >= 2.5:
        print("Pass")
    else:
        print("Failed")

def more_add_student(students):
    i = int(input("How many?: "))
    for _ in range(i):
        add_student(students)
    
def display(students):
    for student in students:
        print(f"Name: {student['name']}\nGPA: {student['gpa']}")
        cat_gpa(student)

def run():
    students = []
    #students = add_student(students)
    more_add_student(students)
    display(students)
run()



'''
🌟 🔰 New Concept Practice: Functions Calling Other Functions + Passing list/dict cleanly

📝 Why is this important?

Because real systems are not written in one giant function.
Instead, small modular functions call each other to perform clear sub-tasks, passing data (lists/dicts) smoothly between them.
Instead of repeating variables everywhere, you pass your list/dict between functions.

What im realized: 

print(students) ==> inside list , only can access list

after for gpa in students: 
    print(gpa) ==> inside the dict so we can manipulate inside dict not list anymore
--->Because each gpa should be categorized individually, not looping the full list each time.    

'''