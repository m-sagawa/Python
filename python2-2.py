# -*- coding: Shift-JIS -*-

print('�ۑ�2')


def leap(year):
	if year % 400 == 0:
		leap = '�[�N'
	elif year % 100 == 0:
		leap = '�[�N�ł͂Ȃ�'
	elif year % 4 == 0:
		leap = '�[�N'
	else:
		leap = '�[�N�ł͂Ȃ�'
	print(year, '�N��', leap, '�ł�')

print('���ׂ����N�𐼗�œ��͂��Ă�������')
year = int(input())

leap(year)

print('���݂̔N�𐼗�œ��͂��Ă�������')
now = int(input())

years = [now-1, now, now+1]
for year in years:
	leap(year)