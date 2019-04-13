#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys
import zipfile

def toBytes(para):
  return bytes(para, 'utf-8')

def getPass(para):
  import getpass
  return getpass.getpass(para)

print(":: Processing File " + sys.argv[1])
file = zipfile.ZipFile(sys.argv[1], "r")

ret = input("Require password? [y/N]")

if ret == '':
  flag = 0
else:
  if ret[0] != 'y' and ret[0] != 'Y' and ret[0] != 'N' and ret[0] != 'n':
    exit(1)
  flag = (ret[0] == 'y') or (ret[0] == 'Y')
  if flag:
    pwd = getPass("Password: ")

for info in file.infolist():
  name = info.filename
  utf8name = name
  try:
    utf8name = utf8name.encode('cp437')
    utf8name = utf8name.decode('gbk')
  except:
    pass
  print("Extracting " + utf8name)
  pathname = os.path.dirname(utf8name)
  if not os.path.exists(pathname) and pathname!= "":
    os.makedirs(pathname)
  if flag:
    data = file.read(name, pwd.encode('gbk'))
  else:
    data = file.read(name)
  if not os.path.exists(utf8name):
    fo = open(utf8name, "wb")
    fo.write(data)
    fo.close
file.close()
