import pyttsx3 as tts

engine = tts.init()

engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

#queue up things to say
engine.say("Hi! This is Eva's bot")
engine.say("How can I help you today?")

# Flush the say() queue and play the audio
engine.runAndWait()

# Program will not continue execution until
# all speech is done talking