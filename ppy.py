#!/usr/bin/python3
# -*- Coding: utf-8 -*-

import forbiddenfruit
from functools import reduce
from sys import *

def curseAll():
  for d in dir():
    f=eval(d)
    if callable(f):
      forbiddenfruit.curse(object, d, createFunc(f))

  for d in dir(__builtins__):
    f=getattr(__builtins__, d)
    if callable(f):
      forbiddenfruit.curse(object, d, createFunc(f))

def createFunc(f):
  def f_(self, *a):
    return f(self, *a)
  return f_

curseAll()

code=argv[1]
args=argv[2:len(argv)]

result=eval(code)

if isinstance(result, list):
  for a in result:
    a.print()
else:
  result.print()
  
