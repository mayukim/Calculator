a = input('정수 입력:')
b = input('기호 입력:')
c = input('정수 입력:')

class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result
    
class UpgradeCal(Calculator):
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self):
        if test1.second == 0 :
            return 0
        else:
            return self.first / self.second
        
test1 = UpgradeCal(int(a), int(c))

if b == '+':
    print(test1.add())
elif b == '-':
    print(test1.sub())
elif b == '*':
    print(test1.pow())
elif b == '/':
    print(test1.div())

