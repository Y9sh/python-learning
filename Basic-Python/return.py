def num_list():
    num = [2,4,5,6]
    return num
n_num = num_list()
print(n_num)

# 🔎 Why?
#  Instead of having nums only inside the function, we return it so the rest of the program can use it.


def person_dict():
    person = {"name": "nyra" , "age": 19,"relay": "idk"}
    return person
people = person_dict()
print(people["name"])

#🔎 Why?
# When you store data structures in functions, your code becomes modular and reusable, like building blocks.

def student_profile(name, age, gpa):
    profile = {
        "name": name,
        "age": age,
        "gpa": gpa
    }
    return profile

# Using it:
student1 = student_profile("Nyra", 19, 3.5)
print(student1)

# 🔎 Why useful?
# You can store each returned dict in a list or database later.

'''
Functions Returning Dictionary or List ✨

💭 Why learn this?

Because when you build bigger systems, you will often:

Get data from functions to store/use elsewhere.

Separate input logic from processing logic.



'''