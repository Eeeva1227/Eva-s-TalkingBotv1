import speech_recognition as sr
# piece of code that easily convert speech to text
r = sr.Recognizer()

readin = "How can I help you today?"
with sr.Microphone() as source:
    print("How can I help you today?")
    audio = r.listen(source)
    print("Thank you ><")


try:
    print("Did you say: " + r.recognize_google(audio))
except:
    pass

def Listen():
    command = input(readin)
    return command

def Decide(listened):
    print("command = {listen}.".format(listened))