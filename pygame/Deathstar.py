import pygame
import math
from Laser import Laser

class Deathstar(pygame.sprite.Sprite):
	def __init__(self, gs):
		self.gs = gs
		self.img = pygame.image.load("deathstar/deathstar.png")
		self.rect = self.img.get_rect()
		self.org_img = pygame.image.load("deathstar/deathstar.png")
		self.is_firing = False
		self.time_to_fire = 0
		self.mouse_x = 0
		self.mouse_y = 0


	def move(self, coord):
		self.rect = self.rect.move(coord)

	def rotate(self, degree):
		self.img = pygame.transform.rotate(self.org_img, degree)
		self.rect = self.img.get_rect(center=self.rect.center)

	def tick(self):
		if self.is_firing:

			angle = math.atan2(self.rect.centery-self.mouse_y, self.mouse_x-self.rect.centerx)
			laser = Laser(self.gs, angle)
			self.gs.spriteList.append(laser)
			self.gs.lasers.append(laser)
			self.time_to_fire+=1

			if self.time_to_fire == 30:
				self.is_firing = False
				self.time_to_fire = 0
		else:
			mousex, mousey = pygame.mouse.get_pos()
			playerx = self.rect.centerx
			playery = self.rect.centery
			degree = math.degrees(math.atan2(mousex-playerx, mousey-playery)) + 225
			self.rotate(degree)
