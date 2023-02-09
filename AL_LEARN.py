import speech_recognition
import pyttsx3
#import sr as sr
import os

#from Scripts import sr

from pyttsx3 import voice

#speech = sr.Recongnizer()

try:
    engine = pyttsx3.init()
except ImportError:
    print('Request driver is not found ')
except RuntimeError:
    print('Driver fails to intillies')

voices = engine.getProperty('voices')

for voice in voices:
     print(voice.id)

engine.setProperty('voices','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
#engine.setProperty('voices','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

engine.say('hello Abhass.  welcome to Limitless....')
engine.runAndWait()

# def speak_text_cmd(cmd):
#     engine.say(cmd)
#     engine.runAndWait()
#
# def read_voice_cmd():
#     voice_text = ''
#     print('lisning.....')
#     with sr.Microphone() as source:
#         audio = speech.listen(source)
#     try:
#         voice_text = speech.recognize_google(audio)
#     except sr.UnknownValueError:
#         pass
#     except sr.RequestError as e:
#         print('Network error ')
#     return  voice_text
#
# if __name__ == "__main__":
#  speak_text_cmd('Hello Mr. NEGI. This as your Artifical intellgent')
#
#     while True:
#
#         voice_note = read_voice_cmd()
#
#         if 'hello' in voice_note:
#             speak_text_cmd('Hello sir how can i help you')
#             continue
#         elif 'open' in voice_note:
#             os.system('explorer C:\\ {}'.format(voice_note.replace(('open',''))))
#             continue
#         elif 'bye' in voice_note:
#              speak_text_cmd('by mr Negi. happy to help you .have a good day')
#              exit()
#


