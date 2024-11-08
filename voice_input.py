import pyaudio
import wave
import numpy as np
from speechbrain.pretrained import SpeakerRecognition
import speech_recognition as sr

# Initialize speaker verification model
verification_model = SpeakerRecognition.from_hparams(source="speechbrain/spkrec-ecapa-voxceleb", savedir="pretrained_models/")
reference_audio = "path/to/your/voice_sample.wav"  # Reference audio for your voice

# Audio configuration
CHUNK = 1024         # Buffer size
FORMAT = pyaudio.paInt16
CHANNELS = 1         # Mono audio
RATE = 16000         # Sample rate (16kHz is commonly used for speech)

# Initialize PyAudio
p = pyaudio.PyAudio()

# Start audio stream
stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

recognizer = sr.Recognizer()

def is_user_voice(audio_file):
    # Speaker verification
    score, prediction = verification_model.verify_files(reference_audio, audio_file)
    return prediction == True and score > 0.5

def transcribe(audio_data):
    # Transcription using SpeechRecognition
    with sr.AudioFile(audio_data) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language="hu-HU")  # Transcribe in Hungarian
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError:
        return "API request failed"


def listening():
    try:
        while True:
            frames = []

            # Capture audio segment
            for i in range(0, int(RATE / CHUNK * 2)):  # Capture 2 seconds of audio
                data = stream.read(CHUNK)
                frames.append(data)

            # Save segment to temporary file
            audio_segment = b"".join(frames)
            temp_filename = "temp_audio.wav"
            wf = wave.open(temp_filename, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(audio_segment)
            wf.close()

            # Verify if it's your voice
            if is_user_voice(temp_filename):
                print("Verified your voice. Transcribing...")
                transcription = transcribe(temp_filename)
                print("Transcription:", transcription)
            else:
                print("Voice not recognized as yours.")
            
    except KeyboardInterrupt:
        print("Stopping...")

    finally:
        # Clean up
        stream.stop_stream()
        stream.close()
        p.terminate()
