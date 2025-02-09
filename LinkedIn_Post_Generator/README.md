## LinkedIn Post Generator

## Overview

This project generates LinkedIn posts based on user-selected attributes such as 
topic, length, and language using a few-shot learning approach and an AI model.

## Requirements

- Python 3.8+
- A valid Groq API key

**Installation**

1. Clone the repository:

- git clone <repository_url>
- cd LinkedIn_Post_Generator

2. Set up environment variables:

- Create a .env file in the root directory and add your Groq API key:
- GROQ_API_KEY="YOUR_API_KEY"


**Running the Project**

- To start the LinkedIn Post Generator:
- streamlit run main.py

This will launch a Streamlit web application where you can generate posts based on your preferences.

## File Structure

- main.py - The entry point for the Streamlit app.

- few_shot.py - Handles retrieval of sample LinkedIn posts.

- llm_helper.py - Manages interactions with the AI model.

- post_generator.py - Generates posts based on user inputs.

- preprocess.py - Prepares and standardizes input data.

- .env - Stores API keys (not included in the repository for security reasons).


## Notes

- Ensure that the data directory contains the necessary JSON files for post retrieval and processing.

- The model requires a valid Groq API key to function correctly.

- If you encounter issues, verify that dependencies are installed correctly and the .env file is properly configured.
  
