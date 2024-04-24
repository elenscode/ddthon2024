from langchain.callbacks.base import BaseCallbackHandler
from langchain.schema import ChatMessage
from langchain_openai import ChatOpenAI
import streamlit as st


class StreamHandler(BaseCallbackHandler):
    def __init__(self, container, initial_text=""):
        self.container = container
        self.text = initial_text

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        self.container.markdown(self.text)


with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    st.write('<input id="abcef" type="text">', unsafe_allow_html=True)

st.markdown(
    """
            <style>
                div[data-testid="column"] {
                    width: fit-content !important;
                    flex: unset;
                }
                div[data-testid="column"] * {
                    width: fit-content !important;
                }
            </style>
            """,
    unsafe_allow_html=True,
)
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.button("button1")
with col2:
    st.button("button2")
with col3:
    st.button("button3")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        ChatMessage(role="assistant", content="How can I help you?")
    ]

for msg in st.session_state.messages:
    st.chat_message(msg.role).write(msg.content)

if prompt := st.chat_input():
    st.session_state.messages.append(ChatMessage(role="user", content=prompt))
    st.chat_message("user").write(prompt)

    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatOpenAI(
            openai_api_key=openai_api_key, streaming=True, callbacks=[stream_handler]
        )
        response = llm.invoke(st.session_state.messages)
        st.session_state.messages.append(
            ChatMessage(role="assistant", content=response.content)
        )
