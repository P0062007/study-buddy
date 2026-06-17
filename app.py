import streamlit as st

def explain_topic(topic):
    explanations = {
        "python": "Python is a high-level programming language used for web development, AI, and data science.",
        "ai": "Artificial Intelligence enables machines to learn and make decisions like humans.",
        "machine learning": "Machine Learning is a branch of AI that learns from data.",
        "java": "Java is an object-oriented programming language used for building applications."
    }
    return explanations.get(topic.lower(), "No explanation found.")

st.title("AI Study Buddy")

topic = st.text_input("Enter Topic")

if st.button("Explain"):
    st.write(explain_topic(topic))
