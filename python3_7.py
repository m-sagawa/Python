# -*- coding: Shift-JIS -*-

print('�ۑ�7')

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
		print('�����Ԃ�' + self.power + '��' + self.do + '�Ɛi�݂܂��B')

class Bicycle(Vehicle):
	def take(self):
		print('���]�Ԃ�' + self.power + '��' + self.do + '�Ɛi�݂܂��B')

class Ship(Vehicle):
	def take(self):
		print('�D��' + self.power + '��' + self.do + '�Ɛi�݂܂��B')

class Airplane(Vehicle):
	def take(self):
		print('��s�@��' + self.power + '��' + self.do + '�Ɛi�݂܂��B')

car = Car('�A�N�Z��', '����')
bicycle = Bicycle('�y�_��', '����')
ship = Ship('�X�N�����[', '��')
airplane = Airplane('�v���y��', '��')

car.take()
bicycle.take()
ship.take()
airplane.take()

