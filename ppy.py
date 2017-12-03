#!/usr/bin/python3
# -*- Coding: utf-8 -*-

from forbiddenfruit import curse
from functools import reduce
from sys import *

def _map(self, func):
  return [eval(func) for a in self]

def _reduce(self, func):
  return reduce(lambda a, b:eval(func), self)

def _filter(self, func):
  return [a for a in self if eval(func)]
 
def _print(self):
  print(self)

curse(list, 'print', _print)
curse(int, 'print', _print)
curse(str, 'print', _print)
curse(float, 'print', _print)
curse(list, 'map', _map)
curse(list, 'reduce', _reduce)
curse(list, 'filter', _filter)

code=argv[1]
args=argv[2:len(argv)]

result=eval(code)

if isinstaence(result, list):
  for a in result:
    a.print()
else:
  result.print()
  
