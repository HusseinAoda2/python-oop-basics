class Main_Calc:
    def __init__(self, name):
        print('welcom in our calculator')

    def sum(self, x, y):
        print(x + y)

class Test:
    def sum(self, x , y):
        print('in Test')
        print(x + y)

class Calculator(Test): # parent super main
    def mul(self, x, y):
        print(x * y)

class Sicentific(Calculator, Main_Calc): # child subclass drived class
    def power(self, x, y):
        return x ** y
    
x = Sicentific('Hussein')
x.sum(5,6)
x.mul(2,3)
