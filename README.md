\# 🐍 Personal Python Question-Answering Chatbot



A knowledge-base-driven chatbot that answers Python programming questions using natural-language similarity matching.



The project allows users to ask Python-related questions in natural language and retrieves the most relevant answer from a predefined Python knowledge base.



\---



\## 📌 Project Overview



This project implements a simple personal question-answering chatbot focused specifically on Python programming.



Instead of generating arbitrary responses, the chatbot uses a predefined collection of Python questions and answers. Natural-language questions are converted into TF-IDF vectors and compared with the knowledge base using cosine similarity.



The system returns the most relevant answer when the similarity score meets the configured confidence threshold.



\---



\## 🎯 Objectives



The main objectives are to:



1\. Build a Python-focused question-answering chatbot.

2\. Create a structured predefined Python knowledge base.

3\. Accept questions in natural language.

4\. Match user questions with relevant knowledge-base entries.

5\. Return an appropriate predefined answer.

6\. Handle unsupported questions without fabricating answers.

7\. Provide a simple interactive Streamlit interface.

8\. Test the chatbot using automated unit tests.



\---



\## 🧠 How It Works



The chatbot follows this workflow:



```text

User Question

&#x20;     ↓

Text Preprocessing

&#x20;     ↓

TF-IDF Vectorization

&#x20;     ↓

Cosine Similarity

&#x20;     ↓

Find Most Relevant Knowledge-Base Question

&#x20;     ↓

Confidence Threshold Check

&#x20;     ↓

Return Answer

