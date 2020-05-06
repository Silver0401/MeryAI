import speech_recognition as sr
import os
from gtts import gTTS
import warnings
import sys


warnings.filterwarnings("ignore")

def Listener():

	AudioReader = sr.Recognizer()

	with sr.Microphone() as source:
		audio = AudioReader.listen(source)
		print ("I'm Listening")

		data = ""
		try:
			data = AudioReader.recognize_google(audio) 
			print ("you said: " + data)

		except sr.UnknownValueError:
			print ("waiting for audio...")

		except sr.RequestError as e:
			print ("Service error from Google Speech Recognition, check internet connection " + e)

		return data


def CallBack(text):
	WakeWords = ["mary", "hey mary", "mery", "married", "marrieds", "he married", "ameri", "amari", "marry"]

	text = text.lower()
	for phrase in WakeWords:
		if phrase in text:
			return True

	return False


def Response(text):

	TtS = gTTS(text = text, lang = "en", slow=False)
	#Text to Speech

	TtS.save("TextToResponse.mp3")

	os.system("afplay TextToResponse.mp3")

def MeryActivated():

	while True:

		audio = Listener() 

		if CallBack(audio) == True:			
			# subprocess.call(["python3","{}".format("AI_animation.py")])
			Response("Yes Master?")

			return "success"
			break

			




