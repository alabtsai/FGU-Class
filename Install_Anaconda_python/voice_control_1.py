import speech_recognition as sr
#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print(index, name)

# obtain audio from the microphone
r = sr.Recognizer()
r.energy_threshold = 800
r.dynamic_energy_threshold = True
with sr.Microphone() as source:
    print("Say something!")
    mic = sr.Microphone()
    print(mic)
    audio = r.listen(source)

text= r.recognize_google(audio)
print("Google Speech Recognition thinks you said:\n" + text)
