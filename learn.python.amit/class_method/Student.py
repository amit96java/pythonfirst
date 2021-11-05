class Students:
    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print("this is static method..")

s1=Students(5,8,4)
s2 = Students(5,9,7)

print(s1.avg())
print(Students.getSchool())
Students.info()

