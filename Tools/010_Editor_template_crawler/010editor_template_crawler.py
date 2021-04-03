# -*- coding: utf-8 -*-
# @Author: Kyle Song (kyl3s0n9@gmail.com)
# @Date:   2020-12-24 11:13:15
# @Last Modified by:   KyleSong

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import os

def main():
	base_url = 'https://www.sweetscape.com/010editor/repository/templates/'
	target_url = 'https://www.sweetscape.com/010editor/repository/'
	base_dir = 'C:\\Users\\KyleSong\\Desktop\\010editor_template'

	print(f'[+] JOB START..!!')

	html = urlopen(base_url)
	soup = BeautifulSoup(html, "html.parser")
	tags = soup.find_all("td")
	cnt = 0
	#tag = soup.select('a')
	#tag.find_all()
	
	for tag in tags:
		if (tag.a != None) and ('.bt' in tag.a.text):
			# fname: ../files/010.bt
			fname_tmp = tag.a['href']
			fname = fname_tmp.split('/')[-1]
			output_file = os.path.join(base_dir, fname)
			download_url = target_url + fname_tmp[3:]

			# download_url: https://www.sweetscape.com/010editor/repository/files/7ZIP.bt
			with urlopen(download_url) as f:
				data = f.read()

			with open(output_file, 'wb') as wf:
				print('='*100)
				print(f'[*] Download URL: {download_url}')
				print(f'[*] FILENAME: {os.path.basename(output_file)}')
				wf.write(data)
			cnt += 1

	print('='*100)
	print(f'[+] TOTAL FILE COUNT: {cnt}')
	print(f'[+] JOB FINISHED..!!')


if __name__ == '__main__':
    main()
