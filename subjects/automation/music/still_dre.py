# imports
from pyautogui import *
import time


# sounds

def treble1(wait, qtd):
	for times in range(0, qtd):
		time.sleep(wait)
		hotkey('s', 'f', 'j')


def treble2(wait, qtd):
	for times in range(0, qtd):
		time.sleep(wait)
		hotkey('a', 'f', 'j')


def treble3(wait, qtd):
	for times in range(0, qtd):
		time.sleep(wait)
		hotkey('a', 'f', 'h')


def bass1(qtd):
	for times in range(0, qtd):
		hotkey('6', 'e')


def bass2(qtd):
	for times in range(0, qtd):
		hotkey('7', 'r')


def bass3(qtd):
	for times in range(0, qtd):
		hotkey("3", "0")


# rythms

def main_rythm(reps):
	for i in range(0, reps):
		treble1(0.2, 8)
		treble2(0.2, 3)
		treble3(0.2, 5)


def main_bass1(reps):
	for i in range(0, reps):
		bass1(1)
		time.sleep(2)
		bass2(1)
		time.sleep(0.5)
		bass3(1)
		time.sleep(2)
		bass3(1)
		time.sleep(0.5)


# run

for s in range(0, 16):
	time.sleep(1)
	print(s)

main_bass1(2)
main_rythm(10)
