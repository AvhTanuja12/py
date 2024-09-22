class maths():
     def add(self):
        self.a=int(input("enter first no:"))
        self.b=int(input("enter second no:"))
        self.c=self.a+self.b
        print("addition is:",self.c)

def sub(self):
        self.a=int(input("enter first no:"))
        self.b=int(input("enter second no:"))
        self.c=self.a-self.b
        print("subtaction is:",self.c)
def mul(self):
       self.a=int(input("enter first no:"))
       self.b=int(input("enter second no:"))
       self.c=self.a*self.b
       print("multplication is:",self.c)
    
def div(self):
        self.a=int(input("enter first no:"))
        self.b=int(input("enter second no:"))
        self.c=self.a/self.b
        print("division is:",self.c)
        
        obj=maths()
        while True:
            print("\n 1.addition")
            print("2.subtraction")
            print("3.multiplication")
            print("4.division")
            print("5.exit")

            ch=int(input("enter choice to perform, any operation"))
            if ch==1:
                obj.add()
            elif ch==2:
                obj.sub()
            elif ch==3:
                obj.mul()
            elif ch==4:
                obj.div()
            elif ch==5:
                print("\n program stop")
                break
            else:
                print("wrong choice!!")






        