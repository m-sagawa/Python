# -*- coding: Shift-JIS -*-

print('�ۑ�6')

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

#�C���X�^���X��
smart = SmartPhone('1234', 'abcd')

smart.play_music()
smart.next_song()
smart.precious_song()
smart.stop_music()
smart.call()
smart.send_mail()