# -*- coding: utf-8 -*-
# @Author: Kyle Song
# @Date:   2020-03-02 11:21:10
# @Last Modified by:   KyleSong

import hashlib
import os

def main():
    """ Generating Hash values """

    file = "file.jpg"

    with open(file, mode='rb') as fh:
        data = fh.read()

    filesize = get_file_size(file)

    md5_hash = generate_md5_hash(data)
    sha1_hash = generate_sha1_hash(data)
    sha256_hash = generate_sha256_hash(data)

    print(f"[+] Filename: {file} ({filesize} bytes)")
    print("[-] MD5:", md5_hash, filesize)
    print("[-] SHA-1:", sha1_hash)
    print("[-] SHA-256:", sha256_hash)


def generate_md5_hash(data):
    """ Generating MD5 Hash values """
    return hashlib.md5(data).hexdigest()


def generate_sha1_hash(data):
    """ Generating SHA-1 Hash values """
    return hashlib.sha1(data).hexdigest()


def generate_sha256_hash(data):
    """ Generating SHA-256 Hash values """
    return hashlib.sha256(data).hexdigest()


def get_file_size(file):
    """ Calculates Size of File """
    return os.path.getsize(file)


if __name__ == '__main__':
    main()
