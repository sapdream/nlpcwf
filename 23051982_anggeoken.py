# -*- coding: utf-8 -*-
"""23051982_AngGeokEn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pvObLe5sxQvVVD5M-iJsM_2U96zy6IUm
"""

import streamlit as st
import transformers
from transformers import pipeline

def create_qa_bot():
    # Load the question-answering pipeline
    qa_pipeline = pipeline("question-answering")

    return qa_pipeline

def ask_question(context, question, qa_pipeline):
    # Use the pipeline to answer the question based on the context
    result = qa_pipeline(context=context, question=question)

    return result['answer']

def main():
    # Create the question-answering bot
    qa_bot = create_qa_bot()

    # Example context and questions
    context = "Hugging Face is an AI research organization that provides state-of-the-art natural language processing models."

    questions = [
        "What does Hugging Face do?",
        "Which organization provides natural language processing models?",
        "Tell me about Hugging Face.",
    ]

    st.title("Question Answering App")
    input_text = st.text_area("Input text", value="")
    
    # Ask questions and print answers
    for question in questions:
        answer = ask_question(context, input_text, qa_bot)
        st.markdown(f"A: {answer}")
        print()

if __name__ == "__main__":
    main()




