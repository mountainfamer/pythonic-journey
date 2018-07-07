#!/usr/bin/python
# coding: utf-8

import abc

'''
代码分三部分:
1. 无面向对象的实现;
2. 面向对象的实现, 但无设计模式;
3. 使用设计模式;
通过对这三部分代码的对比,加深对设计模式的理解;

示例场景: 计算器可功能,根据"不同的运算符",计算结果;
'''

def operation():
    '''
    无面向对象的设计,由于思考过程简单,直接,刚开始看效率很高,动作很快;
    但从长远的需求变化以及维护场景看,需要修改全部原始代码;
    '''
    result = None
    int1 = input('Please input the operation unit1: ')   #input函数接受的是表达式,即如果是想输入字符串,要用引号包含字符串;
    int2 = input('Please input the operation unit2: ')
    op =  raw_input('Please input the operation with "+,-,*,/": ')   #raw_input函数接受的是字符串;
    if op == '+':
        result = int1 + int2
    elif op == '-':
        result = max(int1,int2) - min(int1, int2)
    elif op == '*':
        result = int1 * int2
    elif op == '/':
        result = int1/int2
    else:
        raise ValueError('Invalid operation string!')
    print 'The operation result is: ', result





class Operation(object):

    '''
    将操作抽象成对象,以面向对象的方式处理问题;
    #使用类方式处理,虽然将运算抽象成对象,但如果要增加运算或修改运算,则需要修改类,将会影响到其他已经交付额功能,因为所有功能在一起;
    '''
    result = int()

    def __init__(self, int1, int2, op):
        # item1 = input('Please input the operation nuit1: ')
        # item2 = input('Please input the operation nuit2: ')
        # 上边这种在初始化是通过键盘输入的方式,是不可取的,因为初始化的位置不可知,也就是要求键盘输入的时机不可知,程序在使用上有很大的弊端;
        self.item1 = int1
        self.item2 = int2
        self.opStr = op
        #python的实例变量不需要像java一样先声明,可以直接使用;

    def getResult(self):
        # Operation.result, 如果要引用类变量,就使用'类.',如果想引用实例变量,就使用''self.
        if self.opStr == '+':
            result = self.item2 + self.item1
        elif self.opStr == '-':
            result = max(self.item2, self.item1) - min(self.item2, self.item1)
        elif self.opStr == '*':
            result = self.item2 * self.item1
        elif self.opStr == '/':
            result = self.item2 / self.item1
        else:
            raise ValueError('Invalid operation string!')
        return result


#改造现有设计,使用继承与多态;
#创建操作抽象类:
class Operation_F(object): #添加_F后缀,以免与前面的oper类想区分;
    __metaclass__ = abc.ABCMeta  #定义抽象类;
    def __init__(self, int1, int2, op):
        self.item1 = int1
        self.item2 = int2
        self.opStr = op

    @abc.abstractmethod
    def getResult(self):
        return

    # def getResult(self):
    #     raise NotImplementedError
    #这里有两种定义抽象方法的方式,第一种是使用abc模块的抽象方法装饰器,第二种是抛一个非实例化的异常,只有子类重写这个方法后才能调用;

#创建具体的操作类:
class OperationAdd(Operation):
    def getResult(self):
        result = self.item1 + self.item2
        return result

class OperationSub(Operation):
    def getResult(self):
        result = max(self.item1, self.item2) - min(self.item2, self.item1)
        return result

class OperationMul(Operation):
    def getResult(self):
        result = self.item1 * self.item2
        return result

class OperationDiv(Operation):
    def getResult(self):
        result = max(self.item1, self.item2) / min(self.item2, self.item1)
        return result

#创建工厂方法类(使用类来创建对象):
class OPFactory(object):
    def __init__(self, int1, int2, op):
        self.int1 = int1
        self.int2 = int2
        self.op = op

    def createOperation(self):
        if self.op == '+':
            return OperationAdd(self.int1, self.int2, self.op)
        elif self.op == '-':
            return OperationSub(self.int1, self.int2, self.op)
        elif self.op == "*":
            return OperationMul(self.int1, self.int2, self.op)
        elif self.op == "/":
            return OperationDiv(self.int1, self.int2, self.op)
        else:
            raise ValueError('Invalid input operation.')



def client():
    # -----------------------------------------------------------
    # operation()
    #------------------------------------------------------------
    item1 = input('Please input the operation nuit1: ')
    item2 = input('Please input the operation nuit2: ')
    op = raw_input('Please input the operation with "+,-,*,/": ')
    # op1 = Operation(item1, item2, op)
    # print op1.getResult()
    # ------------------------------------------------------------
    # oper = Operation_F()
    oper = OPFactory(item1, item2, op).createOperation()
    print oper.getResult()
    # ------------------------------------------------------------
    '''
    基于简单的工厂方法实现后, 如果要修改某个操作,就修改对应的子类即可; 如果要增加一种操作,则需要增加操作子类,并在工厂中增加判断;
    问题: 
    '''

if __name__ == "__main__":
    client()