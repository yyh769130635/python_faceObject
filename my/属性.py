# -*- coding: utf-8 -*-
# @Time : 8/4/2020 7:56 PM
# @Author : Peter yang


class Money:
    age = 18
    count = 1
    num = 66
class Test:
    pass
print(Money.age)
print(Money.__dict__)

one = Money()
one.__class__ =Test
print(one.__class__)