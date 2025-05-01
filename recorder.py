# Import the sounddevice module for audio recording
import sounddevice as sd

# Import the soundfile module to save audio files
import soundfile as sf

# Function to record audio from the microphone and save it as a .wav file
def record_audio(filename="my_audio.wav", duration=6, samplerate=44100):
    print("🎙️ Recording... speak now!")

    # Start recording audio
    # duration * samplerate gives the total number of samples
    # channels=1 means mono recording (single channel)
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)

    # Wait until recording is finished
    sd.wait()

    # Save the recorded audio to a file using the given sample rate
    sf.write(filename, recording, samplerate)

    print(f"✅ Audio saved to {filename}")
