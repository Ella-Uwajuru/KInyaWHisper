# Import the speech recognition library
import speech_recognition as sr

# Function to capture audio from the microphone and transcribe it to text
def transcribe_speech():
    # Create a recognizer object that will process audio input
    recognizer = sr.Recognizer()

    # Use the system microphone as the audio input source
    mic = sr.Microphone()

    with mic as source:
        print("🎧 Listening from mic...")
        # Adjust for background noise to improve recognition accuracy
        recognizer.adjust_for_ambient_noise(source)
        # Listen and capture the audio from the microphone
        audio = recognizer.listen(source)

    try:
        print("🧠 Transcribing...")
        # Use Google Speech Recognition to convert the audio to text
        # The 'language' is set to Kinyarwanda ('rw-RW')
        text = recognizer.recognize_google(audio, language="rw-RW")
        print("📝 You said:", text)
        # Return the transcribed text in lowercase and without leading/trailing spaces
        return text.lower().strip()
    
    # Handle cases where speech was unintelligible
    except sr.UnknownValueError:
        print("😵 Couldn’t understand what you said.")
        return ""
    
    # Handle cases where the Google API could not be reached
    except sr.RequestError:
        print("🌐 Internet error during transcription.")
        return ""
