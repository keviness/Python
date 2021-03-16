# -*- coding: utf-8 -*-

from  enum import Enum, unique
@unique
class Gender(Enum):
    Male = 0
    Female = 1
class Student(object):
    def __init__(self, name, gender = 0):
        self.name = name
        if isinstance(gender, Gender):#gender是枚举成员
            self.gender = gender
        elif isinstance(gender, str):#gender是枚举成员名称
            if gender.capitalize() in Gender.__members__.keys():
                self.gender = Gender[gender.capitalize()]
            else:
                raise ValueError('%s is not a valid gender!' % gender)
        elif isinstance(gender, int):#gender是枚举成员的值
            if gender in Gender._value2member_map_:
                self.gender = Gender(gender)
            else:
                raise ValueError('%s is not a valid gender!' % gender)
        else:
            raise ValueError('%s is not a valid gender!' % gender)

#测试
alan = Student('Alan', 0)
bart = Student('Bart', Gender.Male)
cathy = Student('Cathy', 'female')
for i in [alan, bart, cathy]:
    print(i.gender)