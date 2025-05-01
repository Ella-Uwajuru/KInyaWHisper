import sounddevice as sd
import soundfile as sf

def record_audio(filename="my_audio.wav", duration=6, samplerate=44100):
    print("🎙️ Recording... speak now!")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    sf.write(filename, recording, samplerate)
    print(f"✅ Audio saved to {filename}")