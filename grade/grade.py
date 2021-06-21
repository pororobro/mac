class Grade:
    def gradedata(self, kor, eng , mat):
        self.kor = kor
        self.eng = eng
        self.mat = mat

    def sum(self):
        return self.kor+self.eng+self.mat

    def avg(self):
        return self.sum() /3

if __name__ == '__main__':
    g = Grade()
    g.gradedata(80,96,88)
    print(g.sum())
    print(g.avg())


