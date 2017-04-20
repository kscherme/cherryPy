import pygame
import math

class Laser(pygame.sprite.Sprite):
	def __init__(self, gs):
		self.img = pygame.image.load("deathstar/laser.png")
		self.rect = self.img.get_rect()

	def shoot(self, pos):
		print(pos)

	def tick(self):
		pass