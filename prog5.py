class MyDate:
    def accept(self):
        self.d=int(input("Enter day:"))
        self.m=int(input("Enter month:"))
        self.y=int(input("Enter year:"))
def display(self):
                if self.d>31:
                    raise ValueError("Day value is greater than 31")
                if self.m>12:
                    raise ValueError("Month value is greater than 12")
                    print("Date is:",self.d,"-",self.m,"=",self.y)
obj=MyDate()
obj.accpet()
obj.display()

