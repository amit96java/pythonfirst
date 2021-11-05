#when we use + , it call __add__ method in backend

class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1+other.m1
        m2=self.m2+other.m2
        #line 10 and 13 are same
        s3=Student(m1,m2)
        return s3

s1=Student(58,69)
s2=Student(48,52)

s3 = s1+s2

print(s3.m1)

