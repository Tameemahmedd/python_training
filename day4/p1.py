class MyClass:
    class_var=0
    count_of_objs=0

    def __init__(self)->None:
        self.var1=20
        self.var2=30
        MyClass.count_of_objs+=1

    @classmethod
    def class_method(cls):
        return cls.count_of_objs
    @staticmethod
    def static_method():
        return f"This is a static method {MyClass.count_of_objs}"
    def __str__(self)->str:
        return f"var1 ={self.var1}, var2= {self.var2},Count={MyClass.count_of_objs}"
    
print(MyClass.class_method())#o/p:0
print(MyClass.static_method())#o/p:This is a static method 0
obj1=MyClass()
print(obj1)
obj2=MyClass()
print(obj2)