tasks=[]
def show_tasks():
       print("....MENU....")
       print("1.Add Task")
       print("2.show Task")
       print("3.Remove Tasks")
       print("4.Exit")
while True:
      show_tasks()
      choice=int(input("Enter your choice:"))
      if choice==1:
         num=int(input("Enter the number of tasks:"))
         for i in range(num):
            tasks.append(input("Enter task:"))
      elif choice==2:
         if not tasks:
            print("No tasks")
         else:
            i=1
            for task in tasks:
                 print(i,task)
                 i=i+1
      elif choice==3:
          if not tasks:
               print("No tasks")
          else:
               index=int(input("Enter the number of the task:"))
               remove=tasks.pop(index-1)
               i=1
               for task in tasks:
                   print(i,task)
                   i=i+1
      elif choice==4:
           print("EXIST")
           break
