import streamlit as st
from utils.summarizer import summarize_text
from utils.quiz_generator import generate_quiz
from utils.qa_generator import answer_question

st.set_page_config(page_title="Exam Prep Chatbot", layout="wide")

# --- Initialize Session State ---
if "chat_sessions" not in st.session_state:
    st.session_state.chat_sessions = {"Chat 1": []}
if "current_chat" not in st.session_state:
    st.session_state.current_chat = "Chat 1"

# --- Sidebar (like ChatGPT left panel) ---
with st.sidebar:
    st.title("🤖 Exam Preparation Chatbot")

    if st.button("➕ New Chat"):
        new_name = f"Chat {len(st.session_state.chat_sessions)+1}"
        st.session_state.chat_sessions[new_name] = []
        st.session_state.current_chat = new_name

    st.text_input("🔍 Search", placeholder="Search chats...")

    st.markdown("### 📚 Library")
    st.markdown("- 📄 Notes")
    st.markdown("- 📘 Summaries")
    st.markdown("- ❓ Quizzes")

    st.markdown("---")
    st.markdown("⚙️ **Settings**")

    st.markdown("### 💬 History")
    for name in list(st.session_state.chat_sessions.keys()):
        if st.button(name):
            st.session_state.current_chat = name

# --- Get Current Chat ---
chat_history = st.session_state.chat_sessions[st.session_state.current_chat]

# --- Main Chat Window ---
st.markdown("### Study Material")

col1, col2 = st.columns([10, 1])
with col1:
    user_input = st.text_input(
        "Ask anything...",
        placeholder="Ask anything...",
        label_visibility="collapsed"
    )
with col2:
    send = st.button("➤", use_container_width=True)

# --- Handle Input (Q&A flow) ---
if send and user_input:
    chat_history.append({"role": "user", "text": user_input})
    answer = answer_question(user_input, user_input)
    chat_history.append({"role": "assistant", "text": answer})
    st.rerun()

# --- Display Conversation ---
for chat in chat_history:
    if chat["role"] == "user":
        st.markdown(f"🧑 **You:** {chat['text']}")
    elif chat["role"] == "assistant":
        st.markdown(f"🤖 **AI:** {chat['text']}")

# --- Action Buttons ---
colA, colB = st.columns(2)
with colA:
    if st.button("Generate Summary"):
        if chat_history:
            last_input = chat_history[-1]["text"]
            summary = summarize_text(last_input)
            chat_history.append({"role": "assistant", "text": summary})
            st.rerun()
        else:
            st.warning("Please enter some study material first!")

with colB:
    if st.button("Generate Questions"):
        if chat_history:
            last_input = chat_history[-1]["text"]
            quiz = generate_quiz(last_input)
            quiz_text = "\n".join([f"Q{i+1}: {q}" for i, q in enumerate(quiz)])
            chat_history.append({"role": "assistant", "text": quiz_text})
            st.rerun()
        else:
            st.warning("Please enter some study material first!")
