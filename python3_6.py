# -*- coding: Shift-JIS -*-

print('課題6')

from python3_5 import SmartPhone

#インスタンス化
smart = SmartPhone('1234', 'abcd')

smart.play_music()
smart.next_song()
smart.precious_song()
smart.stop_music()
smart.call()
smart.send_mail()