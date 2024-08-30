from gtts import gTTS
import os

def generate_audio_prompt(detections):
    text = " ".join([f"{det['label']} with confidence {det['confidence']:.2f}" for det in detections])
    tts = gTTS(text)
    audio_path = 'output.mp3'
    tts.save(audio_path)

    return audio_path
