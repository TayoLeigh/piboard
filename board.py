import pygame
import time
import curses

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

down = pygame.mixer.Sound('down.wav')
left = pygame.mixer.Sound('left.wav')
right = pygame.mixer.Sound('right.wav')

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
screen.keypad(1)

screen.clear()

while True:
	screen.addstr(1, 0, "Ready to accept up, down, left or right to play sounds or q to quit!")
	screen.addstr(2, 0, "To get to a new console press Alt-F2")

	event = screen.getch()

	screen.clear()

	if event == ord('q'):
		break
	elif event == curses.KEY_UP:
		screen.addstr(0, 0, "You pressed up!")
		pygame.mixer.music.load("Sound1Awakening.mp3")
		pygame.mixer.music.play()
	elif event == curses.KEY_DOWN:
		screen.clear()
		screen.addstr(0, 0, "You pressed down!")
		pygame.mixer.music.load("Sound2ColdSpace.mp3")
		pygame.mixer.music.play()
	elif event == curses.KEY_LEFT:
		screen.clear()
		screen.addstr(0, 0, "You pressed left!")
		pygame.mixer.music.load("Sound3Trapped.mp3")
		pygame.mixer.music.play()
	elif event == curses.KEY_RIGHT:
		screen.clear()
		screen.addstr(0, 0, "You pressed right!")
		pygame.mixer.music.load("Sound4DoorSlam.mp3")
		pygame.mixer.music.play()
	elif event == ord('w'):
		screen.clear()
		screen.addstr(0, 0, "You pressed w!")
		pygame.mixer.music.load("Sound5CrackAppears.mp3")
		pygame.mixer.music.play()
	elif event == ord('a'):
		screen.clear()
		screen.addstr(0, 0, "You pressed a!")
		pygame.mixer.music.load("Sound6Idea.mp3")
		pygame.mixer.music.play()
	elif event == ord('s'):
		screen.clear()
		screen.addstr(0, 0, "You pressed s!")
		pygame.mixer.music.load("Sound7Unknown.mp3")
		pygame.mixer.music.play()
	elif event == ord('d'):
		screen.clear()
		screen.addstr(0, 0, "You pressed d!")
		pygame.mixer.music.load("Sound8Treasures.mp3")
		pygame.mixer.music.play()
	elif event == ord('f'):
		screen.clear()
		screen.addstr(0, 0, "You pressed f!")
		pygame.mixer.music.load("Sound12Transformed.mp3")
		pygame.mixer.music.play()
	elif event == ord('g'):
		screen.clear()
		screen.addstr(0, 0, "You pressed g!")
		pygame.mixer.music.load("Sound14Escaped.mp3")
		pygame.mixer.music.play()
		elif event == ord(' '):
		screen.clear()
		screen.addstr(0, 0, "You pressed space!")
		pygame.mixer.music.load("Sound9Chimes.mp3")
		pygame.mixer.music.play()
	else:
		screen.clear()
		screen.addstr(0, 0, "That key doesn't do anything!")

curses.endwin()
