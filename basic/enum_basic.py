# -*- coding: utf-8 -*-
from enum import Enum, unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print('\n',Month.Jan)

@unique
class Month(Enum):
    Jan = 'January'
    Feb = 'February'
    Mar = 'March'
    Apr = 'April'
    May = 'May'
    Jun = 'June'
    Jul = 'July'
    Aug = 'August'
    Sep = 'September'
    Oct = 'October'
    Nov = 'November'
    Dec = 'December'

if __name__ == '__main__':
    print(Month.Jan,'____________',Month.Jan.name,"_______",Month.Jan.value)
    for name, member in Month.__members__.items():
        print(name, '=>', member, ',', member.value)

class User(Enum):
    name = '三疯'
    age = 19
    sex = '男'

name = User.name
age = User.age
sex = User.sex

print(name == name, name ==User.name)
print(name is name, name is User.name)
try:
    print('\n'.join('  ' + s.name for s in sorted(User)))
except TypeError as err:
    print(' Error : {}'.format(err))