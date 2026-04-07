import streamlit as st
import google.generativeai as genai

# کلیلی API
API_KEY = "gen-lang-client-0628609446" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Rawa AI", page_icon="🤖")
st.title("🤖 ڕەوا ئەی ئای")
st.write("سڵاو ڕەوا، وێبسایتەکەت بە سەرکەوتوویی کار دەکات!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("چی دەپرسی؟"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except:
            st.error("کێشەیەک لە سێرڤەر هەیە، کەمێکی تر تاقی بکەرەوە.")
