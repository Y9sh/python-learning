#✅ Project: Pet AI Simulator
# You will build a tiny text-based pet AI that:
# Has a name (your choice).
# Has hunger and happiness stats.
# Lets the user choose to feed or play with it each turn.
# Shows updated stats after each action.
# Ends if hunger reaches 10 (too hungry) or happiness reaches 0 (too sad).

def pet_name():
    banner ='''========== Welcome to Pet AI =========='''
    name = input("Enter your pet name: ")
    banner_name = (f'''Your pet name is {name} ''')
    print(f"{banner}\n{banner_name}")
    return name
    
def turn(name):
    hunger =1
    happiness =1
    print(f"Hunger: {hunger}\nHappiness: {happiness}")
    while hunger < 10 and happiness  > 0 :
        i= input("What do you want to do?\t(feed/play): ")
        if i == 'feed':
            print(f"fed your {name}")
            hunger-=1
            happiness+=0.5
            print(f"Hunger: {hunger}\nHappiness: {happiness}")
        elif i == 'play':
            print(f"play with {name}")
            happiness+=1
            hunger+=3
            print(f"Hunger: {hunger}\nHappiness: {happiness}")
        else:
            print("Invalid")
        
        if hunger >=10: 
            print(f"{name} too hungry")
            break
        elif happiness < 0 :
            print(f"{name} to sad")
            break
        else: 
            continue
                        
                
pet=pet_name()
turn(pet)

'''
KEY LEARNING ON THIS PROJECT : 

✅ Pass variables between functions (scope)
✅ Control loops with real conditions, not dummy always-true checks
✅ Structure logic cleanly before jumping to advanced like inheritance or OOP



'''