# !/usr/bin/python
# coding: utf-8

import abc
import re
'''
商场打折问题:
1. 简单的面向过程的实现方式;
2. 面向对象的实现, 但无设计模式;
3. 使用设计模式;
通过对这三部分代码的对比,加深对设计模式的理解;

示例场景: 计算器可功能,根据"不同的运算符",计算结果;
'''

#面向过程的实现方式:
def CountCost():
    '''
    简单的面向过程的逻辑,就是从输入端读入折扣, 价格, 商品数量这些信息,然后通过条件判断打折,计算出结果;
    实现比较简单,弊端是如果有新的打折出现,整个代码都要变动;
    '''


    total = 0
    while True:
        range = raw_input('Please input range of "8z, 7z, 5z, input q/Q quite": ')  # 模拟图形界面的选择输入,此处接收字符串;

        if range == "8z":
            disCount = 0.8
        elif range == "7z":
            disCount = 0.7
        elif range == "5z":
            disCount = 0.5
        elif range.upper() == 'Q':
            break
        elif range == "":
            disCount = 1
        else:
            raise ValueError('input error of range! ')

        price = input('Please input price: ')
        num = input('please input num of goods: ')

        totalPrice = price * num * disCount
        total += totalPrice
        print 'current cost: ',totalPrice
        print 'total cost: ', total


#---------------------------------------------------------
#使用简单工厂, 计算花费;
class CountComputeAstr(object):
    def __init__(self):
        self.total = 0
    @abc.abstractmethod
    def countCast(self):
        return

#具体的折扣算法:

#普通方式:
class CountNormal(CountComputeAstr):
    def countCast(self, monery):
        return monery
#打折方式:
class CountRebate(CountComputeAstr):
    def __init__(self, rebate):
        # super.__init__(self)
        self.rebate = int(re.search(r'(\d+)', rebate).groups()[0]) * 0.1   # n*0.1 与 n/10结果是不一样的;  

    def countCast(self, monery):
        return monery * self.rebate

#返利方式:
class CountReturn(CountComputeAstr):
    def __init__(self, moneyCondition, moneyReturn):
        # super.__init__(self)
        self.moneyCondition = moneyCondition
        self.moneyReturn = moneyReturn

    def countCast(self, monery):
        result = monery
        if result > self.moneyCondition:
            return result - result/self.moneyCondition * self.moneyReturn

#工厂方法:
class Factory(object):
    countAlgorithm = None
    @staticmethod                       #简单工厂有两种表现形式: 可以定义成可以将工厂方法定义成静态方法,或非静态方法;
    def getCountAlgorithm(condition):
        if condition == "":
            Factory.countAlgorithm = CountNormal()
        elif condition in '5z8z7z':
            Factory.countAlgorithm = CountRebate(condition)
        elif re.match(r'\d+-\d+', condition):
            moneyCountidiion, moneyReturn = re.search(r'(\d+)-(\d+)', condition).groups()
            Factory.countAlgorithm = CountReturn(int(moneyCountidiion), int(moneyReturn))
        return Factory.countAlgorithm

#---------------------------------------------------------
#使用策略模式, 计算花费;
class Context(object):
    def __init__(self, algorithm):
        self.algorithm = algorithm
    def getResult(self, monkey):
        return self.algorithm.countCast(monkey)

#客户端:
def client():
    #-----------------------------------------
    #CountCost()
    # -----------------------------------------
    # while True:
    #     range = raw_input('Please input range of "8z, 7z, 5z, input q/Q quite": ')  #输入优惠条件
    #     if range.upper()=='Q':
    #         break
    #     # factory = Factory()
    #     # countAlgorithm = factory.getCountAlgorithm(range)    #简单工厂通过类来产生算法类;
    #     countAlgorithm = Factory.getCountAlgorithm(range)      #简单工厂通过类来产生算法类;
    #     price = input('Please input price: ')
    #     num = input('please input num of goods: ')
    #     print 'current cost: ', countAlgorithm.countCast(price * num)
    # -----------------------------------------
    while True:
        try:
            range = raw_input('Please input range of "8z, 7z, 5z, input q/Q quite": ')  #输入优惠条件
    
            if range.upper()=='Q':
                break

            algorithm = None  #策略模式就是维护一个统一的算法,且需要的时候可以替换成其他的算法;
    
            if range == "":
                algorithm = Context(CountNormal())
            elif range in '5z8z7z':
                algorithm = Context(CountRebate(range))
            elif re.match(r'\d+-\d+', range):
                moneyCountidiion, moneyReturn = re.search(r'(\d+)-(\d+)', range).groups()
                algorithm = Context(CountReturn(moneyCountidiion, moneyReturn))
            else:
                raise ValueError('error input!')
        except ValueError as e:
            print
            continue
        price = input('Please input price: ')
        num = input('please input num of goods: ')
        print 'current cost: ', algorithm.getResult(price * num)

if __name__ == '__main__':
    client()