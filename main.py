#!/usr/bin/env python3

import pyqrcode


hex_string="8C 78 C5 33 CB 2C 8D E6 3C 17 FA 21 5D 75 5A C9 30 2A 03 9B C0 89 3D C6 30 2A 03 9B C0 89 3D C6 30 2A 03 9B C0 89 3D C6 30 2A 03 9B C0 89 3D C6 3C ED 3D 6E 54 18 05 6D 9B 01 6F 98 65 A1 5E E3 41 07 F2 BB 98 E5 92 94 28 A1 C1 1B 30 9E D6 C3 95 54 37 10 2B E0 03 3B 9E 8F 93 CA AE A2 D1 CC F0 5A 0E 71 EE A7 AE 5F 3B 40 CF 59 D6 D2 6C 28 6C 4D 9F 5A C2 39 46 B9"
bytes_object = bytes.fromhex(hex_string)
codetest=pyqrcode.create(bytes_object, error='L', mode='binary')
print(codetest.terminal())
#get canvas from gui and print this on it ffs

