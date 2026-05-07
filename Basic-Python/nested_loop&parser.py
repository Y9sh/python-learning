#make simple pattern

for i in range(4):
    for j in range(i+1):
        print("* " ,end="")
    print()

# Task: Make a dictionary with:
# Key: "books" ➔ value: list of 3 book titles
# Key: "owner" ➔ value: your name

books = [
{ 
 "book" : ["ABC","AI","ML"],"owner" : "aiman"
},
{ 
 "book" : ["Love","Lust","Desire"],"owner" : "luna"
},
{ 
 "book" : ["python","game","hack"],"owner" : "lyna"
},
      
]

for owner in books: 
    print(f'{owner["owner"]}') #for display dict not list inside dict
    for book in owner["book"]:
        print(book) # this for display list inside dict 



#Make a dictionary with:
# Key: "pets" ➔ value: list of pet names
# Key: "owner" ➔ value: your name
# ✔ Print the owner and each pet name.

animal= [{"pets":["cat","hamster","bird"], "owner" : "nyra"},{"pets":["snake","spider","fly"], "owner" : "adam"},{"pets":["fish","drgonfly","bird"], "owner" : "sumi"}]

for owner in animal:
    print(f'{owner["owner"]}') # this not for display list in dict 
    for pet in owner["pets"]:
        print(pet)
    
# Make a list of dictionaries where each dictionary has:
# "subject" : subject name
# "score" : your score (number)

result = [{"subject": ["BI","BM","SN"] , "score" : [50,60,90] ,"student": "kermit"},
          {"subject": ["RBT","CH","MT"] , "score" : [90,40,60] ,"student": "pento"},
          {"subject": ["CA","AC","CS"] , "score" : [70,80,40] ,"student": "pupi"}
          ]


print(result)
#🟡 Logic Issue:
#✔ You looped score, then inside that loop you printed all subjects each time. This creates repeated full subject lists for each score
for student in result:
    print(f'{student["student"]}')
    for score in student["score"]:
        print(score)
        for subject in student["subject"]:
            print(subject)
    print()    
    
# Solve 

for student in result:
    print(f'{student["student"]}')
    for i in range(len(student["subject"])):
        print(f'subject: {student["subject"][i]}')
        print(f'score: {student["score"][i]}')
    print()
    
'''
What is Nested Loop ? 
-A loop that insid another loop 
-used for: PATTERN , GRIDS, DATA STRUCTURE

Nested data structure 
- A data structure that inside another 

Examples:

List of dictionaries

Dictionary of lists

Dictionary inside dictionary



'''