#Step1 : Setup API keys for Groq and Tavily
import langchain_groq
import langchain_openai
import langchain_community
import langgraph

import os

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

#Step2 : Setup LLM and Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model="gpt-4o-min")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

search_tool = TavilySearchResults(max_results=2)

#Step3 : Setup AI agent with search tool functionality

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt =  "Act as an AI chatbot who is smart and freindly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    agent = create_react_agent(
        model = llm,
        tools = tools,
        state_modifier = system_prompt
    )

    state = {"messages" : query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]

'''
This code is setting up an AI chatbot that can optionally use a search tool to improve its responses.
1. Search Tool Setup

search_tool = TavilySearchResults(max_results=2)

    This creates a Tavily search tool that retrieves up to 2 search results when needed.

2. Function to Get AI Responses

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):

    This function takes in:
        llm_id → The AI model to use (e.g., OpenAI's GPT or Groq's LLM).
        query → The user's question.
        allow_search → Whether to use an external search tool.
        system_prompt → A custom instruction for how the AI should behave.
        provider → Specifies whether to use Groq or OpenAI for the response.

3. Choosing the AI Model

if provider=="Groq":
    llm=ChatGroq(model=llm_id)
elif provider=="OpenAI":
    llm=ChatOpenAI(model=llm_id)

    If Groq is chosen, it uses ChatGroq(model=llm_id).
    If OpenAI is chosen, it uses ChatOpenAI(model=llm_id).

4. Adding Search Capability

tools = [TavilySearchResults(max_results=2)] if allow_search else []

    If allow_search is True, it enables Tavily search.
    Otherwise, the chatbot answers without external search.

5. Creating the AI Agent

agent = create_react_agent(
    model = llm,
    tools = tools,
    state_modifier = system_prompt
)

    The create_react_agent function creates an AI chatbot with:
        model → The selected AI model.
        tools → Optional search functionality.
        state_modifier → The system prompt (e.g., "Be a smart and friendly chatbot").

6. Running the AI Agent

state = {"messages" : query}
response = agent.invoke(state)

    It sends the user’s query to the AI model and gets a response.

7. Extracting AI's Reply

messages = response.get("messages")
ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
return ai_messages[-1]

    The response may contain multiple messages.
    It filters out only the AI's responses.
    Returns the last AI message as the final response.

💡 Simple Explanation

This code creates an AI chatbot that:

    Uses Groq or OpenAI as the AI model.
    Can optionally search the web for better responses.
    Uses a React agent framework for reasoning and tool usage.
    Extracts and returns the final AI-generated response.
'''