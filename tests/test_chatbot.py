from src.chatbot import PythonChatbot


KNOWLEDGE_BASE = "data/python_knowledge_base.csv"


def test_python_question():
    chatbot = PythonChatbot(KNOWLEDGE_BASE)

    result = chatbot.answer_question("What is Python?")

    assert result["category"] == "Basics"
    assert result["confidence"] > 0.25
    assert result["matched_question"] == "What is Python?"


def test_list_question():
    chatbot = PythonChatbot(KNOWLEDGE_BASE)

    result = chatbot.answer_question("What is a list?")

    assert result["category"] == "Data Structures"
    assert result["confidence"] > 0.25


def test_function_question():
    chatbot = PythonChatbot(KNOWLEDGE_BASE)

    result = chatbot.answer_question("How do I create a function?")

    assert result["category"] == "Functions"
    assert result["confidence"] > 0.25


def test_unsupported_question():
    chatbot = PythonChatbot(KNOWLEDGE_BASE)

    result = chatbot.answer_question(
        "What is machine learning?"
    )

    assert result["category"] == "Unknown"
    assert result["matched_question"] is None