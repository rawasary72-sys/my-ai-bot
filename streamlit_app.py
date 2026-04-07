import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAcc8lswwX1S9emCcVEXq085P-l7Q3ibIk")
model = genai.GenerativeModel('gemini-pro')

st.title("🤖 ڕەوا ئەی ئای")

if prompt := st.chat_input("چی دەپرسی؟"):
    st.chat_message("user").markdown(prompt)
    response = model.generate_content(prompt)
    st.chat_message("assistant").markdown(response.text)
