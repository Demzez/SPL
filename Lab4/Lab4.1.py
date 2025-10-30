class Example:
    static_var1 = 10
    static_var2 = 20

    def __init__(self):
        self.dynamic_var1 = 5
        self.dynamic_var2 = 3

    def method1(self):
        var = 15
        print(var)

    def method2(self):
        return self.static_var1 + self.static_var2

    def method3(self):
        return self.dynamic_var1 ** self.dynamic_var2

obj = Example()
obj.method1()
print(obj.method2())
print(obj.method3())
print(obj.static_var1)