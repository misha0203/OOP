class Calculator:
     def __init__(self, num):
         self.num = num
class SUM(Calculator):
    def __add__(self, other):
        return self.num + other

class SUB(Calculator):
    def __sub__(self, other):
        return self.num - other

class MUL(Calculator):
    def __mul__(self, other):
        return self.num * other

class DIV(Calculator):
    def __truediv__(self, other):
        return self.num / other

class inherit(SUM, SUB, MUL, DIV):
    ...


result1 = inherit(2) + 8
result2 = inherit(3) - 6
result3 = inherit(5) * 8
result4 = inherit(100) / 2
print(result1)
print(result2)
print(result3)
print(result4)