"""
Kinyarwanda Voice Assistant
===========================

This is a simple Kinyarwanda voice assistant that:
1. Records your voice (ASR - Automatic Speech Recognition)
2. Transcribes it into text
3. Matches the text to predefined responses (NLP - Natural Language Processing)
4. Replies back with audio using Text-To-Speech (TTS)

Requirements:
-------------
1. Python 3.8 or above
2. Install dependencies by running `pip install -r requirements.txt`
3. Dependencies include:
    - openai-whisper==20230314
    - gTTS==2.3.2
    - torch==2.2.1
    - pygame==2.5.2
    - sounddevice==0.4.6
    - soundfile==0.12.1
    - SpeechRecognition==3.10.1

How to use:
------------
1. Ensure your microphone is connected.
2. Run this script: `python main.py`
3. The assistant will record your voice and provide a response.
4. It listens for questions like:
    - "amakuru yawe"
    - "witwa nde"
    - "urimo gukora iki"
    - "uri nde"
    - "wakora iki"
5. If the assistant doesn't understand, it will say: "Mbabarira, sinabyumvise neza."

Customization:
-------------
You can add or modify questions and answers by updating the `qa_pairs` dictionary.

Example Output:
---------------
Recording... speak now!
Listening from mic...
Transcribing...
You said: witwa nde
Speaking: Nitwa Umufasha w'Ikoranabuhanga.
"""