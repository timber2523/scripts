#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
A script for 
"""

import os, sys
import zipfile

def toBytes(para):
  return bytes(para, 'utf-8')

def getPass(para):
  import getpass
  return getpass.getpass(para)

def decompress(filename):
  print("Archive: ", filename)
  file = zipfile.ZipFile(filename, "r")
  
  pwd = getPass("Password: ")

  for info in file.infolist():
    name = info.filename
    utf8name = name
    try:
      utf8name = utf8name.encode('cp437')
      utf8name = utf8name.decode('gbk')
    except:
      pass
    print("  extracting: " + utf8name)
    pathname = os.path.dirname(utf8name)
    if not os.path.exists(pathname) and pathname!= "":
      print("  creating: ", pathname)
      os.makedirs(pathname)
    data = file.read(name, pwd.encode('gbk'))
    if not os.path.exists(utf8name):
      fo = open(utf8name, "wb")
      fo.write(data)
      fo.close()
  file.close()
  print("")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    exit(1)
  for i in range(1, len(sys.argv)):
    decompress(sys.argv[i])
