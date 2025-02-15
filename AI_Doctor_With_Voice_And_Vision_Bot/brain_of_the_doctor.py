#Step1 : Setup GROQ API Key
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


#Step2 : Convert image to required format
import base64


#image_path = "C:/AI_doctor_voicebot/acne.jpg"

def encode_image(image_path):
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode('utf-8')

'''
This function, encode_image, takes an image file path as input. It opens the image in binary mode ("rb"), reads its content, 
and converts it into a Base64-encoded string. The b64encode method encodes the binary data, and .decode('utf-8') ensures the 
output is a readable text string. This is useful for embedding images in text-based formats like JSON or HTML.
'''

#Step3 : Setup Multimodal LLM
from groq import Groq

query = "Is there something wrong with my face?"
model = "llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):
    client = Groq()


    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                    },
                },
            ],
        }]
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model
    )

    return chat_completion.choices[0].message.content

'''
This function, analyze_image_with_query, takes a text query, a model name, and a Base64-encoded image as input. It creates a 
Groq client and prepares a message containing both the query text and the image data. The image is formatted as a Base64-encoded 
JPEG for processing. The function then sends this data to the specified model for analysis 
using client.chat.completions.create(). Finally, it returns the model’s response, which is the first generated message content.
'''