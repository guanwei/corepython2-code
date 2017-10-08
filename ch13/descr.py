#!/usr/bin/env python

import os
import pickle

class FileDescr(object):
    saved = []

    def __init__(self, name):
        self.name = name
    
    def __get__(self, obj, typ=None):
        if self.name not in FileDescr.saved:
            raise AttributeError, \
                "%r used before assignment" % self.name
    
        try:
            f = open(self.name, 'r')
            val = pickle.load(f)
            f.close()
            return val
        except (pickle.UnpicklingError, IOError,
                EOFError, AttributeError,
                ImportError, IndentationError), e:
            raise AttributeError, \
                "could not read %r: %s" % (self.name, str(e))

    def __set__(self, obj, val):
        try:
            f = open(self.name, 'w')
            pickle.dump(val, f)
            FileDescr.saved.append(self.name)
        except (IOError, TypeError, pickle.PicklingError), e:
            raise AttributeError, \
                "could not pickle %r: %s" % (self.name, str(e))
        finally:
            f.close()
    
    def __delete__(self, obj):
        try:
            os.unlink(self.name)
            FileDescr.saved.remove(self.name)
        except (OSError, ValueError), e:
            pass