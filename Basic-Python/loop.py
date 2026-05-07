# ✅ Write a for loop that:'
# Prints numbers 1 to 10
# Prints only even numbers from 1 to 10
# Prints each letter in the word “Nyra”

for i in range(11):
    print(i)


for e in range(11):
    if e % 2 == 0:
        print(e)

word = ['N', 'y', 'r', 'a']
for letter in word:
    print(f"{letter}")

# alternative

for letter in "Nyra":
    print(letter)


# ✅ Write a loop that:
# Prints numbers from 10 down to 1
# Prints the sum of numbers from 1 to 5
# Prints “even” or “odd” for each number from 1 to 5

for i in range(1, 11)[::-1]:
    print(i)

for i in range(10, 0, -1):
    print(i)


while (i < 11 and i > 0):
    print(i)
    i += 1

sum = 0
for l in range(1, 6):
    sum += l
print(sum)

k = 1
while k < 6:
    if k % 2 == 0:
        print("even", k)
    else:
        print("odd", k)

    k += 1

# ✅ 1. Write a while loop to print numbers from 5 down to 1.
# ✅ 2. Write nested for loops to print

i = 5
while i > 0:
    print(i)
    i -= 1

n = 4
for rows in range(n):
    print("*")
    for per in range(rows+1):
        print("* ", end="")
        for last in range(per - 2):
            print("* ", end="")
print()
n =4 
for row in range( n + 1):
    for star in range(row):
        print("*", end=" ")
    print()

#💛 [Loop-based Mini Game: Guessing Game (Easy version)]
# ✅ Your task:
# Write a simple guessing game where:
# The answer is fixed as "nyra".
# User has 3 chances to guess it right.
# If guessed correctly ➔ print “You won, wolf!”
# If failed after 3 chances ➔ print “You lost, my wolf. The answer was nyra.”

answer = "Nyra"
for chance in range(3):
    guess = input("What is the correct answer?: ")
    if guess == answer:
        print("You won , you did it!!!!!!") 
        break  
    elif chance < 2 and guess!=answer :
        print("Try again!!") 
    else:
        print("You lost, The answer is Nyra")
'''
LEARN:
 
1. What is a for loop?
Loop is block of multiple code that keep repeat until certain condition is met

For Loop: commonly used on repetitive over a sequence such as list , tuple , string or range (BASIC TO NESTED)

2. What is while loop? 
While loop is will still repeat as long the condition is TRUE (CONDITIONS)

3.What is nested loops?
Nested loop is condition that loop is inside the loop. (Used for grids, tables, combinations,)
'''
