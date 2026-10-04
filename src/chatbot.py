import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class PythonChatbot:
    """Knowledge-base question-answering chatbot for Python topics."""

    def __init__(self, knowledge_base_path, confidence_threshold=0.25):
        self.knowledge_base_path = knowledge_base_path
        self.confidence_threshold = confidence_threshold

        self.knowledge_base = pd.read_csv(knowledge_base_path)

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2)
        )

        self.question_vectors = self.vectorizer.fit_transform(
            self.knowledge_base["question"]
        )

    def answer_question(self, user_question):
        """Find and return the most relevant answer from the knowledge base."""

        if not user_question or not user_question.strip():
            return {
                "answer": "Please enter a Python-related question.",
                "category": "Input",
                "confidence": 0.0,
                "matched_question": None
            }

        query_vector = self.vectorizer.transform([user_question])

        similarity_scores = cosine_similarity(
            query_vector,
            self.question_vectors
        ).flatten()

        best_index = similarity_scores.argmax()
        best_score = float(similarity_scores[best_index])

        matched_row = self.knowledge_base.iloc[best_index]

        if best_score < self.confidence_threshold:
            return {
                "answer": (
                    "I couldn't find a sufficiently relevant answer "
                    "in my Python knowledge base. "
                    "Please try asking about a Python topic such as "
                    "lists, functions, loops, dictionaries, classes, "
                    "exceptions, or file handling."
                ),
                "category": "Unknown",
                "confidence": best_score,
                "matched_question": None
            }

        return {
            "answer": matched_row["answer"],
            "category": matched_row["category"],
            "confidence": best_score,
            "matched_question": matched_row["question"]
        }