# -*- coding: utf-8 -*-
# @Time : 8/7/2020 6:19 PM
# @Author : Peter yang
class check:
    def __init__(self,func):
        self.f=func
    def __call__(self, *args, **kwargs):
        print("登陆验证")
        self.f()

@check
def fashuoshuo():
    print("shuoshuo")

fashuoshuo()
