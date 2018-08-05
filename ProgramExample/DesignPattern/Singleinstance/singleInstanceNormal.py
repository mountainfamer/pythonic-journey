#!/usr/bin/env python


class SingleInstance(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(SingleInstance, '_abc'):
            SingleInstance._abc = object.__new__(cls, *args, **kwargs)
        return SingleInstance._abc

    def __init__(self, name):
        self.name = name
        pass


class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            # orig = super(Singleton, cls)
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        # super(Singleton, self).__init__()
        self.name = name


a = MyClass('jack')
b = MyClass('Stone')
print a is b
