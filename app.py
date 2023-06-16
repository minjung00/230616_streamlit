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

#마크다운

# st.write / st.markdown
# st.write -> 입력하는 것에 맞춰서 알아서 결정 -> 마크다운

# 제목 마크다운
st.write("""
# 가장 큰 제목 텍스트 (h1 - headline1 -st.title)
## 그 다음 큰 제목 (h2 - headline2 -st.title)
### 그것보단 작은 제목 <- 대부분 여기까지만 사용 (h3)
#### h4
##### h5
###### h6
""")

# 서식
text = """
기울임 *별표* 또는 _언더바_ 하나씩 써주면

진하게(bold) : **별표** 또는 __언더바__ 두개씩 써주면

기울임 + 진하게(bold) : ***별표***를 세개씩 써주면

취소선 : ~물결표~

밑줄 : <u>밑줄</u>

형광펜 : <mark>형광펜</mark>
"""
#st.write(text)
st.markdown(text, unsafe_allow_html=True)


# 레이아웃
st.subheader("레이아웃")
st.write("""
    #### 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    * 별표를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        * 들여쓰기1
            * 들여쓰기2
                * 들여쓰기3
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
    - (-)를 여백 1칸 이상과 사용하면 순서가 없는 리스트
        - 들여쓰기1
            - 들여쓰기2
                - 들여쓰기3
""")
st.divider()
st.write("""
    #### 순서가 있는 리스트
    1. 순서가
    2. 있는
    4. 리스트 - 숫자를 건너 뛰어도 무시하고 순서를 따름
        1. 들여쓰기1
            1. 들여쓰기2 # 1로 시작하지 않으면 들여쓰기는 무시
                1. 들여쓰기3
    1. 순서가
    1. 1로 넣어도
    1. 증가됨
    ### 가로줄
    ---
    (---)
    ___
    (___)
    ### 테이블(표)
    |이름|직업|
    |-----|---|
    |파이썬|백수|
    |자바|일잘러|
""")

# 링크
st.divider()
st.subheader("링크")
l1 = "https://naver.com"
l2 = "https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg"
st.write(f"""
    * [표시할 텍스트](https://naver.com)
    * [표시할 텍스트]({l1})
    * ![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)
    * ![이미지에 대한 설명]({l2})
    * [![이미지에 대한 설명](https://cdn.pixabay.com/photo/2023/04/08/18/01/flower-7909902_640.jpg)](https://naver.com)
""")

# 인용
st.divider()
st.subheader("인용")
st.write(f"""
    > 무언가
    
    > 여러줄
    
    책이나, 사람말 인용할 ㅁ대...
    >> 인용문 안에 인용
    
    #### 코드
    `코드를 나타낼 때 주로 쓰이는 묶음 표시`
    ```
    여러 줄 코드
    ```
    
    ```python
    print("파이썬")
    ```
""")
