from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
from playsound import playsound

# This code defines a function `speakTheSentence` that takes two arguments: `text` and `language`.
# The function translates the `text` into the specified `language` using the Google Translate API.
# Then, it uses the Google Text-to-Speech API to convert the translated text into speech.
# Finally, it plays the generated speech using the `playsound` library.
# If a file named 'sound.mp3' already exists in the current directory, it is first removed before proceeding.

eng = Translator()
def speakTheSentence(text, language):
    """
    This function translates the given text into the specified language,
    converts the translated text into speech using Google Text-to-Speech API,
    and plays the generated speech using the playsound library.

    Parameters:
    text (str): The text to be translated and spoken.
    language (str): The target language for translation and speech generation.

    Returns:
    None
    """
    # Check if a file named 'sound.mp3' already exists in the current directory
    if os.path.exists('sound.mp3'):
        os.remove('sound.mp3') # If exists, remove it
        speakTheSentence() # Recursively call the function to remove the file
    else:
        myText = eng.translate(text, dest=language) # Translate the given text into the specified language
        cnvt = gTTS(myText.text, lang=language) # Convert the translated text into speech using Google Text-to-Speech API
        cnvt.save("sound.mp3") # Save the generated speech as 'sound.mp3'
        playsound("sound.mp3")   # Play the saved speech using the playsound library
        os.remove('sound.mp3') # Remove the file 'sound.mp3'


if '__main__' == __name__:
    # This code snippet is used to test the `speakTheSentence` function.
    # It translates the Hindi phrase "namaste bhaaiyo or unki beheno" into the specified Hindi language and plays the translated text as speech.
    speakTheSentence("namaste bhaaiyo or unki beheno", "hi")
    pass

