# -*- coding: utf-8 -*-
# @Author: Kyle Song
# @Date:   2020-04-23 09:33:30
# @Last Modified by:   Kyle Song
# @Last Modified time: 2020-04-23 10:40:00

import sys
import os

def main():
	print("[+] Search Started !!")
	cwd = os.getcwd()
	get_db_size(cwd)
	print("[+] Search Finished !!")


def get_db_size(dirname):
	for root, dirs, files in os.walk(dirname):
		for file in files:
			# Filter only file extension
			file_ext = file.split('.')[-1]
			if ('edb' in file_ext) or ('rdb' in file_ext):
				size = os.path.getsize(file)
				print(f"{file} ({size:,} bytes)")
	

if __name__ == '__main__':
	print(f"[+] Load {os.path.basename(sys.argv[0])}")
	main()