import pygame
import sys

class Runner():
	def __init__(self):
		self.imagen = 
		self.position =


class Game():
	runners =  []
	__startline = 20
	__finishline = 620


	def __init__(self):
		self.__screen = pygame.display.set_mode((640,480))
		pygame.display.set_caption("Carrera de bichos")
		# cargar imagen de fondo para la pantalla
		self.__background = pygame.image.load("images/background.png")

		self.runner = pygame.image.load("images/smallball.png")

	def competir(self):
		gameover = False
		hayGanador = False
		x = 0

		#while not gameover:
		while True:
			# Comprobar eventos
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameover = True
					
			# Pintar en pantalla
			self.__screen.blit(self.background, (0,0))
			self.__screen.blit(self.runner,(x, 240))
			# Refrescar la pantalla
			pygame.display.flip()

			x += 3
			if x >= 630:
				hayGanador = True
		pygame.quit()
		sys.exit()

if __name__ == '__main__':
	pygame.init()
	g = Game()
	g.competir()



# import turtle
# import random

# class Carrera:
# 	corredores = []
# 	# en lugar de crear la tupla de posiciones iniciales, se puede crear una función que 
# 	# calcule las posiciones en función de la altura del circuito o del nº de corredores.
# 	__posStartY = (-30, -10, 10, 30)
# 	__colorTurtle = ('red', 'blue', 'green', 'orange')
	
# 	def __init__(self, width, height):
# 		# width y height serán las dimensiones de nuestro circuito/pantalla
# 		self.__screen = turtle.Screen()
# 		self.__screen.setup(width, height)
# 		self.__screen.bgcolor('lightgray')
# 		# calculamos la línea de salida poniéndola 20uds más avanzada del comienzo del circuito.
# 		self.__startline = (width/2 - 20) * -1 
# 		self.__finishline = width/2 - 20

# 		self.__createRunners()

# 	def __createRunners(self):
# 		for i in range(4):
# 			new_turtle = turtle.Turtle()
# 			new_turtle.shape('turtle')
# 			new_turtle.color(self.__colorTurtle[i])
# 			new_turtle.penup()
# 			new_turtle.setpos(self.__startline, self.__posStartY[i])
# 			self.corredores.append(new_turtle)

# 	def competir(self):
# 		# las tortugas irán avanzando por turnos, una distacia aleatoria
# 		hayGanador = False
# 		while not hayGanador:
# 			for tortuga in self.corredores:
# 				avance = random.randint(1,6)
# 				tortuga.forward(avance)
# 				if tortuga.position()[0] >= self.__finishline:
# 					hayGanador = True
# 					print("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
# 					break

# 		print('')



# if __name__=='__main__':
# 	carrera = Carrera(640, 480)
# 	carrera.competir()