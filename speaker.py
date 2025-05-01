# Import the Google Text-to-Speech module
from gtts import gTTS

# Import pygame to handle audio playback
import pygame

# Function to convert text to speech and play it aloud
def speak(text, filename="response.mp3"):
    print("🗣️ Speaking:", text)

    # Convert the given text to speech using gTTS
    # 'lang' can be set to 'rw' for Kinyarwanda or 'en' for English
    tts = gTTS(text=text, lang='sw')  # Change to 'rw' if using Kinyarwanda

    # Save the generated speech audio to a file
    tts.save(filename)

    # Initialize the pygame mixer module
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(filename)

    # Play the audio file
    pygame.mixer.music.play()

    # Wait until playback is finished before continuing
    while pygame.mixer.music.get_busy():
        continue
