# -*- coding: utf-8 -*-
# @Time : 8/5/2020 1:31 PM
# @Author : Peter yang


class Person:
    """
    关于这个类的描述：
    Attributes:
        count:int代表人的个数
    """
    count = 1

    def run(self, distance, step):
        """
        describe
        :param distance:int
        :param step: int
        :return: float
        """
        print("hello")
        return distance / step

help(Person)