# -*- coding: utf-8 -*-
# Author: Kyle Song

import string

'''
[ASCII CODE]
a-z : 97~122
A-Z : 65~90
91 ~ 96: Special Character ('[', '\', ']', '^', '_', '`')
'''

text = "hello"

alphabet_lower = list(string.ascii_lowercase)

for i in range(1, len(alphabet_lower)+1):

    strText = []

    for char in text:
        intVal = ord(char)
        intVal += i

        if intVal > ord('z'):
            intVal -= 26

        strText.append(chr(intVal))

    print(f"Ceaser Cipher Round {i}, Result: {''.join(strText)}")
