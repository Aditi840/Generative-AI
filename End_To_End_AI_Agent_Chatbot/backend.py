#Step1 : Setup Pydantic Model (Schema Validation)
from pydantic import BaseModel
from typing import List


class RequestState(BaseModel):
    model_name : str
    model_provider : str
    system_prompt : str
    messages : List[str]
    allow_search : bool

'''
This code is setting up a FastAPI-based chatbot API that allows users to interact with an AI model through an endpoint.
1. Defining the Request Format
This defines the structure of incoming API requests using Pydantic.
It ensures that the request contains:

    model_name → Name of the AI model (e.g., GPT-4o, LLaMA-3).
    model_provider → Specifies the AI provider (OpenAI, Groq, etc.).
    system_prompt → Instructions for the AI (e.g., "Be a friendly chatbot").
    messages → A list of user queries (chat history).
    allow_search → A True/False flag to enable external web search.
'''

#Step2 : Setup AI Agent from FrontEnd Request
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

'''
FastAPI is used to create a backend API for the chatbot.
The chatbot logic (get_response_from_ai_agent) is imported from another file.
'''

ALLOWED_MODEL_NAMES = ["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile", "gpt-4o-mini"]

app = FastAPI(title = "LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
#Creating the Chatbot API Endpoint
#This creates a POST API endpoint at /chat where users can send chat requests.
    """
    API Endpoint to interact with the chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}

    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
# Extracts all necessary values from the request.

    # Create AI agent and get response from it!
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response

'''
Calls get_response_from_ai_agent() to generate an AI response.
Returns the AI's reply as the API response.
'''

#Step3 : Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=9999)

'''
Runs the FastAPI server locally on port 9999.
You can test the API using tools like Postman or FastAPI’s Swagger UI.
💡 Simple Explanation

This code:

    Creates an API to talk to an AI chatbot.
    Validates the request to ensure a correct AI model is chosen.
    Forwards the request to get_response_from_ai_agent() to get an AI-generated response.
    Returns the AI's response to the user.
'''