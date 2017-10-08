#!/usr/bin/env python

from time import time, ctime, sleep

class TimeWrapeMe(object):

    def __init__(self, obj):
        self.__data = obj
        self.__ctime = self.__mtime = \
            self.__atime = time()
    
    def set(self, obj):
        self.__data = obj
        self.__mtime = self.__atime = time()

    def get(self):
        self.__atime = time()
        return self.__data

    def gettimeval(self, t_type):
        if not isinstance(t_type, str) or \
                t_type[0] not in 'cma':
            raise TypeError, \
                "argument of 'c', 'm', or 'a' req'd"
        return eval('self._%s__%stime' % \
            (self.__class__.__name__, t_type[0]))
    
    def gettimestr(self, t_type):
        return ctime(self.gettimeval(t_type))

    def __repr__(self):
        self.__atime = time()
        return `self.__data`

    def __str__(self):
        self.__atime = time()
        return str(self.__data)

    def __getattr__(self, attr):
        self.__atime = time()
        return getattr(self.__data, attr)

########################################

wrappedComplex = TimeWrapeMe(3.5+4.2j)
print wrappedComplex
print wrappedComplex.real
print wrappedComplex.imag
print wrappedComplex.conjugate()
print wrappedComplex.get()

wrappedList = TimeWrapeMe([123, 'foo', 45.67])
wrappedList.append('bar')
wrappedList.append('123')
print wrappedList
wrappedList.pop()
print wrappedList
realList = wrappedList.get()
print realList[3]

timeWrapeMeObj = TimeWrapeMe(932)
print timeWrapeMeObj.gettimestr('c')
print timeWrapeMeObj.gettimestr('m')
print timeWrapeMeObj.gettimestr('a')

timeWrapeMeObj.set('time is up!')
print timeWrapeMeObj
print timeWrapeMeObj.gettimestr('m')