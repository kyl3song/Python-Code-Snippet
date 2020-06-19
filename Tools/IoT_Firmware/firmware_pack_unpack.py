#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Kyle Song
# @Date:   2020-04-20 04:35:04
# @Last Modified by:   KyleSong
# @Last Modified time: 2020-04-23 14:04:58

import sys
import os

file_size = os.path.getsize(sys.argv[2])

class FirmwarePart:
	def __init__(self, name, offset, size):
		self.name = name
		self.offset = offset
		self.size = size

firmware_parts = [
	FirmwarePart("uimage_header1", 0x50000, 0x40),
	FirmwarePart("uimage_kernel1", 0x50040, 0x7FFFC0),
	FirmwarePart("uimage_header2", 0x850000, 0x40),
	FirmwarePart("uimage_kernel2", 0x850040, 0x50FFC0),
	FirmwarePart("squashfs_1", 0xD60000, 0x100000),
	FirmwarePart("squashfs_2", 0xE60000, 0x100000),
	FirmwarePart("squashfs_3", 0xF60000, 0x20000),
	FirmwarePart("squashfs_4", 0xF80000, file_size-0xF80000)
]

# Unpacks Firmware
if sys.argv[1] == "unpack":
	f = open(sys.argv[2], "rb")
	for part in firmware_parts:
		outfile = open(part.name, "wb")
		f.seek(part.offset)
		data = f.read(part.size)
		outfile.write(data)
		outfile.close()
		print(f"Wrote {part.name} - {hex(len(data))} bytes")
	f.close()

# Packs Firmware
elif sys.argv[1] == "pack":
	f = open(sys.argv[2], "wb")
	# Reasons for omit header part is to make custom header with the tool.
	for part in firmware_parts[1:]:
		i = open(part.name, "rb")
		data = i.read()
		f.write(data)
		padding = (part.size - len(data))
		print(f"Wrote {part.name} - {hex(len(data))} bytes")
		print(f"Padding: {hex(padding)}")
		f.write(b'\x00' * padding)
	f.close()
