from recorder import record_audio
from transcriber import transcribe_speech
from qa_pairs import match_answer
from speaker import speak

if __name__ == "__main__":
    record_audio()
    user_text = transcribe_speech()
    if user_text:
        reply = match_answer(user_text)
        speak(reply)
    else:
        print("❌ No valid speech to process.")
