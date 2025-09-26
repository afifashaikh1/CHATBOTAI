from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load model and tokenizer once
def load_quiz_generator():
    model_name = "iarfmoose/t5-base-question-generator"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_quiz_generator()

# Function to generate quiz questions
def generate_quiz(text, num_questions=5):
    inputs = tokenizer.encode(
        "generate questions: " + text,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )

    outputs = model.generate(
        inputs,
        max_length=64,
        num_return_sequences=num_questions,
        do_sample=True,
        top_k=50,
        top_p=0.95
    )

    questions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return questions
