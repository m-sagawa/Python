# -*- coding: Shift-JIS -*-

print('課題2')

class MP3Player:
	def __init__(self):
		print('インスタンス化しました')
	def play_music(self):
		print('音楽を再生します')
	def next_song(self):
		print('次の曲を再生します')
	def precious_song(self):
		print('前の曲を再生します')
	def stop_music(self):
		print('音楽を止めます')

#インスタンス化
play = MP3Player()

play.play_music()
play.next_song()
play.precious_song()
play.stop_music()