import streamlit as st
import google.generativeai as genai

# ڕێکخستنی کلیلەکە
genai.configure(api_key="AIzaSyAcc8lswwX1S9emCcVEXq085P-l7Q3ibIk")
model = genai.GenerativeModel('gemini-pro')

st.title("🤖 ڕەوا ئەی ئای")
st.write("سڵاو ڕەوا، ئێستا وێبسایتەکە بە تەواوی ئامادەیە!")

if prompt := st.chat_input("چی دەپرسی؟"):
    st.chat_message("user").markdown(prompt)
    try:
        response = model.generate_content(prompt)
        st.chat_message("assistant").markdown(response.text)
    except:
        st.error("کێشەیەک هەیە، تکایە دواتر تاقی بکەرەوە.")
