from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
from playsound import playsound

eng = Translator()
def speakTheSentence(text, language):
    if os.path.exists('sound.mp3'):
        os.remove('sound.mp3')
        speakTheSentence()
    else:
        myText = eng.translate(text, dest=language)
        cnvt = gTTS(myText.text, lang=language)
        cnvt.save("sound.mp3")
        playsound("sound.mp3")  
        # os.system("mpg123", "sound.mp3")
        os.remove('sound.mp3')


if '__main__' == __name__:
    speakTheSentence("namaste bhaaiyo or unki beheno", "hi")
    pass
