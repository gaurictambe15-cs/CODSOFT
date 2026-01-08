tasks=[]

def add_task():
    enter_task=input("Enter a task:")
    tasks.append({"Task":enter_task,"Status":"Pending"})
    print("Task added to the list!")
def view_task():
    if len(tasks)==0:
        print("No Tasks.")
    else:
        for i,t in enumerate(tasks,start=1):
            print(f"{i}.{t}")
def track_task():
    view_task()
    num=int(input("Enter task number to mark Done:"))
    tasks[num-1]["Status"]="Done"
    print("Task marked as Done!")
    count=0
    for t in tasks:
        if t["Status"]=="Done":
            count+=1
        print("You did",count,"tasks today!")
def remove_task():
    if len(tasks)==0:
        print("No tasks to remove.")
    view_task()
    rem_task=int(input("Enter task no. to remove from list:"))
    if 1<=rem_task<=len(tasks):
        removed=tasks.pop(rem_task-1)
        print("Task removed successfully!")
    else:
        print("Task doesn't exist.")
def exit_task():
    print("Thank You!")

while True:
    print("1.Add Task")
    print("2.View Task")
    print("3.Track Task")
    print("4.Remove Task")
    print("5.Exit")
    ch=int(input("Enter your choice number:"))
    if ch==1:
        add_task()
    elif ch==2:
        view_task()
    elif ch==3:
        track_task()
    elif ch==4:
        remove_task()
    elif ch==5:
        exit_task()  
        break 
    else:
        print("Invalid choice, Try again!")