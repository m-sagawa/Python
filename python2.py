# -*- coding: Shift-JIS -*-

print('\n課題1')
def time(speed, distance):
	time = distance / speed
	return time
print('速度を入力してください')
speed = int(input())
print('距離を入力してください')
distance = int(input())
print('時間は', time(speed, distance), 'です')

print('\n課題2')
print('調べたい年を西暦で入力してください')
year = int(input())
def leap(year):
	if year / 4 == 0:
		if year / 400 == 0:
			leap = '閏年'
		elif year / 100 == 0:
			leap = '閏年ではない'
		else:
			leap = '閏年'
	else:
		leap = '閏年ではない'
	return leap
print(year, '年は', leap(year), 'です')
print('現在の年を西暦で入力してください')
now = int(input())
last = now - 1
next = now + 1
print('去年は', leap(year=last), 'です')
print('今年は', leap(year=now), 'です')
print('来年は', leap(year=next), 'です')

print('\n課題3')
from PIL import Image, ImageFilter
im = Image.open('summer.jpg')
width, height = im.size
#print(width)
#print(height)
import math
g = math.gcd(width, height)
w = width / g
h = height / g
print(w, ' : ', h)