#Step1 : Setup Audio recorder (ffmpeg & portaudio)
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
'''
This configures how logs will be displayed.  It will show messages that are "INFO" level and above (e.g., warnings, errors).
format='%(asctime)s - %(levelname)s - %(message)s' → Defines how the log messages look:

    %(asctime)s → Shows the current time of the log.
    %(levelname)s → Displays the log level (INFO, WARNING, ERROR, etc.).
    %(message)s → The actual log message.
    So, when you log something like logging.info("This is a log message"), it will print:
    2025-02-15 12:34:56 - INFO - This is a log message

'''

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """
    Simplified function to record audio from the microphone and save it as an MP3 file.

    Agrs:
    file_path (str): Path to save the recorded audio file.
    timeout (int): Maximum time to wait for a phrase to start (in seconds).\
    phrase_time_limit (int): Maximum time for the phrase to be recorded (in seconds).
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise....")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start speaking now....")

            #Record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording complete.")

            #Convert the recorded audio to an MP3 file
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate= "128k")

            logging.info(f"Audio saved to {file_path}")

    except Exception as e:
        logging.error(f"An error occured: {e}")

audio_filepath = "C:/AI_doctor_voicebot/human_voice_test.mp3"
record_audio(file_path=audio_filepath)

'''
record_audio(file_path, timeout=20, phrase_time_limit=None):

    file_path: Where to save the audio file.
    timeout: Max time (in seconds) to wait for the user to start speaking.
    phrase_time_limit: Max duration (in seconds) for the speech to be recorded.
    recognizer = sr.Recognizer(): Creates a speech recognizer.
    with sr.Microphone() as source:: Uses the microphone as the audio source.
recognizer.adjust_for_ambient_noise(source, duration=1): Adjusts to background noise.
recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit): Listens and records audio.
Converts recorded audio to WAV format using audio_data.get_wav_data().
Uses AudioSegment.from_wav(BytesIO(wav_data)) to process the WAV file.
Saves it as an MP3 file at the given file_path with 128 kbps quality.
If something goes wrong, it logs an error message.
Example Usage:
audio_filepath = "C:/AI_doctor_voicebot/human_voice_test.mp3"
record_audio(file_path=audio_filepath)

'''
#Step2 : Setup speech to text-STT-model for transcription
import os
from groq import Groq

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
stt_model = "whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)

    audio_file = open(audio_filepath, "rb")
    transcription = client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )

    return transcription.text

'''
This function takes an audio file and converts it into text using Groq's speech-to-text (STT) model. 
transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):

    stt_model: The speech-to-text model to use.
    audio_filepath: The location of the audio file.
    GROQ_API_KEY: The API key to authenticate with Groq.
client = Groq(api_key=GROQ_API_KEY): Creates a connection to Groq using the API key.
audio_file = open(audio_filepath, "rb"): Opens the audio file in binary mode (for reading).
client.audio.transcriptions.create(...):
Uses stt_model to transcribe the English audio file into text.
return transcription.text: The function gives back the text version of the spoken words.
Example Usage:
text_output = transcribe_with_groq("whisper-1", "voice.mp3", "your_groq_api_key")
print(text_output)
Converts voice.mp3 into text using the "whisper-1" model and prints the transcribed text. 
'''