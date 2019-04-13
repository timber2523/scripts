#!/usr/bin/python

import sys
import hmac
import hashlib
import base64

str1 = "timber"
str2 = "core"
str3 = "region"

def toBytes(para):
  return bytes(para, 'latin-1')

def getPass(para):
  import getpass
  return getpass.getpass(para)

def keyGen(key, password):
  md5one = hmac.new(toBytes(key), toBytes(password)).hexdigest()
  base64one = base64.b64encode(toBytes(md5one))
  sha384one = hmac.new(base64one, toBytes(str1), hashlib.sha384).hexdigest()
  sha256one = hmac.new(base64one, toBytes(str2), hashlib.sha256).hexdigest()
  pak = hmac.new(toBytes(sha384one), toBytes(sha256one), hashlib.sha512).hexdigest()
  rule = str(base64.b64encode(toBytes(sha384one)), 'latin-1')
  source = str(base64.b64encode(toBytes(sha256one)), 'latin-1')
  return 'K' + rule[10:15] + pak[0:4] + source[6:12]

if __name__ == "__main__":
  if len(sys.argv) != 2:
    help_str = "Usage: %s KEY\n" % (sys.argv[0])
    sys.stderr.write(help_str)
    sys.exit(1)
  password = getPass("Password: ")
  print(keyGen(sys.argv[1], password))
