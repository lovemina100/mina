import streamlit as st
import datetime

# 1. 앱의 제목과 아이콘 설정하기
st.set_page_config(page_title="내일의 준비물 체크리스트", page_icon="🎒")

# 메인 화면 타이틀
st.title("🎒 내일의 준비물 체크리스트")
st.write("요일별 준비물을 확인하고, 가방에 챙긴 것은 체크해서 지워보세요!")

# 2. 요일별 기본 준비물 데이터 만들기 (딕셔너리 리스트 구조)
# 필요에 따라 준비물을 자유롭게 수정해보세요!
PRESETS = {
    "월요일": ["체육복", "미술 붓", "물감", "영어 교과서"],
    "화요일": ["수학 익힘책", "컴퍼스", "실내화"],
    "수요일": ["음악 리코더", "사회 프린트"],
    "목요일": ["체육복", "과학 실험 관찰 책"],
    "금요일": ["도덕 교과서", "주말 과제 공지장"]
}

# 3. 오늘 날짜를 기준으로 요일 자동으로 알아내기
# 0: 월요일, 1: 화요일, ..., 4: 금요일, 5: 토요일, 6: 일요일
days_kr = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
today_num = datetime.datetime.today().weekday()
current_day = days_kr[today_num]

# 토요일이나 일요일(주말)이면 기본값을 월요일로 설정해 주기
if current_day in ["토요일", "일요일"]:
    default_index = 0
else:
    default_index = days_kr.index(current_day)

# 4. 화면에 요일 선택 상자(Selectbox) 만들기
selected_day = st.selectbox(
    "요일을 선택하세요 👇", 
    options=["월요일", "화요일", "수요일", "목요일", "금요일"],
    index=default_index
)

st.markdown("---") # 중간 구분선

# 5. 선택한 요일의 준비물 보여주고 체크박스 기능 넣기
st.subheader(f"📅 {selected_day} 준비물 목록")

# 해당 요일의 준비물 리스트 가져오기
items = PRESETS.get(selected_day, [])

if items:
    # 스트림릿에서 체크박스 상태를 기억하기 위해 session_state(저장소) 활용
    # 요일이 바뀔 때마다 체크박스를 초기화하기 위한 고유 키(key) 설정
    for item in items:
        # 각 준비물마다 체크박스 만들기
        # 체크를 하면(True가 되면) 취소선(~~text~~)을 그어주는 효과 적용!
        if st.checkbox(item, key=f"{selected
