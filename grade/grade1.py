class Grade(object):
    def __init__(self, k, e, m):
        self.k = k
        self.e = e
        self.m = m

    def sum(self):
        return self.k + self.e + self.m

    def avg(self):
        return self.sum()/3

    @staticmethod
    def main():
        g = Grade(int(input('국어')),int(input('영어')),int(input('수학')))
        print(f'점수의 총합은 {g.sum()}입니다')
        print(f'점수의 평균은 {g.avg()}입니다')

Grade.main()


