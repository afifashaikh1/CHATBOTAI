from transformers import pipeline

def load_qa():
    return pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def get_answer(question, context, qa_pipeline):
    result = qa_pipeline(question=question, context=context)
    return result['answer']
