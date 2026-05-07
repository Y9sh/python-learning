# 📝 🌟 Mini Task Manager – Workflow Plan
# ✅ 1. Prepare a main list to store tasks.
# Each task is a dictionary with:
# title
# due date
# status ("pending" by default, changes to "complete" when marked).
# ✅ 2. Functions needed:
# add_task(tasks) ➔ adds a new task.
# mark_complete(tasks) ➔ changes status to complete.
# delete_task(tasks) ➔ removes task by title.
# show_tasks(tasks) ➔ displays all tasks, showing pending & completed clearly.
# ✅ 3. Main menu loop
# Options:
# Add Task
# Mark Complete
# Delete Task
# Show Tasks
# Exit

def name():
    banner = '''Task Manager'''
    print(banner)

def main_menu(task):
    while True:
        print("1.Add Task\n2.Mark Complete\n3.Delete Taks\n4.Show Tasks\n5.Exit")
        choice = int(input("What's next?: "))
        if choice == 1 :
            add_task(task)
        elif choice ==2 :
            mark_status(task)
        elif choice == 3 :
            delete_task(task)
        elif choice == 4 :
            show_tasks(task)
        elif choice == 5 : 
            print("GoodByee~~")
            break
        else: 
            print("Invalid choice. Try again")
            
def add_task(task):
    u_total = int(input("How many task?: "))
    for _ in range(u_total):
        title = input("Enter task name: ")
        due_date = input("Enter due date task: ")
        status = "Pending"
        task.append({
            "title" : title,
            "due_date" : due_date,
            "status" : status
        })
        
def mark_status(task):
    u_title = input("Enter task title to marks as completed: ")
    found = False
    for i in task:
        if u_title == i["title"]:
            i["status"] = "Completed"
            print(f"Task '{u_title}' marked as completed.")
            found =True
            break
    if not found:
        print(f"Invalid title: {u_title}")
  
def delete_task(task):
    u_delete = input("Enter task title to delete: ")
    found = False
    for t in range(len(task)):
        if u_delete == task[t]["title"]:
            del task[t]
            print(f"Delete {u_delete} successfully!!")
            found = True
            break
    if not found:
        print(f"Invalid title: {u_delete}")
    
def show_tasks(task):
    print("All tasks")
    print("-------------")
    for show in task:
        print(f'Title:{show["title"]}\nDue Date: {show["due_date"]}\nStatus: {show["status"]}')
        print("------------------------------------")
    
    print("Completed Tasks")
    print("----------------")
    for c in task:
        if c["status"] == "Completed":
            print(f'Title:{c["title"]}\nDue Date: {c["due_date"]}\nStatus: {c["status"]}')
            print("----------------")
            
    print("Pending Tasks")
    print("----------------")
    for p in task:
        if p["status"] == "Pending":
            print(f'Title:{p["title"]}\nDue Date: {p["due_date"]}\nStatus: {p["status"]}')
            print("----------------")
        
def run():
    task = []
    name()
    main_menu(task)
    
run()