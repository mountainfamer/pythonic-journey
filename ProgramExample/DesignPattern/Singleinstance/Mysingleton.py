# /usr/bin/env python
# coding: utf-8

class My_Singleton_Module(object):
    _count = 0
    def __init__(self):
        My_Singleton_Module._count+=1
        print My_Singleton_Module._count
    def foo(self):
        pass
my_singleton_module = My_Singleton_Module()

class My_Singleton_new(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(My_Singleton_new, cls).__new__(cls, *args, **kw)
        return cls._instance
class My_Singleton_class_new(My_Singleton_new):
    pass
