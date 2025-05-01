import speech_recognition as sr

def transcribe_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎧 Listening from mic...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Transcribing...")
        text = recognizer.recognize_google(audio, language="rw-RW")  # Kinyarwanda
        print("📝 You said:", text)
        return text.lower().strip()
    except sr.UnknownValueError:
        print("😵 Couldn’t understand what you said.")
        return ""
    except sr.RequestError:
        print("🌐 Internet error during transcription.")
        return ""
