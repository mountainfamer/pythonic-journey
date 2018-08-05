#!/usr/bin/env python

class LeiFeng(object):
    # def __init__(self):
    #     print 'this is object __init__ method'


    def BuyRice(self):
        print 'This is LeiFeng BuyRice'
        pass

    def Sweep(self):
        print 'This is LeiFeng Sweep'
        pass

    def Wash(self):
        print 'This is LeiFeng Wash'
        pass

class Undergraduate(LeiFeng):
    # def __init__(self):
    #     print 'this is Undergraduate __init__ method'

    def BuyRice(self):
        print 'This is Undergraduate BuyRice'


class Volunteer(LeiFeng):
    pass

class IFactory(object):

    def CreateLeiFeng(self):
        pass

class UndergraduateFactory(IFactory):

    def CreateLeiFeng(self):
        return Undergraduate()

class VolunteerFactory(IFactory):

    def CreateLeiFeng(self):
        return Volunteer()



if __name__ == '__main__':
    student = UndergraduateFactory().CreateLeiFeng()
    volunteer = VolunteerFactory().CreateLeiFeng()
    student.BuyRice()
    student.Sweep()
    volunteer.Wash()