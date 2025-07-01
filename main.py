
import streamlit as st
from gemini.gemini_utils import (
    generate_quiz_with_gemini,
    explain_topic_with_gemini,
    summarize_topic_with_gemini
)

st.set_page_config(page_title="AI Exam Helper", layout="centered")

st.title("📚 AI Exam Revision Assistant")
st.write("Use Gemini to quiz yourself, get explanations, or quick summaries of any topic!")

subject = st.text_input("Enter the subject (e.g., Biology, Physics):")
topic = st.text_input("Enter the topic (e.g., Photosynthesis, Newton's Laws):")

option = st.radio(
    "What would you like to do?",
    ["Generate Quiz", "Explain Topic", "Summarize Topic"]
)

if st.button("Submit"):
    if not subject or not topic:
        st.warning("Please fill in both subject and topic.")
    else:
        with st.spinner("Thinking..."):
            if option == "Generate Quiz":
                output = generate_quiz_with_gemini(subject, topic)
            elif option == "Explain Topic":
                output = explain_topic_with_gemini(subject, topic)
            elif option == "Summarize Topic":
                output = summarize_topic_with_gemini(subject, topic)
            st.success("Done!")
            st.text_area("🤖 Response:", output, height=300)
