# -*- coding:utf-8 -*-
from public import *
from array import array
print(dir(array('B', [0xa1])))
print(dir(bytearray))


class Frame(bytearray):
    def __init__(self, source=None, encoding=None, errors='strict'):
        super(Frame, self).__init__(source, encoding, errors)



print(Frame([0x60, 0x29, 0xA1, 0x09, 0x06, 0x07, 0x60, 0x85, 0x74, 0x05, 0x08, 0x01, 0x01, 0xA6, 0x0A, 0x04,
                        0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x98, 0x00, 0xBE, 0x10, 0x04, 0x0E, 0x01, 0x00, 0x00,
                        0x00, 0x06, 0x5F, 0x1F, 0x04, 0x00, 0x00, 0x1F, 0x3F, 0xFF, 0xFD]))


