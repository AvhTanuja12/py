q=[]
def insert():
    size=int(input("enter the size of queue :"))
    if len(q)==size:
        print("Queue is full!!!")
    else:
        element=input("eneter the element :")
        q.append(element)
        print(element,"is added to queue !")

        def delete():
            if len(q)==0:
                print("Queue uis empty!!!")
            else:
                e=q.pop(0)
                print("element are removed :",e)

                def display():
                    print(q)
                    size=int(input("enter the size of queue :"))
                    while True:
                        print("\n select the operations :1.Insert 2.Delete 3.Display 4.Quit")

                        choice=int(input())
                        if choice==1:
                            insert()
                        elif choice==2:
                            delete()
                        elif choice==3:
                            display()
                        elif choice==4:
                            break
                        else:
                            print("Invalid option!!!")