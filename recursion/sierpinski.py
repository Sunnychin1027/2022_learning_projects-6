"""
File: sierpinski.py
Name: Sunny
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This program will recursively prints triangle in triangle.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: this count the layer user enter
	:param length: the initial triangle length
	:param upper_left_x: the initial upper left x value
	:param upper_left_y: the initial upper left x value
	:return: return when the order count to zero
	"""
	if order == 0:
		return
	else:
		line = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		line2 = GLine(upper_left_x, upper_left_y, upper_left_x + length / 2, upper_left_y + length * 0.866)
		line3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length / 2, upper_left_y + length * 0.866)
		window.add(line)
		window.add(line2)
		window.add(line3)
		pause(5)
		# Draw line
		sierpinski_triangle(order-1, length/2, upper_left_x+1/4*length, upper_left_y+length*0.433)
		# Draw line2
		sierpinski_triangle(order-1, length/2, upper_left_x+1/2*length, upper_left_y)
		# Draw line3
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)


if __name__ == '__main__':
	main()