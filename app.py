import streamlit as st
from src.chatbot import PythonChatbot


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Python Q&A Chatbot",
    page_icon="🐍",
    layout="centered"
)


# -----------------------------
# Load chatbot
# -----------------------------
@st.cache_resource
def load_chatbot():
    return PythonChatbot(
        "data/python_knowledge_base.csv",
        confidence_threshold=0.25
    )


chatbot = load_chatbot()


# -----------------------------
# Header
# -----------------------------
st.title("🐍 Python Question-Answering Chatbot")

st.markdown(
    """
    **Personal Python Learning Assistant**

    Ask a Python programming question in natural language
    and get an answer from a predefined Python knowledge base.
    """
)

st.info(
    """
    **Knowledge Base:** 35 Python Q&A entries  
    **Matching Method:** TF-IDF + Cosine Similarity  
    **Coverage:** Python fundamentals, data structures, functions,
    control flow, OOP, exceptions, modules, and file handling
    """
)


# -----------------------------
# Example questions
# -----------------------------
st.subheader("💡 Example Questions")

example_questions = [
    "What is Python?",
    "What is a list?",
    "How do I create a function?",
    "What is inheritance?",
    "What is exception handling?"
]

cols = st.columns(2)

for index, question in enumerate(example_questions):
    with cols[index % 2]:
        if st.button(question, use_container_width=True):
            st.session_state["selected_question"] = question


# -----------------------------
# Question input
# -----------------------------
st.subheader("💬 Ask a Python Question")

default_question = st.session_state.get("selected_question", "")

user_question = st.text_input(
    "Enter your question:",
    value=default_question,
    placeholder="Example: What is a dictionary in Python?"
)


# -----------------------------
# Ask button
# -----------------------------
if st.button("🔎 Get Answer", type="primary", use_container_width=True):

    result = chatbot.answer_question(user_question)

    st.subheader("🤖 Answer")

    st.write(result["answer"])

    if result["matched_question"]:

        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Topic",
                result["category"]
            )

        with col2:
            st.metric(
                "Match Confidence",
                f"{result['confidence']:.1%}"
            )

        st.caption(
            f"Matched knowledge-base question: "
            f"{result['matched_question']}"
        )

    else:
        st.warning(
            "Try asking a more specific Python-related question."
        )


# -----------------------------
# Supported topics
# -----------------------------
st.markdown("---")

st.subheader("📚 Supported Python Topics")

topics = [
    "Python Basics",
    "Data Structures",
    "Control Flow",
    "Functions",
    "Object-Oriented Programming",
    "Exception Handling",
    "Modules",
    "File Handling",
    "Python Concepts"
]

st.write(" • ".join(topics))


# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "This chatbot retrieves answers from a predefined Python "
    "knowledge base using natural-language similarity matching."
)