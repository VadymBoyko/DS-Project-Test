import streamlit as st
import datetime


# get Q and generate A
def chat_with_llm(user_message, conversation_history=[]):

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation_history.append({"role": "user", "content": user_message, "time": current_time})

    # method for get a A
    llm_response = 'Answer for ' + user_message

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation_history.append({"role": "system", "content": llm_response, "time": current_time})

    return llm_response, conversation_history


st.title("LLM Q&A")

uploaded_file = st.sidebar.file_uploader("Choose a file", type=["txt", "pdf"])

user_message = st.sidebar.text_input("Type your message:")

conversation_history = st.session_state.get("conversation_history", [])

# Ask button
if st.sidebar.button("Ask") and user_message:
    llm_response, conversation_history = chat_with_llm(user_message, conversation_history)
    user_message = ""

# Show history
st.subheader("Chat History:")
for message in reversed(conversation_history):
    if message["role"] == "user":
        st.write(f"{message['time']} - **You:** {message['content']}")
    else:
        st.write(f"{message['time']} - **LLM:** {message['content']}")

# Якщо файл завантажений
if uploaded_file is not None:
    st.subheader("Uploaded File:")
    if uploaded_file.type == "text/plain":
        text = uploaded_file.read()
        st.write(text)
    elif uploaded_file.type == "application/pdf":
        text = uploaded_file.read()
    else:
        st.write("File type is not supported.")

# Save history
st.session_state["conversation_history"] = conversation_history
