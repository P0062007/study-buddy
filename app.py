import streamlit as st

st.title("AI Study Buddy 🤖")

question = st.text_input("Ask me anything")

answers = {
    "what is python": "Python is a high-level programming language.",
    "what is ai": "AI stands for Artificial Intelligence.",
    "what is machine learning": "Machine Learning is a branch of AI that learns from data.",
    "what is streamlit": "Streamlit is a Python library for creating web apps.",
    "what is html": "HTML is used to create web pages.",
    "what is css": "CSS is used to style web pages.",
    "what is javascript": "JavaScript adds interactivity to websites.",
    "what is github": "GitHub is a platform for storing and sharing code.",
    "what is data science": "Data Science involves extracting insights from data."
}

if st.button("Get Answer"):
    if question:
        st.write(
            answers.get(
                question.lower(),
                "Sorry, I don't know that answer yet."
            )
        )
    else:
        st.write("Please enter a question.")
