
import streamlit as st
import google.generativeai as genai

# کلیلی API کە پێشتر دروستت کردبوو
API_KEY = "gen-lang-client-0628609446" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

st.set_page_config(page_title="Rawa AI", page_icon="🤖")
st.title("🤖 ڕەوا ئەی ئای")
st.markdown("سڵاو ڕەوا، من ئامادەم وەڵامی هەموو پرسیارەکانت بدەمەوە.")

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
        except Exception as e:
            st.error("کێشەیەک لە پەیوەندییەکەدا هەیە.")
