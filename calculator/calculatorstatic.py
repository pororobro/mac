class CalculatorStatic(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

    @staticmethod
    def main():
        c = CalculatorStatic(int(input('첫 번쪠 수 입력하라')), int(input('두 번째 수 입력하라')))
        print(f'{c.first} + {c.second} = {c.add()}')
        print(f'{c.first} - {c.second} = {c.sub()}')
        print(f'{c.first} * {c.second} = {c.mul()}')
        print(f'{c.first} / {c.second} = {c.div()}')

CalculatorStatic.main()

