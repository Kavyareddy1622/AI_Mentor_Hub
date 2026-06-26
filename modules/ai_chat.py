import streamlit as st
from services.gemini_service import GeminiService


def show():

    st.title("💬 AI Chat Assistant")

    st.write("Ask anything powered by Google Gemini.")

    # Initialize Gemini
    ai = GeminiService()

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User input
    prompt = st.chat_input("Type your question...")

    if prompt:

        # Store user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Response
        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = ai.generate_response(prompt)

                st.markdown(response)

        # Save AI response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )