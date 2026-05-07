#Mini Shopping Cart System
# ✔ Ask how many items to add
# ✔ For each item input:
# name
# price
# quantity
# ✔ Store all in list of dictionaries
# ✔ After input, print each item with total cost (price x quantity)


def banner():
    banner = ''' Mini Shopping Cart System '''
    print(banner)
    

def system_run():
    items=[]
    
    item = input("How many items to add into a cart?: ")
    x = int(item)
    
    for count in range(x):
        name = input("Name item: ")
        price = input("Prices: ")
        quantity = input("Quantity: ")
        total = int(quantity) * float(price) # THIS WHERE AND HOW TO USE IT
        items.append({"name":name, "price": price,"quantity": quantity, "total": total})
        
    for y in items:
       print(f'Item:{y["name"]}\nPrice:{y["price"]}\nQuantity:{y["quantity"]}\nTotal:{y["total"]}')
    
    
    

#pipline
banner()
system_run()

'''
What im learned...
---
✨ Why Casting Needed?
Because inputs return string type by default ➔ operations like multiplication need int or float.
-----


'''