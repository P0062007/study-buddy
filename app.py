import streamlit as st
from openai import OpenAI

# Create client (we will add API key next)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("AI Study Buddy 🤖")

topic = st.text_input("Ask me anything")

if st.button("Get Answer"):
    if topic:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful study tutor for students."},
                {"role": "user", "content": topic}
            ]
        )

        answer = response.choices[0].message.content
        st.write(answer)
    else:
        st.write("Please enter a question")
