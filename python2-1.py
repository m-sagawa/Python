# -*- coding: Shift-JIS -*-

print('�ۑ�1')

def time(speed, distance):
	time = distance / speed
	return time

print('���x����͂��Ă�������')
speed = int(input())

print('��������͂��Ă�������')
distance = int(input())

print('���Ԃ�', time(speed, distance), '�ł�')