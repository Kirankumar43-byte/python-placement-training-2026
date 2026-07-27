# Program 14: Multiple inheritance
class A:
    def method_a(self):
        print("A")

class B:
    def method_b(self):
        print("B")

class C(A, B):
    pass

C().method_a()
C().method_b()
