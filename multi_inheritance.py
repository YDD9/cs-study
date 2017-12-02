class A(object):
    def go(self):
        print("go A go!")
    def stop(self):
        print("stop A stop!")
    def pause(self):
        raise Exception("Not Implemented")

class B(A):
    def go(self):
        super(B, self).go()
        print("go B go!")

class C(A):
    def go(self):
        super(C, self).go()
        print("go C go!")
    def stop(self):
        super(C, self).stop()
        print("stop C stop!")

class D(B,C):
    def go(self):
        super(D, self).go()
        print("go D go!")
    def stop(self):
        super(D, self).stop()
        print("stop D stop!")
    def pause(self):
        print("wait D wait!")

class E(B,C): pass


if __name__=='__main__':
    a = A()
    b = B()
    c = C()
    d = D()
    e = E()

    # explanation of super() with multi parent class: 
    # simple rule: depth first and left to right without duplication
    # https://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
    # d.stop():  
    # backward search: D B(A) C(A)
    # del duplication: D B C A
    # output in order: A,C,B,D

    a.go()
    b.go()
    c.go()
    d.go()
    e.go()

    a.stop()
    b.stop()
    c.stop()
    d.stop()
    e.stop()

    a.pause()
    b.pause()
    c.pause()
    d.pause()
    e.pause()

