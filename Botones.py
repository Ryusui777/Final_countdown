import pygame
import sys


class Button():
	def __init__(self, imagen, posicion, texto_entrada, fuente, color_base, hovering_color):
		self.imagen = imagen
		self.x_pos = posicion[0]
		self.y_pos = posicion[1]
		self.fuente = fuente
		self.color_base, self.hovering_color = color_base, hovering_color
		self.texto_entrada = texto_entrada
		self.texto = self.fuente.render(self.texto_entrada, True, self.color_base)
		if self.imagen is None:
			self.imagen = self.texto
		self.rect = self.imagen.get_rect(center=(self.x_pos, self.y_pos))
		self.texto_rect = self.texto.get_rect(center=(self.x_pos, self.y_pos))

	def actualizar(self, screen):
		if self.imagen is not None:
			screen.blit(self.imagen, self.rect)
		screen.blit(self.texto, self.texto_rect)

	def verificar_input(self, posicion):
		if posicion[0] in range(self.rect.left, self.rect.right) and posicion[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def cambiar_color(self, posicion):
		if self.verificar_input(posicion):
			self.texto = self.fuente.render(self.texto_entrada, True, self.hovering_color)
		else:
			self.texto = self.fuente.render(self.texto_entrada, True, self.color_base)

