# -*- coding: Shift-JIS -*-

print('\n�ۑ�1')
def time(speed, distance):
	time = distance / speed
	return time
print('���x����͂��Ă�������')
speed = int(input())
print('��������͂��Ă�������')
distance = int(input())
print('���Ԃ�', time(speed, distance), '�ł�')

print('\n�ۑ�2')
print('���ׂ����N�𐼗�œ��͂��Ă�������')
year = int(input())
def leap(year):
	if year / 4 == 0:
		if year / 400 == 0:
			leap = '�[�N'
		elif year / 100 == 0:
			leap = '�[�N�ł͂Ȃ�'
		else:
			leap = '�[�N'
	else:
		leap = '�[�N�ł͂Ȃ�'
	return leap
print(year, '�N��', leap(year), '�ł�')
print('���݂̔N�𐼗�œ��͂��Ă�������')
now = int(input())
last = now - 1
next = now + 1
print('���N��', leap(year=last), '�ł�')
print('���N��', leap(year=now), '�ł�')
print('���N��', leap(year=next), '�ł�')

print('\n�ۑ�3')
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