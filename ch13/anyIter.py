#!/usr/bin/env python

class AnyIter(object):
    def __init__(self, data, safe=0):
        self.safe = safe
        self.iter = iter(data)
    
    def __iter__(self):
        return self

    def next(self, howmany=1):
        retval = []
        for eachItem in range(howmany):
            try:
                retval.append(self.iter.next())
            except StopIteration:
                if self.safe:
                    break
                else:
                    raise
        return retval

##############################################

a = AnyIter(range(10))
for j in range(1,5):
    print j, ':', a.next(j)

a = AnyIter(range(10), True)
print a.next(14)