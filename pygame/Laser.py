import pygame
import math

class Laser(pygame.sprite.Sprite):
	def __init__(self, gs, angle):
		self.gs = gs
		self.img = pygame.image.load("deathstar/laser.png")
		self.img = pygame.transform.scale2x(self.img)
		self.rect = self.img.get_rect(center=self.gs.player.rect.center)
		self.angle = angle
		self.speed = 10

	def tick(self):
		self.rect = self.rect.move([self.speed*math.cos(self.angle),-self.speed*math.sin(self.angle)])