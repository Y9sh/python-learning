#🔥 Topic 1 – Functions Quick Recap
# 💡 Practice:
# Write a function to:
# Add two numbers and return the result.
# Multiply two numbers and print the result.

def add(n1, n2):
    sum = n1 + n2
    return sum 

def multiple(n1,n2,sum):
    mult = n1 * n2 
    print(f"Sum: {sum}")
    print(f"Total: {mult}")
    
n1 =2 
n2 = 10

sum=add(n1,n2)
multiple(n1,n2,sum)
        
#🔥 Topic 2 – Lists & Dictionaries Quick Recap
# 💡 Practice:
# Create a list of 3 fruits and print each one.
# Create a dictionary with “name”, “age”, “skill” and print all keys and values.

frut = ["apple ", "pineapple", "banana"]

for e in range(len(frut)):
    print(frut[e])

for fruit in frut:
    print(fruit)

person = {"name": "ali", "age" : "21", "skill": "fishing"}

print(person["name"],person["age"],person["skill"])

for key, value in person.items():
    print(key , ":" ,value)
    

#Recap 2/7/2025
# Return a dictionary from a function.
# Write a function student_info() that:
# Takes name, age, skill as parameters.
# Returns a dictionary containing them.

def student_info(name,age,skill):
    
    student = {
        "name": name,
        "age": age,
        "skill":skill
    }
    
    return student

print(student_info("iman",12,"css"))


#Return a list from a function.
# Write a function subjects_list() that:
# Takes three subjects as parameters.
# Returns them as a list.

def sub_list(sub1,sub2,sub3):

    subject = [
        sub1,sub2,sub3
    ]
    
    return subject 

print(sub_list("Math", "Machine Learning","AI"))