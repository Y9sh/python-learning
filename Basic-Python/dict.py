#✔ Create a dictionary of 3 programming languages with their release year
# ✔ Print each language with its year
# ✔ Add 1 new language
# ✔ Change the release year of one language
# ✔ Remove one language
# ✔ Print final dictionary

# Im trying : 
python_dict = {
    "language" : "python", "year" : "2015"
}
java_dict = {
    "language" : "java" , "year" : "2012"
}
cpp_dict ={
    "language" : "c++" , "year" : "2003"
}

print(python_dict["year"],java_dict["year"],cpp_dict["year"])
java_dict["language"] = "C#"
java_dict["year"] ="2000"

del cpp_dict["language"] 

for key, value in java_dict.items():
    print(key, ":", value)
    
for key, value in python_dict.items():
    print(key, ":", value)
    
for key , value in cpp_dict.items():
    print(key , ":", value)
    
print(python_dict,java_dict,cpp_dict)

# The more clarity : 

languages = {
    "python" : 2014,
    "java": 2012,
    "cpp" : 2000   
}

languages["C#"] =1990

languages["java"] = 2000 

del languages["cpp"]

for lang, year in languages.items():
    print(lang , ":", year)
'''
What is dictionary? 
- A group of key and value that pairs (name : age || irfn : 21 || year : 2000 )
- uses {} --> curley brackets
- each keys are unique no duplicate
- values can be anything 

🌙✨ 📝 My Thought Process

My question:
--
If I add the same key twice, will it store both values or only the latest one?
---
✔️ Answer:
In dictionaries, keys must be unique.
➡️ If you add the same key again, it overwrites the existing value.

So it will not store two values with the same key name.

🌙✨ Key Learning
✔ Dictionaries ➔ store unique key-value pairs
✔ Lists ➔ store multiple items in order
✔ For multiple dictionaries ➔ use list of dicts


'''