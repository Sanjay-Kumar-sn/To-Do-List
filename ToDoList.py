def add_task(task):
    tasks.append(task)
    print(tasks)
    
def remove_task(task):
    for t in tasks:
        if t[0] == task:
            tasks.remove(t)
            print("Task", task, "is removed")
            return

    print("Task not found")
    
def display(tasks):
    print(tasks)
def completed(completed_task):
    for t in tasks:
        if t[0] == completed_task:
            tasks.remove(t)
            print("Task is completed")
            return

    print("Task not found")
tasks=[]
while True:
    try:
        print("1.Add Task")
        print("2.Remove Task")
        print("3.Display Task")
        print("4.Completed Task")
        print("5.Exit")
        print("Enter your choice(1/2/3/4):")
        ch=int(input())
        match ch:
            
            case 1:
                task = input("Enter Task:")
                priority = input("Enter Priority:")
                add_task([task, priority])
            case 2:
                task=input("Enter Task:")
                remove_task(task)
                
            case 3:
                display(tasks)
            case 4:
                completed_task=input("Enter Task:")
                
                completed(completed_task)
            case 5:
                print("Do you want to exit:")
                ex=input()
                break
            case _:
                print("Invalid option")
                break
    except ValueError:
        print("Please enter a valid input")
    except TypeError:
        print("Type Error")
    except Exception as e:
        print("Error=",e)
