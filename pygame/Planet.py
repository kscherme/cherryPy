import pygame
import math
from Explosion import Explosion

class Planet(pygame.sprite.Sprite):

	def __init__(self, gs):
		self.gs = gs
		self.img = pygame.image.load("deathstar/globe.png")
		self.rect = self.img.get_rect()
		self.rect.centerx = 640
		self.rect.centery = 470
		self.hitpoints = 30
		self.hit = False

	def tick(self):
		for sprite in self.gs.lasers:
			if( self.rect.colliderect(sprite.rect) == True):
				self.hit = True
				break

		if self.hit:
			self.hitpoints-=1
			self.hit = False

		if self.hitpoints == 0:
			self.gs.spriteList.remove(self.gs.planet)
			self.gs.explosion = Explosion(self.gs)
			self.gs.spriteList.append(self.gs.explosion)
