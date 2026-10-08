import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Chat Assistant")
st.caption("Powered by Google Gemini API")

try:
    api_key = st.secrets["GEMINI_API_KEY"]
    client = genai.Client(api_key=api_key)
except Exception:
    st.error("Gemini API key is missing or invalid.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("⚙️ Settings")

    system_instruction = st.text_area(
        "System Instruction",
        value="You are a helpful, friendly and accurate AI assistant."
    )

    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1
    )

    max_tokens = st.slider(
        "Maximum Output Tokens",
        min_value=100,
        max_value=2000,
        value=800,
        step=100
    )

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Type your message...")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    conversation = []

    for message in st.session_state.messages:
        conversation.append(
            {
                "role": message["role"],
                "parts": [{"text": message["content"]}]
            }
        )

    try:
        with st.chat_message("assistant"):

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=conversation,
                config=types.GenerateContentConfig(
                    system_instruction=system_instruction,
                    temperature=temperature,
                    max_output_tokens=max_tokens
                )
            )

            answer = response.text

            st.markdown(answer)

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer
        })

    except Exception as e:
        st.error("Something went wrong while communicating with the Gemini API.")
        st.caption(str(e))