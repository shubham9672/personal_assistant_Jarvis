import speech_recognition as sr
import pyttsx3
import news
import wikipedia
import webbrowser
#pip install pipwin
#pipwin install pyaudio

engine = pyttsx3.init()
i=0
while 1:
	fp=["get me","turn on","how are you"]
	tp=["getting you","turning on", "i'm fine"]
	r = sr.Recognizer()
	with sr.Microphone() as source:
		engine.say("Speak anything")
		engine.runAndWait()
	#print("speak anything:")
		audio= r.listen(source)
		text=r.recognize_google(audio)
		try:
			#print(text)
			engine.say("you said:{}".format(text))
			d=text.split("Jarvis")
			#print(d)
				#print(len(d))
			#if "thanks" in text:print("My pleasure")
			#if "news" in text:news.NewsFromBBC()
			if d[1]!='':
				e=d[1]
				#print(e)
				if ("who" and "you") in e:
					engine.say("I'm a python 3.8 based package which was created by Harsh Nandwana ")
				#print("WEA")
								#########[WEATHER]######################(START)
				if "weather in" in e:
					g=e.split("weather in")
					f=e.split(" ")
					import weather
					weather.weather(f[1])
					#print(f[1])
								#########[WEATHER]######################(STOP)
				#print("NEWS")
				if "news" in e:news.NewsFromBBC() 					#########	[NEWS]
								#########[WIKIPIDEA]######################(START)
				#print("WIKIPIDEA")
				if "what is" or "tell me about" in e:
					if "what is" in e:
						h=e.split("what is")
					if "tell me about" in d[1]:
						h=e.split("tell me about")
					#print(h[1])
					#print(f[1])
					try:
						print(wikipedia.summary(h[1]))
						#engine.say(wikipedia.summary(d[1]))
						#engine.runAndWait()
					except:
						print("sorry nothing such found")
								#########[WIKIPEDIA]######################(STOP)
				print("BROWSER")
								#########[BROWSER]######################(START)
				if "browser" in e:
					#print("vdfgdsvjh")
					webbrowser.open('http://google.com', new=2)
								#########[BROWSER]######################(STOP)
				for strings in fp:
					e=e.replace(fp[i], tp[i])
					i=i+1
					engine.say("Jarvis:{}".format(e))

				engine.runAndWait()



					###########################
			if d[1]=='':
				if "Jarvis" in text:
					engine.say("Jarvis: yes sir")
					engine.runAndWait()
					audio= r.listen(source)
					command=r.recognize_google(audio)
					#print(command)
					if "weather in" in command:
						e=command.split("weather in")
						f=e[1].split(" ")
						import weather
						weather.weather(f[1])
					elif "news" in command:news.NewsFromBBC() 					#########	[NEWS]
						#print(f)
						#weather.cityname=f[1]

								#########	[WIKIPEDIA]	######################	(START)
					elif "what is" or "tell me about" in command:
						if "what is" in command:
							h=command.split("what is")
						if "tell me about" in command:
							h=command.split("tell me about")
						#print(h[1])
						#print(f[1])
						try:
							print(wikipedia.summary(h[1]))
							#engine.runAndWait()
						except:
							print("sorry nothing such found")
								#########	[WIKIPIDEA]	######################	(STOP)

								#########	[BROWSER]	######################	(START)
					elif "open browser" in command:
						webbrowser.open('http://google.com', new=2)
								#########	[BROWSER]	######################	(STOP)
					for strings in fp:
						command=command.replace(fp[i], tp[i])
						i=i+1
					engine.say("Jarvis:{}".format(command))
					engine.runAndWait()
		except:
			print("sorry")
