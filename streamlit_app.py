import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAcc8lswwX1S9emCcVEXq085P-l7Q3ibIk")
model = genai.GenerativeModel('gemini-pro')

st.title("🤖 ڕەوا ئەی ئای")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    st.chat_message(msg["role"]).markdown(msg["content"])

if prompt := st.chat_input("چی دەپرسی؟"):
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.chat_message("user").markdown(prompt)
    
    response = model.generate_content(prompt)
    st.session_state.chat_history.append({"role": "assistant", "content": response.text})
    st.chat_message("assistant").markdown(response.text)
