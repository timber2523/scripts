#!/usr/bin/python

import sys
import hmac
import hashlib

STR1 = "forest"
STR2 = "timber"
STR3 = "usingnamespacestd2678658726183681273"

def keygen(password, key):
    # hmac.new(key, msg)
    md5one = hmac.new(bytes(key, 'latin-1'), bytes(password, 'latin-1'), hashlib.sha512).hexdigest()
    md5two = hmac.new(bytes(STR1, 'latin-1'), bytes(md5one, 'latin-1'), hashlib.sha256).hexdigest()
    md5three = hmac.new(bytes(STR2, 'latin-1'), bytes(md5one, 'latin-1'), hashlib.md5).hexdigest()
    rule = list(md5three)
    source = list(md5two)
    for i in range(0, 32):
        if rule[i] in STR3:
            source[i] = source[i].upper()
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
    print(keygen(password, sys.argv[1]))
