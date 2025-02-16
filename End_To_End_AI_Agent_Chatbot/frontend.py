#Step1 : Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import streamlit as st

#Setting Up the Web Page
st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with AI Agents!")

'''
Sets the page title and layout using set_page_config().
Displays a title and a short description of the chatbot.
'''

# User Defines the AI Agent’s Personality
system_prompt = st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here....")

#Users can describe how the AI should behave (e.g., "Be a friendly assistant").

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq", "OPENAI"))
#Users select the AI provider (either Groq or OpenAI).

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OPENAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

#Depending on the selected provider, it shows the available models to choose from.

#Allow Web Search Option
allow_web_search = st.selectbox("Allow Web Search", ["Yes", "No"])
#Users choose whether to enable web search for better responses.


user_query = st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

#. Sending the Request to Backend
API_URL = "http://localhost:9999/chat"
#Defines the backend API URL (which was created using FastAPI).

if st.button("Ask Agent!"):
    if user_query.strip():
        # Step2 : Connect with backend via URL
        import requests

#When the user clicks "Ask Agent!", the chatbot sends the request to the backend.
#Ensures the user has entered a valid question.

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

'''
Creates a JSON payload with user inputs:

    Selected AI model & provider
    System prompt (personality of the AI)
    User’s question
    Whether web search is allowed
'''
        response = requests.post(API_URL, json=payload)
        #Sends the request to the FastAPI backend via HTTP POST.

        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")

# If the request is successful, it checks if there is an error.
# If there's no error, it displays the AI’s response on the screen.
'''
 Simple Explanation

    User defines the chatbot’s personality using a system prompt.
    User selects an AI model (Groq or OpenAI).
    User enters a question for the chatbot.
    The request is sent to a FastAPI backend for processing.
    The AI generates a response, which is displayed on the screen.
'''




