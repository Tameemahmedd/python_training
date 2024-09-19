class A:
    pass
class B(A):
    pass
class c(B):
    pass

obj=A()
obj2=B()
obj3=c()
print(type(obj))#o/p:<class '__main__.A'>
print(isinstance(obj,B))#o/p:False
print(isinstance(obj2,B))#o/p:True
print(isinstance(obj3,B))#o/p:True
print(issubclass(A,B))#o/p:False #issubclass(Derived,base class)
