import streamlit as st
from gemini.gemini_utils import (
    generate_quiz_with_gemini,
    explain_topic_with_gemini,
    summarize_topic_with_gemini
)
from agent.state_tracker import StateTracker

# App config
st.set_page_config(page_title="AI Exam Helper", layout="centered")
st.title("📚 AI Exam Revision Assistant")
st.write("Use Gemini to quiz yourself, get explanations, or quick summaries of any topic!")

# Initialize memory
if "tracker" not in st.session_state:
    st.session_state.tracker = StateTracker()

# Input UI
subject = st.text_input("Enter the subject (e.g., Biology, Physics):")
topic = st.text_input("Enter the topic (e.g., Photosynthesis, Newton's Laws):")

option = st.radio(
    "What would you like to do?",
    ["Generate Quiz", "Explain Topic", "Summarize Topic"]
)

# Action button
if st.button("Submit"):
    if not subject or not topic:
        st.warning("Please fill in both subject and topic.")
    else:
        with st.spinner("Thinking with Gemini..."):
            if option == "Generate Quiz":
                output = generate_quiz_with_gemini(subject, topic)
            elif option == "Explain Topic":
                output = explain_topic_with_gemini(subject, topic)
            elif option == "Summarize Topic":
                output = summarize_topic_with_gemini(subject, topic)

            # Save state
            st.session_state.tracker.update(subject, topic, option, output)

            # Display result
            st.success("✅ Done!")
            st.text_area("🤖 Response:", output, height=300)

# Optional: Show history
if st.checkbox("📜 Show History"):
    history = st.session_state.tracker.get_history()
    if not history:
        st.info("No history yet.")
    else:
        for idx, entry in enumerate(reversed(history), 1):
            st.markdown(f"**{idx}. {entry['action']} — {entry['subject']} / {entry['topic']}**")
            st.text(entry['response'])
