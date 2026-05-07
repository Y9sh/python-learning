#Example how to use it

def get_amount():
    while True:
        try: 
            amount = float(input("Enter amount: "))
            return amount
        except ValueError:
            print("Invalid input. Please enter a number.")
amt = get_amount()
print(f"Amount entered: {amt}")



'''
Topic : Error Handling (try/except)

📝 Why it matters:

Prevents your program from crashing on bad input.

Gives user-friendly messages when errors happen.

🔧 When to use try/except 

✅ When you do something that might fail unexpectedly:

| **Example**       | **Why might it fail?**                             |
| ----------------- | -------------------------------------------------- |
| `int(user_input)` | User types letters instead of numbers ➔ ValueError |
| `mylist[index]`   | Index out of range ➔ IndexError                    |
| `dict[key]`       | Key not found ➔ KeyError                           |
| Opening files     | File not found ➔ FileNotFoundError                 |

Diff between if...else and try/except :

| 🔹           | `if...else`              | `try...except`                   |
| ------------ | ------------------------ | -------------------------------- |
| **Use for:** | Logical checks on values | Handling errors during execution |
| **Example:** | Is age > 18?             | Input is not a number            |

Summary: 
 Use try/except ➔ for runtime errors like converting types, file operations, risky index/key access.
 Use if/else logic ➔ for checking user’s string input validity (empty, length, specific values).

'''