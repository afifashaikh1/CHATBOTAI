from transformers import pipeline

# Load summarizer model
def load_summarizer():
    return pipeline("summarization", model="t5-base", tokenizer="t5-base", device=-1)

summarizer = load_summarizer()

# Function to summarize text
def summarize_text(text):
    summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
    return summary[0]["summary_text"]
