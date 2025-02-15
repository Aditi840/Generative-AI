#Step1a : Setup Text to Speech-TTS-Model with gTTS
import os
from gtts import gTTS
from pydub import AudioSegment

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False
    )
    audioobj.save(output_filepath)

input_text = "Hi this is Ai with Aditi!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

'''
This function converts text into speech using Google Text-to-Speech (gTTS) and saves it as an audio file.
1.Function Definition: 
text_to_speech_with_gtts_old(input_text, output_filepath):

    input_text: The text you want to convert to speech.
    output_filepath: Where to save the generated speech as an MP3 file.
    2.Set the Language:
    language = "en" → The speech will be in English.
3.Create the Audio Object:
audioobj = gTTS(text=input_text, lang=language, slow=False):
Uses gTTS to convert the text to speech.
slow=False → The speech will be in a normal speed (not slow).
4.Save the Speech as an MP3 File:
audioobj.save(output_filepath): Saves the generated speech to the given file path.
5.Example Usage
input_text = "Hi, this is AI with Aditi!"
text_to_speech_with_gtts_old(input_text, output_filepath="gtts_testing.mp3")
What this does:

    Converts "Hi, this is AI with Aditi!" into speech.
    Saves it as "gtts_testing.mp3".

'''


#Step1b : Setup Text to Speech-TTS-model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")


def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Aria",
        model="eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

'''
This function converts text into speech using ElevenLabs' Text-to-Speech (TTS) API and saves it as an audio file. 
Import Required Libraries:

    import elevenlabs → Imports the ElevenLabs library.
    from elevenlabs.client import ElevenLabs → Gets the ElevenLabs client for API calls.

Get the API Key:

    ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
        Retrieves the API key from environment variables (needed to access ElevenLabs' services).
        input_text: The text to convert into speech.
        output_filepath: Where to save the generated audio file.
Create an ElevenLabs Client:
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
This connects to ElevenLabs using the API key.
Generate Speech from Text:
audio = client.generate(
    text=input_text,
    voice="Aria",
    model="eleven_turbo_v2"
)
Converts input_text into speech.
Uses the "Aria" voice.
Uses the "eleven_turbo_v2" model for fast speech generation.
Save the Speech as an MP3 File:
elevenlabs.save(audio, output_filepath)
Saves the generated speech as an MP3 file.
Example Usage:
input_text = "Hi, this is AI with Aditi!"
text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")
What this does:

    Converts "Hi, this is AI with Aditi!" into speech.
    Saves it as "elevenlabs_testing.mp3".
'''

#Step2 : Use Model for Text output to Voice

import subprocess
import platform


def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    # Generate MP3 file using gTTS
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    os_name = platform.system()

    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Convert MP3 to WAV (Required for Windows SoundPlayer)
            wav_filepath = output_filepath.replace(".mp3", ".wav")
            sound = AudioSegment.from_mp3(output_filepath)
            sound.export(wav_filepath, format="wav")

            # Play WAV file using PowerShell
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # Alternative: 'ffplay' or 'aplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

'''
This function converts text to speech using Google Text-to-Speech (gTTS) 
and plays the generated audio file on different operating systems.
Function Definition:

def text_to_speech_with_gtts(input_text, output_filepath):

    input_text: The text to be converted into speech.
    output_filepath: The location where the generated audio file will be saved.
    Set Language to English:

language = "en"

    The speech will be in English.

Convert Text to Speech & Save MP3:

audioobj = gTTS(text=input_text, lang=language, slow=False)
audioobj.save(output_filepath)

    gTTS converts input_text into speech.
    Saves the output as an MP3 file at output_filepath.
    Detect the Operating System:

os_name = platform.system()

    Determines if the system is macOS, Windows, or Linux.

Play the Audio Based on OS:

if os_name == "Darwin":  # macOS
    subprocess.run(['afplay', output_filepath])

    If macOS, it plays the MP3 file using afplay.

elif os_name == "Windows":  # Windows
    # Convert MP3 to WAV
    wav_filepath = output_filepath.replace(".mp3", ".wav")
    sound = AudioSegment.from_mp3(output_filepath)
    sound.export(wav_filepath, format="wav")

    # Play WAV file using PowerShell
    subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'])

    If Windows, it first converts MP3 to WAV (because Windows' default player doesn’t support MP3 playback in this way).
    Then, it plays the WAV file using PowerShell.

elif os_name == "Linux":  # Linux
    subprocess.run(['mpg123', output_filepath])  # Alternative: 'ffplay' or 'aplay'

    If Linux, it plays the MP3 using mpg123 (or alternatives like ffplay or aplay).

else:
    raise OSError("Unsupported operating system")

    If the OS is unknown, it raises an error.

Error Handling:

    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

        If any error occurs while playing the file, it prints an error message.

Example Usage:

input_text = "Hello, this is AI with Aditi!"
text_to_speech_with_gtts(input_text, output_filepath="speech.mp3")

🔹 What this does:

    Converts "Hello, this is AI with Aditi!" into speech.
    Saves it as "speech.mp3".
'''

