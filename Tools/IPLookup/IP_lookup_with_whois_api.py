# -*- coding: utf-8 -*-
# @Author: Kyle Song
# @Date:   2020-06-16 17:21:15
# @Last Modified by:   Kyle Song
# @Last Modified time: 2020-06-19 09:19:05

import glob
import urllib.request
import json


""" 
Country Code Reference URL:
http://www.iegate.net/country_code.php

Whois API키는 개인적으로 직접 발급 받아야함(whois.kisa.or.kr)
"""

def main():
	log_path = '.\\**\\*.log'
	file_list = glob.glob(log_path, recursive=True)
	
	for file in file_list:
		slice_filename = file[2:]
		print(f"[+] Filename: {slice_filename} - Whois(whois.kisa.or.kr) Result:")

		fh = open(file, mode='r')
		
		while True:
			oneline = fh.readline()
			if oneline == '':
				break
			if ("ESTABLISHED" in oneline) and ("127.0.0.1" not in oneline):
				foreign_ip_port = oneline.split()[4]
				foreign_ip = foreign_ip_port.split(':')[0]
				foreign_port = foreign_ip_port.split(':')[1]

				whois_result = whois_api(foreign_ip)
				# Results
				# {"whois":{"query":"47.105.57.238","queryType":"IPv4","registry":"APNIC","countryCode":"CN"}}
				
				whois_result = json.loads(whois_result)
				print(f" [-] IP: {foreign_ip}, CountryCode: {whois_result['whois']['countryCode']}")
		fh.close()


def whois_api(ip):
	whois_key = 'you_need_to_request_private_api_key_from_whois.kisa.or.kr'
	query = "http://whois.kisa.or.kr/openapi/whois.jsp?query=" + ip + "&key="+ whois_key + "&answer=json";
	request = urllib.request.urlopen(query).read().decode("utf-8")
	return request


if __name__ == '__main__':
	main()