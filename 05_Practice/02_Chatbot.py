import streamlit as st
from openai import AzureOpenAI

endpoint = "https://internal-apigw-kr.hmg-corp.io/hchat-in/api/v2/01K6ET0Y7FMK2PN72HDMZ4P9W6"
api_key = "OYlOck5vnTLYUF7iE2hmeZlK2Z84bR0gLsSwC5em4zyDIpBSvzQXChRDaBopvWw"
MODEL_NAME = "gpt-4.1"
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-21"
)

st.set_page_config(page_title="실시간 챗봇", page_icon="🤖")
st.title("🤖 실시간 LLM 채팅 챗봇")

# 대화 기록 저장
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}
    ]

def get_completion(messages):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages
    )
    return response.choices[0].message.content

# chat message style을 위한 CSS 삽입
st.markdown("""
<style>
.user-msg {
    background-color: #DCF8C6;
    color: #222;
    padding: 10px 15px;
    border-radius: 18px 18px 5px 18px;
    margin-bottom: 10px;
    margin-left: 80px;
    max-width: 65%;
    text-align: left;
    font-size: 1.05em;
    border: 1px solid #b2dfdb;
    float: right;
    clear: both;
}
.bot-msg {
    background-color: #ececec;
    color: #222;
    padding: 10px 15px;
    border-radius: 18px 18px 18px 5px;
    margin-bottom: 10px;
    margin-right: 80px;
    max-width: 65%;
    text-align: left;
    font-size: 1.05em;
    border: 1px solid #90caf9;
    float: left;
    clear: both;
}
.clearfix { clear: both; }
</style>
""", unsafe_allow_html=True)

# 채팅 출력
with st.container():
    for chat in st.session_state.chat_history:
        if chat["role"] == "user":
            st.markdown(
                f'<div class="user-msg"><b>🙍‍♂️ 나</b><br>{chat["content"]}</div><div class="clearfix"></div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="bot-msg"><b>🤖 챗봇</b><br>{chat["content"]}</div><div class="clearfix"></div>',
                unsafe_allow_html=True
            )

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("메시지를 입력하세요.", key="user_input")
    submitted = st.form_submit_button("보내기")
    if submitted and user_input.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.spinner("챗봇이 답변을 작성중입니다..."):
            reply = get_completion(st.session_state.chat_history)
            st.session_state.chat_history.append({"role": "assistant", "content": reply})
        st.rerun()

if st.button("대화 초기화"):
    st.session_state.chat_history = [
        {"role": "assistant", "content": "안녕하세요! 무엇을 도와드릴까요?"}
    ]
    st.rerun()


