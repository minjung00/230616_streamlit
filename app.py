import streamlit as st # streamlit -> import (가져오기) -> as (st이름)
# st라는 변수명으로 streamlit의 기능들을 사용하겠다.

# st. -> ctrl + space -> 다양한 기능(함수, 메소드)를 가지고 있다

st.title("나의 파이썬 웹 페이지")
st.header("수업 8일차에 만들었어요!")
st.subheader("그래도 잘 만들었죠?")
st.write("내가 만든 페이지")
st.video("https://www.youtube.com/watch?v=SaCheA6Njc4") # 유튜브 링크
st.image("https://cdn.pixabay.com/photo/2023/06/02/14/12/woman-8035772_1280.jpg")  # 인터넷 링크
st.image("https://i.imgur.com/QzWz9JO.png")  # 인터넷 링크
st.image("img/img2.png")  # 파일 경로 (app.py)
st.image(image="img/img2.png")  # 키워드를 사용해서...
st.image("img/img2.png", use_column_width=True)  # 파일 경로 (app.py)
st.image("img/img2.png", width=100)  # 파일 경로 (app.py)
# https://imgur.com/

#streamlit run app.py
