#!/usr/bin/env python

from os import popen
from re import split

f =popen('dir')
for eachLine in f:
    print split('\s\s+|\t', eachLine.strip())
f.close()