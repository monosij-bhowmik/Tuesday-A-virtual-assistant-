#pyaudio and SpeechRecognition required
import speech_recognition as sr

#record audio
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Please enter the password...")
    audio = r.listen(source, phrase_time_limit=3)

#Recognize Speech and text output
try:
    value = r.recognize_google(audio)
    r.recognize_google(audio)
    print("You Said :"+ r.recognize_google(audio))
    if value == 'hey Tuesday':
        print("Hey Rohit, I'm Tuesday how can I help you ?")
    else:
        print("Incorrect Pasword")
except sr.UnknownValueError:
    print("Google Speech Recognition couldn't understand")
except sr.RequestError as e:
    print("Could not request results".format(e))
