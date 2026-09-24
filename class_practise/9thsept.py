"""Multiple Inheritance in Python"""

class A:
    def process(self):
        print("Processing in class A")

class B(A):
    def process(self):
        print("Processing in class B")

class C(A):
    def process(self):
        print("Processing in class C")

class D(B, C):
    def process(self):
        print("Processing in class D")
        super().process()  # Calls the process method of the next class in MRO

d = D()
d.process()  # Output: Processing in class D
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

"""A -> B -> C -> D"""
class A:
    def process(self):
        print("Processing in class A")


class B(A):
    def process(self):
        print("Processing in class B")
        super().process()


class C(B):
    def process(self):
        print("Processing in class C")
        super().process()


class D(C):
    def process(self):
        print("Processing in class D")
        super().process()


d = D()
d.process()
