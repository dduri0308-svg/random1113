import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍱")

# 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("결정 장애 해결! 아래 버튼을 눌러 오늘 먹을 점심 메뉴를 추천받아 보세요.")

# 추천할 메뉴 리스트 (원하는 메뉴를 자유롭게 추가하거나 수정하세요)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "돈까스",
    "비빔밥",
    "짜장면",
    "짬뽕",
    "초밥",
    "파스타",
    "햄버거",
    "국밥",
    "쌀국수",
    "떡볶이",
    "부대찌개",
    "카레라이스",
]

# 버튼을 눌렀을 때 실행될 동작
if st.button("메뉴 추천받기 🎲", type="primary"):
    # 리스트에서 랜덤으로 1개 선택
    selected_menu = random.choice(lunch_menus)

    # 화면에 결과 출력 및 풍선 애니메이션 효과
    st.balloons()
    st.success(f"오늘의 추천 점심 메뉴는 **{selected_menu}**입니다! 맛있게 드세요! 😋")
