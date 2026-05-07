#Write a code that:
# Creates a list of your 5 favorite words
# Adds one more word to it
# Removes the second word
# Prints all items with their index

fav_dict = ["blue", "short hair", "sad","pout", "precious"]
print(fav_dict[2])

fav_dict.append("mwhehehe")
fav_dict.remove("short hair")
fav_dict.insert(4,"heh")
fav_dict.reverse()
fav_dict.sort()
fav_dict.extend("precious")

print(fav_dict[1])
print(fav_dict)

for item in fav_dict:
    print(item)
    
num = []
num.append(1)
print(num)
'''
What is lists?
- A group of multiple items stored under a single vaiable
- Ordered --> each items have an index as unique id (starting from 0)
- Mutable --> can be add , delete, edit

'''