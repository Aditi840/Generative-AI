**End To End AI Agent Chatbot**
This project is a smart AI chatbot built with LangGraph, OpenAI, and Groq LLMs. It allows users to interact with AI models, customize responses with system prompts, and optionally enable web search functionality for better answers. The chatbot supports multiple AI providers (Groq & OpenAI) and comes with a FastAPI backend and a Streamlit-based frontend for an easy-to-use interface.
**Project Structure**
**1. ai_agent.py 🤖**

**This file contains the core logic for the AI chatbot. It:**

    - Sets up Groq, OpenAI, and Tavily Search API keys.
    - Configures LLM models from OpenAI (gpt-4o-mini) and Groq (llama-3.3-70b-versatile).
    - Allows the AI agent to respond to user queries and optionally use web search to enhance its responses.

**2. backend.py ⚙️**

- This file implements the FastAPI backend, which:

    - Defines the request schema using Pydantic to validate inputs.
    - Creates an API endpoint (/chat) where the frontend can send requests.
    - Calls the AI agent function (get_response_from_ai_agent) to get a response based on the user's input.
    - Runs the FastAPI server on localhost:9999 and provides Swagger UI documentation for easy API testing.

**3. frontend.py 🌐**

- This file builds a user-friendly web interface using Streamlit. It:

    - Lets users select an AI provider (Groq or OpenAI).
    - Allows users to choose an LLM model (like llama-3.3-70b-versatile or gpt-4o-mini).
    - Provides a text area to define a system prompt (to customize AI behavior).
    - Enables an optional web search feature to enhance responses.
    - Connects with the FastAPI backend (http://localhost:9999/chat) to process queries and display AI responses.

**How to Run the Project 🚀**
**Step 1: Install Dependencies**

- Make sure you have Python 3.8+ installed. Then, install the required libraries:

- pip install fastapi uvicorn streamlit langchain_openai langchain_groq langgraph pydantic requests

**Step 2: Set Up API Keys**

- You need API keys for Groq, OpenAI, and Tavily Search. Set them as environment variables:

- export GROQ_API_KEY="your_groq_api_key"
- export OPENAI_API_KEY="your_openai_api_key"
- export TAVILY_API_KEY="your_tavily_api_key"

- (For Windows, use set instead of export.)
**Step 3: Start the Backend Server**

- Run the FastAPI backend:

- python backend.py

    - The server will run at http://localhost:9999.
    - Open http://localhost:9999/docs in your browser to test the API.

**Step 4: Start the Frontend**

- Launch the Streamlit-based UI:

- streamlit run frontend.py

    - The chatbot interface will open in your browser.
    - You can enter your query, choose an AI model, and get responses.

**Example Usage 🎯**

- 1️⃣ User selects: AI provider (Groq or OpenAI).
- 2️⃣ User enters: System prompt ("Act like a friendly AI assistant.").
- 3️⃣ User types: Query ("What's the latest news on AI?").
- 4️⃣ AI processes the query, optionally using web search.
- 5️⃣ AI responds in real time with an intelligent answer.

**Future Improvements 🚀**

- ✅ Support for more AI models.
- ✅ Integration with voice-based queries.
- ✅ Enhancements in real-time response generation.

This project is a powerful AI chatbot that leverages LLMs and web search to provide smart and insightful answers. Give it a try and enhance your chatbot experience! 🤖🔥
