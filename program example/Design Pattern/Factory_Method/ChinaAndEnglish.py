#!/usr/bin/env python
#coding:utf-8
'''
Factory Method Example
'''

class Getter(object):
    def get(self,msgid):
        return str(msgid)

class ChinaGetter(Getter):

    def __init__(self):
        self.trans = dict(dog=u'小狗', cat=u'小猫')

    def get(self,msgid):
        try:
            return self.trans[msgid]
        except KeyError:
            return str(msgid)

class EnglishGetter(Getter):
    pass

class Japan(Getter):
    pass

class IFactory(Getter):
    languages = dict(English=EnglishGetter,
                     China=ChinaGetter,
                     Japaner=Japan,
                     )
    @staticmethod
    def createGetter(language):
        return IFactory.languages[language]()

if __name__ == '__main__':
    chinaGetter = IFactory.createGetter('China')
    englishGetter = IFactory.createGetter('English')
    japanGetter = IFactory.createGetter('Japaner')
    print chinaGetter.get('dog')
    print englishGetter.get('dog')
    print japanGetter.get('cat')
