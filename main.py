import streamlit as st
import datetime

# 1. 앱 페이지의 제목과 아이콘 설정 (웹 브라우저 탭에 보여요)
st.set_page_config(page_title="내일의 준비물 체크리스트", page_icon="🎒")

# 메인 화면 큰 제목 작성
st.title("🎒 내일의 준비물 체크리스트")
st.write("요일별 준비물을 확인하고, 가방에 챙긴 것은 체크해서 지워보세요!")

# 2. [리스트 & 딕셔너리] 요일별 기본 준비물 데이터 저장소 만들기
# 친구들의 실제 준비물에 맞게 아래 글자들을 자유롭게 바꿔보세요!
PRESETS = {
    "월요일": ["체육복", "미술 붓", "물감", "영어 교과서"],
    "화요일": ["수학 익힘책", "컴퍼스", "실내화"],
    "수요일": ["음악 리코더", "사회 프린트"],
    "목요일": ["체육복", "과학 실험 관찰 책"],
    "금요일": ["도덕 교과서", "주말 과제 공지장"]
}

# 3. [날짜 기능] 오늘 날짜를 기준으로 현재 요일을 자동으로 계산하기
# 시스템은 요일을 0(월) ~ 6(일) 숫자로 알려주므로 한국어 이름으로 바꿔줍니다.
days_kr = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
today_num = datetime.datetime.today().weekday()
current_day = days_kr[today_num]

# 만약 오늘이 주말(토, 일)이라면 월요일 준비물을 기본으로 보여주도록 설정
if current_day in ["토요일", "일요일"]:
    default_index = 0
else:
    default_index = days_kr.index(current_day)

# 4. [선택 상자] 화면에 요일을 고를 수 있는 드롭다운 메뉴 만들기
selected_day = st.selectbox(
    "요일을 선택하세요 👇", 
    options=["월요일", "화요일", "수요일", "목요일", "금요일"],
    index=default_index # 오늘 요일이 자동으로 먼저 선택되어 있어요
)

st.markdown("---") # 화면에 깔끔한 구분선 그리기

# 5. [체크박스 기능] 선택한 요일의 준비물 목록 보여주기
st.subheader(f"📅 {selected_day} 준비물 목록")

# 사용자가 선택한 요일의 준비물 리스트를 딕셔너리에서 꺼내옵니다.
items = PRESETS.get(selected_day, [])

if items:
    # 반복문(for)을 사용해서 준비물을 하나씩 꺼내어 체크박스로 만듭니다.
    for item in items:
        # 각 체크박스마다 고유한 이름(key)을 부여해야 스트림릿이 꼬이지 않아요.
        # 체크박스를 누르면 True가 되어 if문 안의 코드가 실행됩니다!
        if st.checkbox(item, key=f"{selected_day}_{item}"):
            # 체크했을 때: 글자에 취소선(~~글자~~)을 그어 지워진 것처럼 보이게 합니다.
            st.write(f"🍏 ~~{item} 챙기기 완료!~~")
        else:
            # 체크 안 했을 때: 아직 안 챙겼다는 표시를 해줍니다.
            st.write(f"❌ **{item}** 챙겨야 해요!")
else:
    st.write("🎉 선택한 요일에는 특별한 준비물이 없습니다!")

# 6. 하단에 나만의 응원 메시지 구역
st.markdown("---")
st.caption("💡 가방을 완벽하게 다 챙겼다면 내일도 활기찬 하루 보내세요!")
