#VoiceBot UI with Gradio
import os
import gradio as gr

from brain_of_the_doctor import encode_image, analyze_image_with_query
from  voice_of_the_human import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_with_gtts, text_to_speech_with_elevenlabs

system_prompt = """You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def process_inputs(audio_filepath, image_filepath):
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
                                                 audio_filepath=audio_filepath,
                                                 stt_model="whisper-large-v3")

    # Handle the image input
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output,
                                                   encoded_image=encode_image(image_filepath),
                                                   model="llama-3.2-11b-vision-preview")
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_with_elevenlabs(doctor_response, "final.mp3")

    return speech_to_text_output, doctor_response, voice_of_doctor

'''
This code listens to an audio question, analyzes an image, and generates a doctor's response as speech using AI models.
System Prompt for AI Doctor
    Defines instructions for the AI to respond like a doctor when analyzing an image.
    Ensures the AI avoids unnecessary phrases and answers concisely in a natural way.

2. Function: process_inputs(audio_filepath, image_filepath)

This function takes an audio question and an image, processes them, and generates a doctor’s voice response.
Step 1: Convert Speech to Text

speech_to_text_output = transcribe_with_groq(
    GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
    audio_filepath=audio_filepath,
    stt_model="whisper-large-v3"
)

    Converts spoken input (audio file) into text using the Whisper model via Groq API.

Step 2: Analyze the Image (If Provided)

if image_filepath:
    doctor_response = analyze_image_with_query(
        query=system_prompt + speech_to_text_output,
        encoded_image=encode_image(image_filepath),
        model="llama-3.2-11b-vision-preview"
    )

    If an image is provided, the AI:
        Encodes the image (encode_image(image_filepath)).
        Sends the image + question to an AI model (llama-3.2-11b-vision-preview) to analyze it like a doctor.
        Generates a doctor’s response based on what’s seen in the image.

Step 3: Handle Missing Image

else:
    doctor_response = "No image provided for me to analyze"

    If no image is given, the AI simply states it can't analyze anything.

Step 4: Convert Text Response to Speech

voice_of_doctor = text_to_speech_with_elevenlabs(doctor_response, "final.mp3")

    Converts the doctor’s response into speech and saves it as "final.mp3" using ElevenLabs TTS.

Step 5: Return All Outputs

return speech_to_text_output, doctor_response, voice_of_doctor

    Returns:
        Converted speech-to-text output
        Doctor’s written response
        Doctor’s spoken response (audio file)

How This Works in Action 🚀

    You ask a medical question via audio. 🎙️
    The AI converts your voice to text.
    If an image is provided, AI analyzes it like a doctor. 🩻
    The AI generates a medical response.
    The response is converted into a voice message. 🔊
    The AI "doctor" answers in speech! 👨‍⚕️🎤

Example Usage:

process_inputs(audio_filepath="question.wav", image_filepath="xray.jpg")

    🎙️ Input: A recorded question about an X-ray.
    📝 Text Output: "Doctor-style diagnosis based on X-ray."
    🔊 Audio Output: "final.mp3" (doctor's voice response).

In Simple Terms:

This function makes an AI doctor 
that listens to your voice, looks at an image (like an X-ray), and then speaks back with a medical response! 🤖👨‍⚕️
'''



# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("Temp.mp3")
    ],
    title = "AI Doctor with Vision and Voice"
)

iface.launch(debug=True)

'''
This code creates a user-friendly AI doctor interface using Gradio. 
The interface takes an audio question and an image and returns a doctor's response in text and speech.
Create the Interface (gr.Interface)

iface = gr.Interface(
    fn=process_inputs,  # The function that processes user inputs

    Uses Gradio to create a web-based interface.
    Calls the process_inputs function when a user submits their inputs.

2. Define Inputs (What Users Provide)

inputs=[
    gr.Audio(sources=["microphone"], type="filepath"),  # User speaks into the mic
    gr.Image(type="filepath")  # User uploads an image (e.g., X-ray, scan)
],

    Audio Input:
        Lets users speak into the microphone.
        Saves the recorded audio as a file (so it can be processed).
    Image Input:
        Lets users upload an image (like a medical scan).

3. Define Outputs (What Users Receive)

outputs=[
    gr.Textbox(label="Speech to Text"),  # Shows transcribed text
    gr.Textbox(label="Doctor's Response"),  # Shows AI-generated doctor's response
    gr.Audio("Temp.mp3")  # Plays the AI doctor's spoken response
],

    Speech to Text:
        Displays what the user said (converted from voice to text).
    Doctor’s Response:
        Displays AI’s medical diagnosis or advice in text.
    Audio Output:
        Plays the doctor’s response as speech (saved in Temp.mp3).

4. Set the Title of the Interface

title = "AI Doctor with Vision and Voice"

    The title that appears on the Gradio web app.

5. Launch the Interface

iface.launch(debug=True)

    Starts the Gradio app so users can interact with it.
    debug=True helps with error tracking during development.

How This Works in Action 🚀

    User speaks a question into the microphone. 🎙️
    User uploads an image (e.g., an X-ray). 🩻
    AI processes both inputs and generates a response.
    AI displays the text response. 💬
    AI plays the doctor's voice response. 🔊

Example Scenario:

    🎤 User speaks: "What does this chest X-ray show?"
    📷 User uploads: X-ray image.
    📝 AI response (text): "With what I see, I think you have mild pneumonia. You should see a doctor."
    🔊 AI response (voice): (Doctor's voice speaks the response.)

In Simple Terms:

This code creates an AI doctor web app where 
users can ask medical questions by voice, upload medical images, and get a doctor-style response in both text and speech! 🤖👨‍⚕️
'''
#http://127.0.0.1:7860
