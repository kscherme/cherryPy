import pygame
import math
from Deathstar import Deathstar
from Laser import Laser
from Planet import Planet


class GameSpace:
	def main(self):

		# Initialize screen
		pygame.init()
		self.size = self.width, self.height = 640, 470
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)

		# Initialize objects and clock
		self.spriteList = []
		self.player = Deathstar(self)
		self.planet = Planet(self)
		self.spriteList.append(self.player)
		self.spriteList.append(self.planet)
		self.lasers = []
		self.clock = pygame.time.Clock()
		self.explosion = 0


		while 1:
			self.clock.tick(60)
			for event in pygame.event.get():

				# If an arrow key is pressed
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.player.move([-5,0])
					if event.key == pygame.K_RIGHT:
						self.player.move([5,0])
					if event.key == pygame.K_UP:
						self.player.move([0,-5])
					if event.key == pygame.K_DOWN:
						self.player.move([0,5])

				# If the user clicks out of the game
				if event.type == pygame.QUIT:
					exit(0)


				# If the user shoots a laser
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.player.is_firing == False:
						self.player.is_firing = True
						self.player.mouse_x, self.player.mouse_y = pygame.mouse.get_pos()

			for sprite in self.spriteList:
				sprite.tick()

			self.screen.fill(self.black)

			for sprite in reversed(self.spriteList):
				self.screen.blit(sprite.img, sprite.rect)


			pygame.display.flip()