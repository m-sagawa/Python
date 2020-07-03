# -*- coding: Shift-JIS -*-

print('課題1')

def time(speed, distance):
	time = distance / speed
	return time

print('速度を入力してください')
speed = int(input())

print('距離を入力してください')
distance = int(input())

print('時間は', time(speed, distance), 'です')