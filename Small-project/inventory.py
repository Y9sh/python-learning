# Inventory Manager:
# - add_item()
# - update_stock()
# - display_inventory()
# - calculate_total_value()
# 💡 Goal:
# Build a Mini Inventory System that can:
# ✅ 1. Add items with name, price, quantity
# ✅ 2. Update existing item stock
# ✅ 3. Show all items with total value

inventory = []

def banner():
    banner = '''Welcome to Inventory Manager System'''
    print(banner)
    
def add_item(name,price,quantity):
    inventory.append({
        "name":name,
        "price" : price,
        "quantity":quantity
    })
        
def display_all():
    title = '''Inventory'''
    gap ='''---------------------------------------------------'''
    print(gap)
    print(title)
    print(gap)
    for display in inventory:
        print(f"Name: {display["name"]} | Price:RM{display["price"]} | Quantity: {display["quantity"]}")
        total_value = display["price"] * display["quantity"]
        print(f"Name: {display["name"]} | Price:RM{display["price"]} | Quantity: {display["quantity"]} | Value:RM{total_value}")
        print(gap)
        
def main_menu():

    while True:
        print("------------------------")
        print("1.Add new item ")
        print("2.Update stock")
        print("3.Show Inventory")
        print("4.Exit")
        print("------------------------")
        choice =int(input("What you want to do?: "))
        print("------------------------")
        if choice == 1:
            add =int(input("How many items?: "))
            for _ in range(add):
                add_item(
                    name=input("Input name items: "),
                    price=int(input("Input price items: ")),
                    quantity=int(input("Input quantity items: ")))
        #ai helping how to make proper update
        elif choice == 2:
            user_updt = input("Input name item to update: ")
            exist = False
            for filter in inventory:
                if user_updt ==   filter["name"]:
                    print("------------------------")
                    print(f"Current -> Name: {filter['name']} | Price:RM{filter['price']} | Quantity: {filter['quantity']}")
                    print("------------------------")
                    filter["price"] = int(input("Input new pric: "))
                    filter["quantity"] = int(input("Input new quantity: "))
                    exist =True
                    print(f"{user_updt} has been updated.")
            if not exist:
                print(f"Invalid item name: {user_updt}")
        elif choice == 3 :
            display_all()
        
        else:
            break 

        

banner()
main_menu()

'''
Learned :
No need for i counter in while i < 100: if you use break to exit.
For clean exit, you can use while True: with break.
how to make a proper update exist items 


This my attempt: this not update its same as add but have filter

        elif choice == 2:
            user_updt = input("Input name items: ")
            for filter in inventory:
                if user_updt == filter["name"]:
                    print("------------------------")
                    print(f"Name: {filter["name"]} | Price:RM{filter["price"]} | Quantity: {filter["quantity"]}")
                    print("------------------------")
                    add_item(
                        name =input("Input new items: "),
                        price= int(input("Input new prices items: ")),
                        quantity=int(input("Input new quantity: ")))
            
                print(f"Invalid item name: {user_updt}")
                
                
'''