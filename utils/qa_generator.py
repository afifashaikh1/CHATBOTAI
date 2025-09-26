# utils/qa_generator.py
from transformers import pipeline

def load_qa_pipeline():
    # Use a lightweight model for Q&A
    return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question, context):
    qa = load_qa_pipeline()
    result = qa(question=question, context=context)
    return result["answer"]
