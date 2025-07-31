todoli = []

def additem(task):
        todoli.append(task)
        print(f"Added task:{task}")
         
def removeitem(task):
    if task in todoli:
        todoli.remove(task)
        print(f"removed task:{task}")
    else:
        print(f"Task {task} not found in the list.")

def showitem():
    if todoli:
         print("\nYour to do list:")
         for i ,task in enumerate(todoli,1):
             print(f"{i}.{task}")
    else:
          print("Your to do list is empty.")
       

while True:

    print("\nMenu:")
    print("1.Add task")
    print("2.Remove task")
    print("3.Show all tasks")
    print("4.Exit")

    choice = input("Enter your choice(1-4):")

    if choice == '1':
       task = input("Enter task to add:")
       additem(task)
   
    elif choice == '2':
       task = input("Enter task to remove:")
       removeitem(task)

    elif choice == '3':
       showitem()

    elif choice == '4':
      print("Exiting To-Do list.GoodBye!")
      break

    else:
     print("Invalid Choice.Please try again")

       



