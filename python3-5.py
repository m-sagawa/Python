# -*- coding: Shift-JIS -*-

print('課題5')

class MP3Player:
	def play_music(self):
		print('音楽を再生します')
	def next_song(self):
		print('次の曲を再生します')
	def precious_song(self):
		print('前の曲を再生します')
	def stop_music(self):
		print('音楽を止めます')

class CellPhone:
	def __init__(self, tel_number, mail_address):
		self.tel_number = tel_number
		self.mail_address = mail_address
		print('電話番号：', tel_number)
		print('メールアドレス：', mail_address)
		print('インスタンス化しました2')
	def call(self):
		print(self.tel_number, 'から発信します')
	def send_mail(self):
		print(self.mail_address, 'から送信します')

class SmartPhone(MP3Player, CellPhone):
	def print(self):
		print('スマートフォン')