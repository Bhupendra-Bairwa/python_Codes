class Test:
    def fn(self):
        print("hello")

    def G(self):
        print("hi")


class T(Test):
    def G(self):
        print("hh")
        super().G()


t1=T()
t1.G()

        
