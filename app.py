import streamlit as st
import ollama
from prompts import create_prompt

st.title("AI YouTube Assistant")

topic = st.text_input("Enter Video Topic")

if st.button("Generate"):

    prompt = create_prompt(topic)
    response = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    st.write(response["message"]["content"])