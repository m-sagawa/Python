# -*- coding: Shift-JIS -*-

print('\n�ۑ�1')
print('11 + 3 = ', 11 + 3)
print('11 - 3 = ', 11 - 3)
print('11 * 3 = ', 11 * 3)
print('11 / 3 = ', 11 // 3, '�]��', 11 % 3)

print('\n�ۑ�2')
print('��ڂ̒l����͂��Ă�������')
num1 = int(input())
print('��ڂ̒l����͂��Ă�������')
num2 = int(input())
sum = num1 + num2
print('���v�F', sum)
print('���ρF', sum / 2)

print('\n�ۑ�3')
print('�̏d(kg)����͂��Ă�������')
weight = int(input())
print('�g��(cm)����͂��Ă�������')
height = int(input()) * 0.01
bmi = weight / (height ** 2)
#print('�̏d', weight)
#print('�g��',height)
#print('BMI', bmi)
if bmi < 18.5:
	result = '�₹'
elif bmi < 25:
	result = '�W��'
elif bmi < 30:
	result = '�얞'
else:
	result = '���x�얞'
print('���Ȃ��́u', result, '�v�ł��B')

print('\n�ۑ�4')
borrow = 250000
remain = borrow
repay = 30000
inte = 14.0 / 12
month = 1;
while remain != 0:
	remain = remain * (inte * 0.01 + 1)
	remain = remain - repay
	if remain < repay:
		print(month, '�����ځF�ԍϊz=', remain, '�~,�ԍϊ����B')
		remain = 0
	else:
		print(month, '�����ځF�ԍϊz=', repay, '�~,�c��', remain, '�~')
		month += 1
