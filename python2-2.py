# -*- coding: Shift-JIS -*-

print('課題2')


def leap(year):
	if year % 400 == 0:
		leap = '閏年'
	elif year % 100 == 0:
		leap = '閏年ではない'
	elif year % 4 == 0:
		leap = '閏年'
	else:
		leap = '閏年ではない'
	print(year, '年は', leap, 'です')

print('調べたい年を西暦で入力してください')
year = int(input())

leap(year)

print('現在の年を西暦で入力してください')
now = int(input())

years = [now-1, now, now+1]
for year in years:
	leap(year)