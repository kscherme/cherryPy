import pygame
import math

class GameSpace:
	def main(self):
		pygame.init()
		self.size = self.width, self.height = 640, 470
		self.black = 0, 0, 0
		self.screen = pygame.display.set_mode(self.size)

		self.player = Player("deathstar/deathstar.png")
		self.clock = pygame.time.Clock()


		while 1:
			self.clock.tick(60)
			for event in pygame.event.get():
				#print(event)
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.player.move([-5,0])
					if event.key == pygame.K_RIGHT:
						self.player.move([5,0])
					if event.key == pygame.K_UP:
						self.player.move([0,-5])
					if event.key == pygame.K_DOWN:
						self.player.move([0,5])

				if event.type == pygame.QUIT:
					exit(0)

				if event.type == pygame.MOUSEMOTION:
					#self.player.rotate(180)
				#self.rect= self.rect.move([1,1])
				#self.player.move([1,1])
				#rad = event.pos[0]/event.pos[1]
					mousex, mousey = event.pos
					playerx = self.player.rect.centerx
					playery = self.player.rect.centery
					print(playerx)
					print(playery)
				# degree = math.degrees(math.atan(mousex/mousey))
				# self.player.rotate(degree)
			#self.player.tick()
			self.screen.fill(self.black)
			self.screen.blit(self.player.img, self.player.rect)

			pygame.display.flip()

class Player:
	def __init__(self, img_link):
		self.img = pygame.image.load(img_link)
		self.rect = self.img.get_rect()


	def move(self, coord):
		self.rect = self.rect.move(coord)

	def rotate(self, degree):
		starting_rect = self.rect
		rot_img = pygame.transform.rotate(self.img, degree)
		new_rect = starting_rect.copy()
		new_rect.center = rot_img.get_rect().center
		self.img = rot_img.subsurface(new_rect).copy()







if __name__ == "__main__":
	gs = GameSpace()
	gs.main()
