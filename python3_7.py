# -*- coding: Shift-JIS -*-

print('課題7')

from abc import ABCMeta, abstractclassmethod

class Vehicle(metaclass=ABCMeta):
	def __init__(self, power, do):
		self.power = power
		self.do = do

	@abstractclassmethod
	def take(self):
		pass

class Car(Vehicle):
	def take(self):
		print('自動車は' + self.power + 'を' + self.do + 'と進みます。')

class Bicycle(Vehicle):
	def take(self):
		print('自転車は' + self.power + 'を' + self.do + 'と進みます。')

class Ship(Vehicle):
	def take(self):
		print('船は' + self.power + 'を' + self.do + 'と進みます。')

class Airplane(Vehicle):
	def take(self):
		print('飛行機は' + self.power + 'を' + self.do + 'と進みます。')

car = Car('アクセル', '踏む')
bicycle = Bicycle('ペダル', '漕ぐ')
ship = Ship('スクリュー', '回す')
airplane = Airplane('プロペラ', '回す')

car.take()
bicycle.take()
ship.take()
airplane.take()

