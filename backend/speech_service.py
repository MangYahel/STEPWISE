import os
import azure.cognitiveservices.speech as speechsdk
import uuid

speech_config = speechsdk.SpeechConfig(
    subscription=os.getenv("AZURE_SPEECH_KEY"),
    region=os.getenv("AZURE_SPEECH_REGION")
)

speech_config.speech_synthesis_voice_name = "en-US-JennyNeural"

def synthesize_speech(text):
    filename = f"audio/{uuid.uuid4()}.wav"
    audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)

    synthesizer = speechsdk.SpeechSynthesizer(
        speech_config=speech_config,
        audio_config=audio_config
    )

    synthesizer.speak_text_async(text).get()
    return filename
