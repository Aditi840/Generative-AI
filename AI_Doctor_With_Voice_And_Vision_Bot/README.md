**AI Doctor: Vision & Voice-based Diagnosis**

This project creates an AI-powered doctor assistant that listens to audio questions, analyzes medical images, and responds with text-based and voice-based medical advice. It uses speech recognition, image analysis, and text-to-speech synthesis to simulate a real-world AI doctor consultation.
**Project Structure**
**1. brain_of_the_doctor.py 🧠**

- This file is responsible for image analysis using Groq's multimodal LLM. It:

    - Converts images into Base64 format for processing.
    - Sends medical images along with a query to the AI model (llama-3.2-90b-vision-preview).
    - Returns a doctor-like diagnosis based on the image analysis.

**2. voice_of_the_human.py 🎤**

- This file handles audio input and speech-to-text conversion. It:

    - Records audio from the microphone and saves it as an MP3 file.
    - Uses Groq’s speech-to-text model (whisper-large-v3) to convert spoken words into text.
    - Returns the transcribed text for further processing.

**3. voice_of_the_doctor.py 🔊**

- This file handles text-to-speech conversion, making the AI doctor’s response more interactive. It:

    - Converts text into speech using Google TTS (gTTS) and ElevenLabs TTS.
    - Supports automatic playback of the generated voice response on Windows, macOS, and Linux.
    - Saves the output as an MP3 file and plays it accordingly.

**4. gradio_app.py 🌐**

- This file provides a user-friendly interface using Gradio. It:

    - Allows users to ask questions by voice and upload medical images.
    - Calls the AI models to generate a doctor-like response.
    - Displays the transcribed text, doctor's written response, and doctor’s voice response.
    - Runs a Gradio-based web app to interact with the AI doctor.

**How to Run the Project 🚀**
**Step 1: Install Dependencies**

- Make sure you have Python 3.8+ installed. Then, install the required libraries:

- pip install gradio speechrecognition gtts pydub elevenlabs groq

**Step 2: Set Up API Keys**

- You need Groq API Key and ElevenLabs API Key. Set them as environment variables:

- export GROQ_API_KEY="your_groq_api_key"
- export ELEVENLABS_API_KEY="your_elevenlabs_api_key"

- (For Windows, use set instead of export.)
** Step 3: Run the Gradio App**

**Start the AI doctor web app by running:**

- python gradio_app.py

**Step 4: Interact with the AI Doctor**

    - Speak into the microphone and/or upload a medical image.
    - The AI will transcribe your speech, analyze the image, and generate a diagnosis.
    - The doctor’s response will be displayed in text and played back as speech.

**Example Usage 🎯**

- 1️⃣ User speaks: "What does this X-ray show?"
- 2️⃣ User uploads: an X-ray image.
- 3️⃣ AI responds (Text): "With what I see, I think you have mild pneumonia. You should see a doctor."
- 4️⃣ AI responds (Voice): Plays the response using ElevenLabs TTS.
**Future Improvements 🚀**

- ✅ Support for multiple languages.
- ✅ Integration with more advanced medical AI models.
- ✅ Enhancements in speech recognition accuracy.

**This AI-powered doctor assistant is designed for educational purposes only and should not be used for real medical diagnoses. Always consult a licensed doctor for medical concerns.**

- 👩‍⚕️👨‍⚕️ Enjoy your AI Doctor Experience! 🎙️💡
