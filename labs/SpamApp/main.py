"""
Simple GUI with configuration for a spam
"""

# imports
import pyautogui as pt
import time
from tkinter import *


# main class
class App:
	def __init__(self):
		# window
		self.main = Tk()

		# window configuration
		self.main.title('Spammer - By Aquaman Do Tietê')

		# title
		self.title_lb = Label(self.main, text='O que vc vai fazer com esse spammer? Só não me culpe...')

		# instructions
		self.instructions_lb = Label(self.main,
		                             text='O tempo de espera antes de começar a escrever é o tempo que você deve selecionar a caixa de texto que o spammer começará a escrevern\nTempo de espera entre cada mensagem recomendado:\nWhatsApp: 0.1 s\nDiscord: 0.5')

		# message
		self.lb_1 = Label(self.main, text='Mensagem:')
		self.entry_1 = Entry(self.main)

		self.lb_2 = Label(self.main, text='Número de mensagens:')
		self.entry_2 = Entry(self.main)

		# waits
		self.lb_3 = Label(self.main, text='Tempo de espera antes de começar a escrever (segundos):')
		self.entry_3 = Entry(self.main)

		self.lb_4 = Label(self.main, text='Tempo de espera entre cada mensagem (segundos): ')
		self.entry_4 = Entry(self.main)

		# buttons
		self.execute_bt = Button(self.main, text='Iniciar', command=self.execute)

		# executing the program

		self.show()

		self.main.mainloop()

	def show(self):
		# packing
		self.title_lb.pack()
		self.instructions_lb.pack()
		self.lb_1.pack()
		self.entry_1.pack()
		self.lb_2.pack()
		self.entry_2.pack()
		self.lb_3.pack()
		self.entry_3.pack()
		self.lb_4.pack()
		self.entry_4.pack()
		self.execute_bt.pack()

	def execute(self):

		time.sleep(int(self.entry_3.get()))

		for i in range(1, int(self.entry_2.get())):
			pt.typewrite(self.entry_1.get())

			wait = self.entry_4.get().replace(',', '.')

			print(wait)

			time.sleep(float(wait))

			pt.press('enter')



if __name__ == '__main__':
	App()
