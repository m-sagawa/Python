# -*- coding: Shift-JIS -*-

print('課題3')

class CellPhone:
	def __init__(self, tel_number, mail_address):
		self.tel_number = tel_number
		self.mail_address = mail_address
		print('電話番号：', tel_number)
		print('メールアドレス：', mail_address)
		print('インスタンス化しました')
	def call(self):
		print(self.tel_number, 'から発信します')
	def send_mail(self):
		print(self.mail_address, 'から送信します')