from gtts import gTTS
import os
 
# 1. Type the text you want to hear
text = input("What do you want to say? ")
 
# 2. Make the voice ("es" = Spanish, "en" = English, "fr" = French)
voice = gTTS(text=text, lang="es")
 
# 3. Save the voice as an audio file


path = os.path.join(os.path.expanduser("~"), "Desktop", "hello.mp3")
voice.save(path)

print("Saved here:", path)
