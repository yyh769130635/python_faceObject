# -*- coding: utf-8 -*-
# @Time : 8/6/2020 6:14 PM
# @Author : Peter yang
def add(x,y):
    print('和为：%d'%(x+y))

class A:
    def __init__(self,xx,yy):
        self.x=xx
        self.y=yy
    def add(self):
        print("x和y的和为：%d"%(self.x+self.y))