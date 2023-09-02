class parent:
    def func1(self):
        print("this is function 1")
class child1(parent):
    def func2(self):
        print("this is function 2")
class child2(parent):
    def func3(self):
        print("this is the function3")
class child3(child1,parent):
    def func4(self):
        print("this is the function4")
r=child3()
r.func1()
r.func2()
r.func4()
