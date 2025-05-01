# Import the function that records audio from the microphone and saves it
from recorder import record_audio

# Import the function that transcribes spoken words into text using speech recognition
from transcriber import transcribe_speech

# Import the function that matches user input text to a predefined answer
from qa_pairs import match_answer

# Import the function that converts text to speech and plays it aloud
from speaker import speak

# Entry point of the program
if __name__ == "__main__":
    # Step 1: Record user's speech and save it as an audio file
    record_audio()

    # Step 2: Transcribe the recorded audio into text
    user_text = transcribe_speech()

    # Step 3: If valid speech was transcribed
    if user_text:
        # Match the text to a predefined response
        reply = match_answer(user_text)
        # Speak out the response
        speak(reply)
    else:
        # If transcription failed or no valid input was detected
        print("❌ No valid speech to process.")
