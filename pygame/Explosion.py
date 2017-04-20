import pygame
import math

class Explosion(pygame.sprite.Sprite):

	def __init__(self, gs):
		self.gs = gs
		self.img = pygame.image.load("deathstar/explosion/frames000a.png")
		self.rect = self.img.get_rect(center= [600,400])
		self.explode_countdown = 5
		self.frames_count = 0

	def tick(self):
		self.explode_countdown-=1

		if self.frames_count == 16:
			self.gs.spriteList.remove(self.gs.explosion)	
		else:		
			if self.explode_countdown == 0:
				self.frames_count += 1
				img_name = "deathstar/explosion/frames000a.png"
				if self.frames_count < 10:
					img_name = "deathstar/explosion/frames00" + str(self.frames_count) + "a.png"
				elif self.frames_count > 10:
					img_name = "deathstar/explosion/frames0" + str(self.frames_count) + "a.png"
				self.img = pygame.image.load(img_name)
				self.explode_countdown = 5

		