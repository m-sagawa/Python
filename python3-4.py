# -*- coding: Shift-JIS -*-

print('�ۑ�4')

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

#�C���X�^���X��
phone = CellPhone('1234', 'abcd')

phone.call()
phone.send_mail()