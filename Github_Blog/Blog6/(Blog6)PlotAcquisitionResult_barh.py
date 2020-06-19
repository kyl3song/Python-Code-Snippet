# -*- coding: utf-8 -*-
# @Author: Kyle Song (fkilla8210@gmail.com)
# @Date:   2020-04-23 14:16:51

import matplotlib.pyplot as plt
import numpy as np
import datetime

def main():
	#### 1. bar plot으로 나타낼 데이터 입력
	tools = ['EnCase', 'FTK 4.2', 'FTK 4.3', 'Falcon']
	# 0시간 ~ 6시간을 초로 환산(비교를 위함)
	_xticks = [0, 3600, 7200, 10800, 14400, 18000, 21600]
	yticks = ['Total Elasped', 'Verification', 'Imaging']
	_data = {'EnCase':['5:31:08', '2:38:42', '2:52:26'],
	        'FTK 4.2':['4:28:00', '2:07:29', '2:20:31'],
			'FTK 4.3':['3:59:00', '1:53:07', '2:06:53'],
			'Falcon':['3:50:29', '1:55:14', '1:55:15']}
	
	#### 2. matplotlib의 figure 및 axis 설정
	fig, ax = plt.subplots(1,1,figsize=(11,6)) # 1x1 figure matrix, 11x6 size
	colors = ['salmon', 'orange', 'cadetblue', 'skyblue']
	height = 0.15
	
	# Refine '_data' dictionary data (시간 데이터 초로 변환)
	data = refine_data_with_time_conversion(_data)

	#### 3. bar 그리기
	for i, tool in enumerate(tools):
		pos = compute_pos(yticks, height, i, tools)
		bar = ax.barh(pos, data[tool], height=height*0.95, label=tool, color=colors[i])
		# bar 값 출력
		present_width(ax, bar)
	
	#### 4. x축 세부설정
	# xticks 값을 먼저 그래프에 세팅한 다음 포매팅을 해서 원하는 포맷으로 변경이 가능함
	ax.set_xticks(_xticks)
	xlabels = [time_convert_to_str_time(x) for x in _xticks]
	ax.set_xticklabels(xlabels)
	ax.xaxis.set_tick_params(labelsize=10)
	ax.set_xlabel('Elasped Time', fontsize=14)

	#### 5. y축 세부설정
	ax.set_yticks(range(len(yticks)))
	ax.set_yticklabels(yticks, fontsize=10)	
	ax.set_ylabel('Items', fontsize=16)
	
	#### 6. 범례 나타내기
	# 범례를 그래프 상자 밖에 그리기 위해 상자크기를 조절
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
	ax.legend(loc='center left', bbox_to_anchor=(1,0.5), shadow=True, ncol=1)
	
	#### 7. 보조선(눈금선) 나타내기
	ax.set_axisbelow(True)
	ax.xaxis.grid(True, color='gray', linestyle='dashed', linewidth=0.5)
	
	#### 8. 그래프 저장하고 출력하기
	plt.title('Results of Acquisition Time', fontsize=15)
	plt.savefig('Result_barhplot.png', format='png', dpi=300)
	plt.show()
	
def compute_pos(yticks, height, i, tools):
	index = np.arange(len(yticks))
	n = len(tools)
	correction = i - 0.5*(n-1)
	return index + height * correction

def present_width(ax, bar):
	for rect in bar:
		width = rect.get_width()
		posx = width*1.01
		posy = rect.get_y()+rect.get_height()*0.5
		str_time = time_convert_to_str_time(width)
		ax.text(posx, posy, str_time, rotation=0, ha='left', va='center')

# _data 딕셔너리의 시간값을 모두 초로 환산한 뒤 동일한 딕셔너리 형태로 만듦
def refine_data_with_time_conversion(data):
	sec_data = {}
	for dict_key in data:
		_data_tmp_list = []
		time_data_list = data[dict_key]

		for str_time in time_data_list:
			hour, minute, second = map(int, str_time.split(':'))
			conv_to_sec = (hour * 3600) + (minute * 60) + second
			_data_tmp_list.append(conv_to_sec)

		# Dictionary에 요소 추가
		sec_data[dict_key] = _data_tmp_list
	return sec_data

# 시간 변환 부분(초 -> 시:분:초)
def time_convert_to_str_time(sec):
	""" Convert second time to '3:11:06' string format """
	# numpy.int32 type -> int type
	sec = int(sec)
	return str(datetime.timedelta(seconds=sec))

# 시간 변환 부분(시:분:초 -> 초)
def time_convert_to_sec(time_data_list):
	""" Convert '3:11:06' string format to Second time """
	sec_data = []
	for str_time in time_data_list:
		hour, minute, second = map(int, str_time.split(':'))
		conv_to_sec = (hour * 3600) + (minute * 60) + second
		sec_data.append(conv_to_sec)
	return sec_data


if __name__=='__main__':
	main()