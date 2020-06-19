# -*- coding: utf-8 -*-
# @Author: Kyle Song (fkilla8210@gmail.com)
# @Date:   2020-03-04 22:29:47
# @Last Modified by:   KyleSong

import base64


def main():

    string_data = "Hello Python"

    byte_data = convert_string_to_byte(string_data)
    b64_encoded = base64_encode(byte_data)
    print(b64_encoded)

    base64_data = "SGVsbG8gUHl0aG9u"

    byte_data = convert_string_to_byte(base64_data)
    b64_decoded = base64_decode(byte_data)
    print(b64_decoded)



def convert_string_to_byte(string_data):
    """ Encodes string into bytes as "base64.b64encode()" only takes byte-type data """
    return string_data.encode()

def convert_byte_to_string(byte_data):
    """ Decodes string to bytes """
    return byte_data.decode()

def base64_encode(byte_data):
    """ Encodes byte data to base64 """
    return base64.b64encode(byte_data)

def base64_decode(byte_data):
    """ Decodes byte data to base64 """
    return base64.b64decode(byte_data)


if __name__ == '__main__':
    main()
