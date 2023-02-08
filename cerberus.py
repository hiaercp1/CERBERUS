#!/usr/bin/env/ python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from getpass4 import getpass
import sys
import os
import argparse

fls = []

argument = sys.argv[1]

slsl = ""
sasa = ""
def Encryption():
    global slsl
    if len(sys.argv) > 2:
        slsl = sys.argv[2]
        password = slsl
        lop = len(password)
        if lop < 14:
            print("Password must be 16 characters or longer!!!")
        else:
                secondpassword = password.encode(encoding='utf-8')

                for file in fls:
                with open(file, "rb") as x:
                    contentoffile = x.read()
                    cipher = AES.new(secondpassword,AES.MODE_ECB)
                    econtent = cipher.encrypt(pad(contentoffile, AES.block_size))

                with open(file, "wb") as y:
                        y.write(econtent)
    else:
        password = getpass("password: ")
        secondpassword = password.encode(encoding='utf-8')
        for file in fls:
            with open(file, "rb") as x:
                contentoffile = x.read()
                cipher = AES.new(secondpassword,AES.MODE_ECB)
                econtent = cipher.encrypt(pad(contentoffile, AES.block_size))

            with open(file, "wb") as y:
                y.write(econtent)

def Decryption():
    global sasa
    if len(sys.argv) > 2:
        sasa = sys.argv[2]
        password = sasa
        lop = len(password)
        if lop < 14:
                print("Password must be 16 characters or longer!!!")
        else:
                secondpassword = password.encode(encoding='utf-8')
                for file in fls:
                with open(file, "rb") as x:
                    contentoffile = x.read()
                        cipher = AES.new(secondpassword,AES.MODE_ECB)
                        dcontent = unpad(cipher.decrypt(contentoffile), AES.block_size)
                with open(file, "wb") as y:
                        y.write(dcontent)

for argm in sys.argv[0:]:
    if os.path.isfile(argm):
        if argm != "this.py":
            fls.append(argm)
        else:
            continue

if argument == "-e" or argument == "-E":
    Encryption()

elif argument == "-d" or argument == "-D":
    Decryption()
else:
    this = input("do you want to encrypt or decrypt? [e/d] ")
    if this == "e":
        Encryption()
    elif this == "d":
        Decryption()
    else:
        print("ERROR")
