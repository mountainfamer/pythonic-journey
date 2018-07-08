# !/usr/bin/env python


def single01(cls):
    instance = []
    print 'test: this is outside function'
    def wrap(*args, **kwargs):
        if not instance:
            # instance = (cls(*args, **kwargs))
            # instance = ''
            instance.append(cls(*args))
        # print type(instance)
        return instance
    return wrap


@single01
class A(object):

    def __init__(self, name):
        self.name = name


a = A('test')
b = A('test1')
print a is b

c = single01(A)
# print type(c)
d = c('sdfas')
# print d[0][0].name
