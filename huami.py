#!/usr/bin/env python
# Huami CLI Version.
# Author: Tao Yang (ninehills.github.com)
# Origin: https://code.google.com/p/flower-password/
# Usage: huami.py KEY
import sys
import hmac

STR1 = "snow"
STR2 = "kise"
STR3 = "sunlovesnow1990090127xykab"

def toBytes(s):
	return bytes(s, 'latin-1')

def huami(password, key):
    # md5one, md5two, md5three
    # hmac.new(key, msg)
    md5one = hmac.new(toBytes(key), toBytes(password)).hexdigest()
    md5two = hmac.new(toBytes(STR1), toBytes(md5one)).hexdigest()
    md5three = hmac.new(toBytes(STR2), toBytes(md5one)).hexdigest()
    rule = list(md5three)
    source = list(md5two)
    for i in range(0, 32):
        if rule[i] in STR3:
            source[i] = source[i].upper()
    #code32 = ''.join(source)
    if source[0].isdigit():
        code16 = "K" + "".join(source[1:16])
    else:
        code16 = "".join(source[0:16])
    return code16

if __name__ == "__main__":
    if len(sys.argv) != 2:
        help_str = "Usage: %s KEY\n" % (sys.argv[0])
        sys.stderr.write(help_str)
        sys.exit(1)
    import getpass
    password = getpass.getpass("Password:")
    print(huami(password, sys.argv[1]))
