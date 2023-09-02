class a:
    def __init__(self):
        print("parent of b and c")
class b(a):
    def __init__(self):
        print("b child class of A")
class c(a):
    def __init__(self):
        print("c child class of a")
obj1=c()
obj2=b()
        
