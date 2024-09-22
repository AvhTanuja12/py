class country():
    def acceptcountry(self):
        self.name(input("eneter country name"))

        def displaycountry(self):
            print("enter name of country",self.name)

            class state(country):
                def acceptstate(self):
                    self.state(input("enter state name"))

                    def displaystate():
                        print("enter state name",self.state)
                        c=state()
                        c.acceptcountry()
                        c.displaycountry()
                        c.displaystate()
                        c.acceptstate()