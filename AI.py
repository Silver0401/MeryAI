#!/usr/local/bin/python3

import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import time
import tkinter
from PIL import Image, ImageTk, ImageSequence
import sys
import subprocess

class Mery(object):
	def __init__(self):

		self.language = "en"

		warnings.filterwarnings("ignore")

		# self.root = tkinter.Tk()
		# self.canvas = tkinter.Canvas(self.root, width=250, height=230, background="black")
		# self.sequence = [ImageTk.PhotoImage(img.resize(((300),(220))))
		# 					for img in ImageSequence.Iterator(
		# 							Image.open(
		# 							r'/Users/Ismael/Desktop/AI-Project/brain1.gif'))]
		# self.image = self.canvas.create_image(125,125, image=self.sequence[0])

	def Listener(self):

		AudioReader = sr.Recognizer()

		with sr.Microphone() as source:
			audio = AudioReader.listen(source)
			# prindasht ("I'm Listening")

			data = ""
			try:
				data = AudioReader.recognize_google(audio) 
				print ("you said: " + data)

			except sr.UnknownValueError:
				print ("waiting for audio...")

			except sr.RequestError as e:
				print ("Service error from Google Speech Recognition, check internet connection " + e)

			return data

	def CallBack(self):
		WakeWords = ["mary", "hey mary", "mery", "married", "marrieds", "he married", "ameri", "amari", "marry"]
		MeryHeard = False

		text = OneTrueMery.Listener() 
		text = text.lower()
		for phrase in WakeWords:
			if phrase in text:
				MeryHeard = True

		if MeryHeard:

			OneTrueMery.Response("Yes Sir?",self.language)

			return "succes"

	def Response(self,text,language):

		TtS = gTTS(text = text, lang = language, slow=False)
		#Text to Speech

		TtS.save("TextToResponse.mp3")

		os.system("afplay TextToResponse.mp3")

		# subprocess.call(('/usr/bin/osascript', '-e',  'tell application "Music" to pause',))

	def getDate(self):

		month_names = [

		"January", "February", "March"
		, "April", "May", "June", "July"
		, "August", "September", "October"
		, "November", "December"]


		ordinal_numbers = [

		"1st", "2nd", "3rd", "4rd", "5th", "6th", "7th", "8th", "9th", "10th",
		"11th", "12th", "13th", "14th", "15th", "16th", "17th", "18th", "19th", "20th",
		"21st", "22nd", "23rd", "24th", "25th", "26th", "27th", "28th", "29th", "30th", "31st"]

		Now = datetime.datetime.now()

		My_day = datetime.datetime.today()

		Weekday = calendar.day_name[My_day.weekday()]

		Month_num = Now.month

		Day_num = Now.day

		return "Today is: " + Weekday + " " + month_names[Month_num - 1] + " the " + ordinal_numbers[Day_num - 1] + "."

	def getInfo(self, audio2):
		try:
			sentence = audio2.split(" ")
			filtered = []
			for word in sentence:
				if word == "look" or word == "up" or word == "search":
					pass
				else:
					filtered.append(sentence[sentence.index(word)])

			filteredWord = " ".join(filtered)
			wikInfo = wikipedia.summary(filteredWord, sentences=2)
			OneTrueMery.Response("Here's what I found: " + wikInfo,self.language)


		except:
			OneTrueMery.Response("I didn't understand what you want me to search",self.language)

	def OpenApp(self, audio2):

		try:
			AudioList = audio2.split(" ")
			Grammar = []
			counter = 1

			for word in AudioList:
				if word == "open" or word == "Open":
					pass
				else:
					for letter in word:
						if word.index(letter) == 0 and counter == 1:
							x = letter.upper()
							Grammar.append(x)
							counter+=1
						elif word.index(letter) == 0 and counter == 2:
							x = letter.upper()
							Grammar.append("\\")
							Grammar.append(" ")
							Grammar.append(x)
						else:
							x = letter
							Grammar.append(x)


			CorrectedGrammar = "".join(Grammar)
			os.system("open -a " + CorrectedGrammar)
			OneTrueMery.Response("Opening " + CorrectedGrammar,self.language)
		except:
			OneTrueMery.Response("I didn't recognize the application.",self.language)

	def CloseApp(self, audio2):
		try:
			AudioList = audio2.split(" ")
			Grammar = []
			counter = 1

			for word in AudioList:
				if word == "close" or word == "Close":
					pass
				else:
					for letter in word:
						if word.index(letter) == 0 and counter == 1:
							x = letter.upper()
							Grammar.append(x)
							counter+=1
						elif word.index(letter) == 0 and counter == 2:
							x = letter.upper()
							Grammar.append(" ")
							Grammar.append(x)
						else:
							x = letter
							Grammar.append(x)


			CorrectedGrammar = "".join(Grammar)
			# AppPID = os.system("pgrep " + CorrectedGrammar)
			OneTrueMery.Response("Closing " + CorrectedGrammar,self.language)
			subprocess.call(('/usr/bin/osascript', '-e',  "tell application "+ "\"" +CorrectedGrammar+ "\"" +" to quit",))
			# os.system("pkill -x " + CorrectedGrammar)
			
		except:
			OneTrueMery.Response("I didn't recognize the application.",self.language)

	def AI(self):

		while True:

			audio2 = OneTrueMery.Listener()

			if "open" in audio2:
				OneTrueMery.OpenApp(audio2)
			
			if "look up" in audio2 or "search" in audio2:
				OneTrueMery.getInfo(audio2)

			if "play" in audio2 or "play music" in audio2 or "music please" in audio2:
				subprocess.call(('/usr/bin/osascript', '-e',  'tell application "Music" to play',))

			if "date" in audio2:
				OneTrueMery.Response(OneTrueMery.getDate(),self.language)

			if "stop music" in audio2 or "stop" in audio2 or "silence" in audio2 or  "quiet" in audio2:
				subprocess.call(('/usr/bin/osascript', '-e',  'tell application "Music" to pause',))

			if "next" in audio2 or "track" in audio2 or "next song" in audio2 or "next track" in audio2:
				subprocess.call(('/usr/bin/osascript', '-e',  'tell application "Music" to next track',))

			if "previous"  in audio2 or "previous song" in audio2 or "previous track" in audio2:
				subprocess.call(('/usr/bin/osascript', '-e',  'tell application "Music" to previous track',))

			if "thanks mary" in audio2 or "thanks" in audio2:
				OneTrueMery.Response("sure thing. goodbye",self.language)
				pid = os.system("ps a | grep AI_animation")
				os.system("kill -9 " + str(pid))
				# break
				sys.exit()
			if "close" in audio2:
				OneTrueMery.CloseApp(audio2)

			if "nothing" in audio2 or "nevermind" in audio2:
				OneTrueMery.Response("alright then",self.language)
				pid = os.system("ps | grep AI_animation.py")
				os.system("kill -9 " + str(pid))
				# break
				sys.exit()

			if "goodbye" in audio2 or "exit" in audio2:
				OneTrueMery.Response("Goodbye",self.language)
				pid = os.system("ps | grep AI_animation.py")
				os.system("kill -9 " + str(pid))
				sys.exit()

			else:
				pass


	# def Animate(self,counter):
	# 	self.canvas.itemconfig(self.image, image=self.sequence[counter])
	# 	self.root.after(20, lambda: OneTrueMery.Animate((counter+1) % len(self.sequence)))

	# def Exit(self):
		
	# 	self.root.destroy()
	# 	sys.exit()

	# def Miscelaneous(self):
	# 	self.canvas.pack(fill=tkinter.BOTH, expand=True)
	# 	label = tkinter.Label(self.root, text="Mery [Isma's Personal AI]", background="black", foreground="white").pack(fill=tkinter.BOTH, expand=True, side="left")
	# 	button = tkinter.Button(self.root, text="exit",font="bold", highlightbackground="black",command=OneTrueMery.Exit).pack(fill=tkinter.BOTH,side=tkinter.BOTTOM)

	# def Pop(self):
	# 		OneTrueMery.Miscelaneous()
	# 		OneTrueMery.Animate(1)
	# 		self.root.mainloop()



OneTrueMery = Mery()
thingy = "none"
subprocess.Popen("python3 AI_animation.py",shell=True)
	
while True:

	if thingy == "succes":

		OneTrueMery.AI()

	else:

		thingy = OneTrueMery.CallBack()





		