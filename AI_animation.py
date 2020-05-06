#!/usr/local/bin/python3

import sys
import tkinter
from PIL import Image, ImageTk, ImageSequence
import time
import subprocess
import os

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=250, height=230, background="black")
sequence = [ImageTk.PhotoImage(img.resize(((300),(220))))
					for img in ImageSequence.Iterator(
							Image.open(
							r'/Users/Ismael/Desktop/AI-Project/brain1.gif'))]
image = canvas.create_image(125,125, image=sequence[0])


def Animate(counter):
	canvas.itemconfig(image, image=sequence[counter])
	root.after(20, lambda: Animate((counter+1) % len(sequence)))

def Exit():
	root.destroy()
	pid = os.system("ps a | grep AI")
	os.system("kill -9 " + str(pid))

	# sys.exit(0)

def Miscelaneous():
	canvas.pack(fill=tkinter.BOTH, expand=True)
	label = tkinter.Label(root, text="Mery [Isma's Personal AI]", background="black", foreground="white").pack(fill=tkinter.BOTH, expand=True, side="left")
	button = tkinter.Button(root, text="exit",font="bold", highlightbackground="black",command=Exit).pack(fill=tkinter.BOTH,side=tkinter.BOTTOM)

def Pop():
	Miscelaneous()
	Animate(1)
	root.call('wm', 'attributes', '.', '-topmost', '1')
	root.mainloop()



# subprocess.Popen("python3 AI.py &",shell=True)
Pop()





# time.sleep(3)
# root.destroy()
