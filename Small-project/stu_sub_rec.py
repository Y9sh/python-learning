#💻 📝 TASK: Student & Subjects Record
# ✅ Goal:
# Create a list of students
# Each student has: name, age, subjects (list), marks (list)
# Print each student with their subjects & marks nicely
# ------------
# 🐾 Steps:
# Ask how many students to add
# For each student:
# Input name, age
# Input number of subjects
# For each subject:
# Input subject name
# Input mark
# Store all data properly
# Print nicely at the end
#------------------

def title():
    banner ='''Student & Subject Record'''
    print(banner)


def run():
    students= []
    
    i = int(input(" How many students to add?: "))
    
    while i > 0 : 
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        subject = int(input("How many subjects: "))
        subjects = []
        for _ in range(subject):
            subject_name =input("Enter subject name: ")
            marks = int(input("Enter mark: "))
            subjects.append({"subject": subject_name, "marks":marks})
        i-=1
        
        students.append({"name" : name,"age":age,"subjects":subjects})
    #what im try
    for content in students:
        print(f"Name:{content["name"]}\nAge:{content["age"]}")
        for other in subjects:
            print(f"Subjects:{other["subject"]}\nMarks:{other["marks"]}")
    
    '''
    💡 Issue:
    You’re looping over subjects which is not linked to each student individually because you used the outer variable subjects instead of each student’s own subjects.
    
    '''
    # AI refine 
    for content in students:
        print(f"Name: {content['name']}\nAge: {content['age']}")
        for other in content['subjects']:
            print(f"Subject: {other['subject']}\nMarks: {other['marks']}")
            
    ''' 
    ⭐ Why?
    Because content['subjects'] accesses that specific student’s list of subjects, avoiding duplication or wrong outputs from the outer subjects list.
    
    '''

title()
run()


'''
Where im stuck ? 

Keep overwriting subject_name and marks in each loop , so the last output keep save the last one 
Actually its because list inside the dict inside the list 

So how to solve it ? 

Make a seperate append for new list a.k.a in this code is subjects = [] 
So each dict inside list have own append, students =[] and subjects =[]
For the final output , combine it in 1 core append 
students append include subjects
No need to append 1 by 1 , take a full list instead from other dict

'''