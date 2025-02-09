#Importing Libraries


from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os

load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-90b-vision-preview")

if __name__ == "__main__":
    response = llm.invoke("What are the two main ingredients in samosa")
    print(response.content)


'''
This code initializes and utilizes a language model from Groq's API. It first loads environment variables using load_dotenv(), ensuring that sensitive 
information like API keys is securely retrieved. The ChatGroq instance is then created, using the GROQ_API_KEY from environment variables and specifying the 
model "llama-3.2-90b-vision-preview". If the script is run directly, it invokes the model with the question "What are the two main ingredients in samosa" and 
prints the model’s response. This setup enables interaction with an AI model for natural language processing tasks.
'''