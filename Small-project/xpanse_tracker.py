#  Practice Project: Mini Expense Tracker
# TIME SPEND = 3 HOURS 30 MINUTE
# 3/7/25
expanses = []


def title():
    banner = '''Welcome to Xpanse Tracker'''
    print(banner)


def add_xpanse(name, category, amount):
    expanses.append({
        'name': name,
        'category': category,
        'amount': amount
    })
    return expanses


def total_by_cat():

        user_input = str(input("Input category type: "))
        print(f"Category: {user_input}")
        total_each = 0
        found = False
        for by_cat in expanses:
            if user_input == by_cat['category']:
                print(f"Item:{by_cat['name']}")
                found = True
                try:
                    total_each += int(by_cat['amount'])
                except ValueError:
                    print(f"Invalid amount for {by_cat['name']}. Skipping...")
        if found == True:
            print(f"Total: {total_each}")
        else:
            print(f"No items on {user_input}")


def delete_expanse():
    '''REMEMBER THIS HOW TO DELETE PROPER ON LIST DICT FOR EXACT INDEX'''
    user_input = input("Input name items to delete: ")
    found = False
    for i in range(len(expanses)):
        if user_input == expanses[i]['name']:
            del expanses[i]
            found = True
            break
    if found == True:
        print(f"Delete {user_input} succesfully!!!")
    else:
        print(f"No item {user_input}, found")


def update_expanse():

    user_input = input("Input name items to update: ")
    found = False
    for updating in expanses:
        if user_input == updating['name']:
            user_update = int(
                input("What do you want to update?\n1.Name\n2. Category\n3. Amount\n"))
            found = True
            if user_update == 1:
                updating['name'] = input("Input new name: ")

            elif user_update == 2:
                updating['category'] = input("Input new category: ")

            elif user_update == 3:
                updating['amount'] = input("Input new amount: ")
            else:
                found = False
    if found == True:
        print(f"Update new {user_update} successfully!!!!")
    else:
        print(f"{user_input} not exists")


def main_menu():

    while True:
        print("1. Add item")
        print("2. View by category")
        print("3. Delete item")
        print("4. Update item")
        print("5. Exit")
        try: 
            choice = int(input("Choose your next step: "))

            if choice == 1:
                add_xpanse(name=input("Input name item: "), category=input(
                    "Input type category: "), amount=input("Input amount item: "))
            elif choice == 2:
                total_by_cat()
            elif choice == 3:
                delete_expanse()
            elif choice == 4:
                update_expanse()
            else:
                break
        except ValueError:
            print("Input only number.")
      

title()
main_menu()
'''
Where did im stuck!!!!!!!!!

When to delete exactly 1 dict not just 1 argument on dict......
Solution:
-- 
for i in range(len(expanse)) 
---
thiss will count the list in expanse remember this !!!!

💭 Key Points
✅ Use range(len(expanses)) when deleting by index.
✅ Delete from the list itself, not from a dict’s key list.
✅ Always break after delete to avoid skip issues.
✅ Correct placement of found = True and its if check.

When making update fction, dont confuse if you want to change only 1: 
--
expanse['name'] = new_name 
----
no need to use append({}) for update single arguments because it will change all inside the dict
------
💡 Key Learning Goals
Practice list search logic

Practice update within dicts in list

Practice delete by index or item

'''
