# -*- coding: Shift-JIS -*-

print('�ۑ�5')

class MP3Player:
	def play_music(self):
		print('���y���Đ����܂�')
	def next_song(self):
		print('���̋Ȃ��Đ����܂�')
	def precious_song(self):
		print('�O�̋Ȃ��Đ����܂�')
	def stop_music(self):
		print('���y���~�߂܂�')

class CellPhone:
	def __init__(self, tel_number, mail_address):
		self.tel_number = tel_number
		self.mail_address = mail_address
		print('�d�b�ԍ��F', tel_number)
		print('���[���A�h���X�F', mail_address)
		print('�C���X�^���X�����܂���2')
	def call(self):
		print(self.tel_number, '���甭�M���܂�')
	def send_mail(self):
		print(self.mail_address, '���瑗�M���܂�')

class SmartPhone(MP3Player, CellPhone):
	def print(self):
		print('�X�}�[�g�t�H��')