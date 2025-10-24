import streamlit as st
from openai import AzureOpenAI

# OpenAI 연결 세팅
endpoint = "https://internal-apigw-kr.hmg-corp.io/hchat-in/api/v2/01K6ET0Y7FMK2PN72HDMZ4P9W6"
api_key = "OYlOck5vnTLYUF7iE2hmeZlK2Z84bR0gLsSwC5em4zyDIpBSvzQXChRDaBopvWw"

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-10-21"
)

st.title("💬 LLM 챗봇 데모")

# 세션 상태 초기화
if "history" not in st.session_state:
    st.session_state["history"] = [
        {"role": "assistant", "content": "안녕하세요! 궁금한 점을 입력해주세요."}
    ]
if "email_mode" not in st.session_state:
    st.session_state["email_mode"] = False

# 이메일모드 토글
st.session_state["email_mode"] = st.toggle("이메일 모드", value=st.session_state["email_mode"])

# 채팅 기록 표시 함수
def display_chat():
    for msg in st.session_state["history"]:
        st.chat_message(msg["role"]).markdown(msg["content"])

# 1. 채팅 기록 표시 (최상단에서 항상 호출)
display_chat()

# 2. 채팅 입력 받고, 메시지 처리
user_input = st.chat_input("메시지를 입력하세요.")
if user_input:
    # 사용자 채팅 기록 저장
    st.session_state["history"].append({"role": "user", "content": user_input})
    
    # 이메일 모드면 프롬프트 추가
    prompt_messages = st.session_state["history"].copy()
    if st.session_state["email_mode"]:
        prompt_messages.insert(0, {
            "role": "system",
            "content": "당신은 전문가이며, 아래 요청에 대해 항상 질 높은 업무용 이메일 양식으로 답변을 작성하세요."
        })

    # 답변 받아 리스폰스 저장
    try:
        response = client.chat.completions.create(
            model="gpt-4.1",
            messages=prompt_messages
        )
        bot_message = response.choices[0].message.content
    except Exception as e:
        bot_message = f"⚠️ 오류가 발생했습니다: {str(e)}"
    # 어시스턴트 답변 대화 기록에 저장
    st.session_state["history"].append({"role": "assistant", "content": bot_message})

    # ***** 입력받으면 새로고침해서 바로 표시 *****
    st.rerun()
    

# display_chat()은 오직 코드 최상단에서 한 번만 호출!
