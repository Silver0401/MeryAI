import subprocess

x = "Microsoft Word"

subprocess.call(('/usr/bin/osascript', '-e',  "tell application "+ "\"" +x+ "\"" +" to quit",))


# audio2 = "close microsoft word"
# AudioList = audio2.split(" ")
# Grammar = []
# counter = 1

# for word in AudioList:
# 	if word == "close" or word == "Close":
# 		pass
# 	else:
# 		for letter in word:
# 			if word.index(letter) == 0 and counter == 1:
# 				x = letter.upper()
# 				Grammar.append(x)
# 				counter+=1
# 			elif word.index(letter) == 0 and counter == 2:
# 				x = letter.upper()
# 				Grammar.append("\\")
# 				Grammar.append(" ")
# 				Grammar.append(x)
# 			else:
# 				x = letter
# 				Grammar.append(x)


# CorrectedGrammar = "".join(Grammar)
# print (CorrectedGrammar)
		
# 		print (Grammar)

# 		filtered.append(Grammar[Grammar.index(word)])
		
# filteredWord = " ".join(filtered)
# #osascript -e 'quit app "Slack"'
# print (filteredWord)




# from gtts import gTTS
# import os

# def Response(text):

# 	TtS = gTTS(text = text, lang = "es", slow=False)
# 	#Text to Speech
# 	TtS.save("TestAudio.mp3")

# 	os.system("afplay TestAudio.mp3")

# Response("si?")

# import subprocess
# import os

# proc = subprocess.Popen("python3 AI.py",shell=True)

# x = input("thing")
# if x == "exit":
# 	pid = os.system("ps a | grep AI")
# 	os.system("kill -9 " + str(pid))





# import tkinter
# from PIL import Image, ImageTk, ImageSequence
# import PIL

# def animate(counter):
# 	canvas.itemconfig(photo, image=sequence[counter])
# 	if not animating:
# 		return
# 	window.after(33,lambda: animate((counter+1) % len(sequence)))


# animating = True
# thing = ImageTk.PhotoImage
# frames = ImageSequence.Iterator
# image = Image.open
# name = r'/Users/Ismael/Desktop/AI-Project/brain1.gif'
# sequence = list(map(thing, frames(image(name))))
# # sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('/Users/Ismael/Desktop/AI-Project/brain1.gif'))]

# window = tkinter.Tk()

# canvas = tkinter.Canvas(window, width=300, heigh=300)
# canvas.pack()

# photo = canvas.create_image(150,150, image=sequence[0])

# animate(0)

# window.mainloop()









# import graphics
# from graphics import *
# import time

# window = GraphWin("gameWindow", 200, 200)
# brain = Image(Point(25,100), 'brain1.gif')
# brain.draw(window)
# time.sleep(5)

# window.close()

