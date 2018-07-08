#!/usr/bin/python
# coding: utf-8

'''
台阶问题或斐波那切，一只青蛙一次可以跳上１级台阶，也可以跳上２级台阶．求该青蛙跳上一个n级台阶共有多少种跳法；
使用递归方法；
'''



# 使用lambda方式，会使用到递归：

fib = lambda n: n if n <=2 else()

# 使用记忆方法，可以减少运算，提高效率，也会用到递归：


def mem(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@mem
def fib(i):
    if i < 2:
        return 1
    return fib(i-1) + fib(i-2)


def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return b

