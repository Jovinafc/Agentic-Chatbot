import streamlit as st
import os

st.set_page_config(page_title="Langgraph Agent UI", layout = "wide")
st.title('AI Chatbot Agents')
st.write('Create and Interact with AI agents')

system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["meta-llama/llama-4-scout-17b-16e-instruct"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)
    
    
allow_web_search = st.checkbox('Allow Web Search')

user_query = st.text_area("Enter your query:  ", height=150, placeholder="Ask Anything!")

# API_URL = 'http://127.0.0.1:9999/chat'
# API_URL = 'https://agentic-chatbot-backend-3l4l.onrender.com/chat'
API_URL = f'{os.environ.get('API_URL')}/chat'

if st.button("Ask Agent!"):
    #Get Response From Backend
    if user_query.strip():
        
        import requests
            
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }
        
        response = requests.post(API_URL, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data['error'])
            else:      
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:** {response_data}")

        