# -*- coding: Shift-JIS -*-

print('�ۑ�2')

class MP3Player:
	def __init__(self):
		print('�C���X�^���X�����܂���')
	def play_music(self):
		print('���y���Đ����܂�')
	def next_song(self):
		print('���̋Ȃ��Đ����܂�')
	def precious_song(self):
		print('�O�̋Ȃ��Đ����܂�')
	def stop_music(self):
		print('���y���~�߂܂�')

#�C���X�^���X��
play = MP3Player()

play.play_music()
play.next_song()
play.precious_song()
play.stop_music()