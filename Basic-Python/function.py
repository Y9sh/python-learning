def get_sum(num1 , num2):
    
    if num1 > 0 and num2 > 0: 
        return num1 + num2 
    else: 
        return "invalid"
    
print(get_sum(2,5))
print(get_sum(-5, -4))


def get_info():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
    print(f"Your Information: {name} , {age}")
    
get_info() 

def check_word(word):
    if word == word [::-1]: # check if the word will same in backward and foward
        return "Palindrome"
    else:
        return "nope"
    
print(check_word("oppai"))
print(check_word("noon"))


def get_max(): 
    num = {1,2,4,5,6,7,9}
    maximum = max(num) # min() and max() remember this its a builts in function from python 
    return maximum
print(get_max())
    

def get_count_vowels(word):
    
    vowels = {'a','e','i','o','u'}
    count = 0
    for letter in word:
        if letter in vowels : 
            count+=1
    return count
print(get_count_vowels("happy"))
print(get_count_vowels("lesgooo"))

'''
LEARNING: 

What is FUNCTIONS? 
its like a block that can be reused again that perform a specific task inside it...

Parameters vs Arguments

Param == (___) <--- definition/representative for arguments values (example : name)
Args == (___) <--- the values inside param (example: nyra , irfn)

✅ Parameter: The variable name inside the function definition that receives input.
✅ Argument: The actual value passed to that parameter when calling the function.

Return vs Print

return == gives value back 
print == displays to console but return None

QNA: 
✔ Why use return instead of print?
✅ Return sends data back for further use (like passing it to another function or storing it).
✅ Print just displays text to the screen; the function still returns None.

✔ What happens if we forget to return?
“no values will return, so return is very important to give what values we want to send to other part or print it properly.”

What was your biggest realisation today about functions and your learning journey?

✅ Parameter is the variable name in function definition that receives the value (argument) passed when calling the function.

So, the parameter is not the exact name of the value – it’s a placeholder that receives whatever value (argument) you pass in.



'''