# Example usage
input_text = "Hi, this is AI with Aditi! Autoplay testing."
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    if not ELEVENLABS_API_KEY:
        raise ValueError("ElevenLabs API key is missing. Set 'ELEVENLABS_API_KEY' as an environment variable.")

    # Initialize ElevenLabs client with the API key
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    try:
        # Generate speech
        audio = client.generate(
            text=input_text,
            voice="Aria",
            model="eleven_turbo_v2"
        )

        # Save audio file
        elevenlabs.save(audio, output_filepath)

        # Determine OS and play the audio
        os_name = platform.system()
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath], check=True)
        elif os_name == "Windows":  # Windows (use Windows Media Player or ffplay)
            try:
                subprocess.run(['powershell', '-c', f'Start-Process -FilePath wmplayer -ArgumentList "{output_filepath}" -NoNewWindow'], check=True)
            except subprocess.CalledProcessError:
                print("Windows Media Player failed. Trying ffplay...")
                subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath], check=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath], check=True)  # Alternative: 'aplay', 'ffplay'
        else:
            raise OSError("Unsupported operating system")

    except Exception as e:
        print(f"An error occurred while generating or playing audio: {e}")

# Example usage
input_text = "Hello, this is AI with Aditi! Autoplay testing with ElevenLabs."
text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")

'''
This function converts text into speech using ElevenLabs' Text-to-Speech (TTS) API, 
saves it as an audio file, and automatically plays the generated speech based on the operating system.
Function Definition:

def text_to_speech_with_elevenlabs(input_text, output_filepath):

    input_text: The text you want to convert into speech.
    output_filepath: The file path where the generated speech will be saved.

Check if the API Key is Available:

if not ELEVENLABS_API_KEY:
    raise ValueError("ElevenLabs API key is missing. Set 'ELEVENLABS_API_KEY' as an environment variable.")

    Ensures that the ElevenLabs API key is set, otherwise it throws an error.

Initialize the ElevenLabs Client:

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    Connects to ElevenLabs API using the provided API key.

Generate Speech from Text:

audio = client.generate(
    text=input_text,
    voice="Aria",
    model="eleven_turbo_v2"
)

    Uses the "Aria" voice model (eleven_turbo_v2) to convert input_text into speech.

Save the Generated Audio:

elevenlabs.save(audio, output_filepath)

    Saves the generated speech as an MP3 file.

Detect the Operating System:

os_name = platform.system()

    Identifies whether the system is macOS, Windows, or Linux.

Play the Audio Based on OS:

    macOS:

subprocess.run(['afplay', output_filepath], check=True)

    Uses afplay to play the audio.

Windows:

subprocess.run(['powershell', '-c', f'Start-Process -FilePath wmplayer -ArgumentList "{output_filepath}" -NoNewWindow'], check=True)

    Tries to play the file using Windows Media Player.
    If it fails, it falls back to ffplay:

    subprocess.run(['ffplay', '-nodisp', '-autoexit', output_filepath], check=True)

Linux:

subprocess.run(['mpg123', output_filepath], check=True)  # Alternative: 'aplay', 'ffplay'

    Uses mpg123 to play the audio (alternatives: aplay, ffplay).

If OS is Unsupported:

    raise OSError("Unsupported operating system")

        If the system is not macOS, Windows, or Linux, it throws an error.

Handle Any Errors Gracefully:

    except Exception as e:
        print(f"An error occurred while generating or playing audio: {e}")

        If anything goes wrong, an error message is printed.

Example Usage:

input_text = "Hello, this is AI with Aditi! Autoplay testing with ElevenLabs."
text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")

🔹 What this does:

    Converts "Hello, this is AI with Aditi!" into speech.
    Saves it as "elevenlabs_testing_autoplay.mp3".
'''