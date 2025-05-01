from gtts import gTTS
import pygame

def speak(text, filename="response.mp3"):
    print("🗣️ Speaking:", text)
    tts = gTTS(text=text, lang='en')  # Use 'rw' for Kinyarwanda
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
