class anna():
    def __init__(self):
        self.name1="jeeva"
class papa(anna):
    def __init__(self):
        self.name2="arul"
        anna.__init__(self)
class relation(papa):
    def __init__(self):
        self.hobby="art"
        papa.__init__(self)
    def  display(self):
        print("anna:",self.name1)
        print("papa:",self.name2)
        print("relation:",self.hobby)
obj=relation()
obj.display()
