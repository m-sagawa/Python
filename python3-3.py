# -*- coding: Shift-JIS -*-

print('�ۑ�3')

class CellPhone:
	def __init__(self, tel_number, mail_address):
		self.tel_number = tel_number
		self.mail_address = mail_address
		print('�d�b�ԍ��F', tel_number)
		print('���[���A�h���X�F', mail_address)
		print('�C���X�^���X�����܂���')
	def call(self):
		print(self.tel_number, '���甭�M���܂�')
	def send_mail(self):
		print(self.mail_address, '���瑗�M���܂�')