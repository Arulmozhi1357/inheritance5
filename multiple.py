class a:
    def __init__(self):
        print("hi kutty")
class b:
    def __init__(self):
        print("how are you")
class c(a,b):
    def __init__(self):
        print("from c")
        a.__init__(self)
        b.__init__(self)
        
c=c()
