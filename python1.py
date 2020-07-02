# -*- coding: Shift-JIS -*-

print('\n課題1')
print('11 + 3 = ', 11 + 3)
print('11 - 3 = ', 11 - 3)
print('11 * 3 = ', 11 * 3)
print('11 / 3 = ', 11 // 3, '余り', 11 % 3)

print('\n課題2')
print('一つ目の値を入力してください')
num1 = int(input())
print('二つ目の値を入力してください')
num2 = int(input())
sum = num1 + num2
print('合計：', sum)
print('平均：', sum / 2)

print('\n課題3')
print('体重(kg)を入力してください')
weight = int(input())
print('身長(cm)を入力してください')
height = int(input()) * 0.01
bmi = weight / (height ** 2)
#print('体重', weight)
#print('身長',height)
#print('BMI', bmi)
if bmi < 18.5:
	result = 'やせ'
elif bmi < 25:
	result = '標準'
elif bmi < 30:
	result = '肥満'
else:
	result = '高度肥満'
print('あなたは「', result, '」です。')

print('\n課題4')
borrow = 250000
remain = borrow
repay = 30000
inte = 14.0 / 12
month = 1;
while remain != 0:
	remain = remain * (inte * 0.01 + 1)
	remain = remain - repay
	if remain < repay:
		print(month, 'か月目：返済額=', remain, '円,返済完了。')
		remain = 0
	else:
		print(month, 'か月目：返済額=', repay, '円,残り', remain, '円')
		month += 1
