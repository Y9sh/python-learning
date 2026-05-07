#Create a list of dictionaries for 3 students
# Each dictionary stores:
# name
# age
# marks

students_list =[{
    "name" : "mannie",
    "age"  : 19,
    "marks": "-10%"
},
{    
    "name" : "lyna",
    "age"  : 18,
    "marks": "68%"
},             
{    
    "name" : "ikmal",
    "age"  : 21,
    "marks": "1%"
},  
]


students_list[2]["name"] = "huii"

students_list.append({"name": "Lulu", "age": 18 , "marks": "19%"})

for data in students_list:
    print(f'{data["name"]} : {data["age"]} : {data["marks"]}')


print("For display all data")
for student in students_list:
    print(student)

print("While methods")
i =0
while i < len(students_list):
    print(students_list[i])
    i+=1
    
'''
What im learned? 

❌ Issue with print(f"{data["name"]}...")
- Potential error
- Better using single quotes outside, or escape the inner quotes

(len) :
- i < len(students_list)
- len for representing number of items inside the object
'''