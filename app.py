import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_page_config(page_title="촉매 반응 시뮬레이션", layout="centered")

st.title("🧪 촉매 반응 실험 시뮬레이션")
st.markdown("모든 시험관에는 **3% 과산화수소수와 주방세제 3스푼**이 들어 있어요.")
st.markdown("하나의 시험관에 특정 물질을 넣고 반응을 관찰해보세요!")

# 시험관 초기 이미지
st.image("https://cdn.pixabay.com/photo/2017/03/24/07/28/test-tube-2178490_1280.png", caption="시험관 5개 (시작 전)", use_column_width=True)

# 촉매 종류와 반응 속도
catalyst_options = {
    "인산": 0.0,
    "아이오딘화 칼륨": 1.0,
    "이산화 망가니즈": 1.2,
    "썰은 감자": 0.8,
    "아무것도 넣지 않음": 0.0
}

# 사용자 선택
st.markdown("### ⬇️ 어떤 물질을 시험관에 넣을까요?")
catalyst = st.selectbox("물질 선택", list(catalyst_options.keys()))
start = st.button("🚀 실험 시작")

if start:
    st.subheader(f"🔍 '{catalyst}' 을(를) 시험관에 넣었습니다!")

    rate = catalyst_options[catalyst]
    chart_area = st.empty()
    progress = st.progress(0)
    reaction_start = time.time()

    if rate > 0:
        # 반응 있음: 거품 gif 출력
        st.success("✅ 반응이 일어났어요! 거품이 부풀어오르고 있어요.")
        st.image("https://media.giphy.com/media/3o6Mbl0jVekWqWrC2w/giphy.gif", caption="거품 생성 중!", use_column_width=True)

        # 반응 속도 그래프
        x_vals, y_vals = [], []
        for t in range(1, 11):
            x_vals.append(t)
            y_vals.append(rate * t + np.random.normal(0, 0.2))
            fig, ax = plt.subplots()
            ax.plot(x_vals, y_vals, marker='o', color='green')
            ax.set_xlabel("시간 (초)")
            ax.set_ylabel("거품 생성량 (ml)")
            ax.set_title("⏱️ 반응 속도 그래프")
            chart_area.pyplot(fig)
            progress.progress(t * 10)
            time.sleep(0.2)

        st.info(f"🕒 총 반응 시간: {round(time.time() - reaction_start, 2)}초")

    else:
        # 반응 없음: 정적 이미지 출력
        st.warning("⚠️ 반응이 일어나지 않았어요. 거품이 생기지 않습니다.")
        st.image("https://cdn.pixabay.com/photo/2017/03/24/07/28/test-tube-2178490_1280.png", caption="반응 없음", use_column_width=True)

        # 반응 없음 그래프
        x_vals = list(range(0, 11))
        y_vals = [0] * 11
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, marker='o', color='gray')
        ax.set_xlabel("시간 (초)")
        ax.set_ylabel("거품 생성량 (ml)")
        ax.set_title("⛔ 반응 없음 그래프")
        chart_area.pyplot(fig)

    # 실험 다시 시작 버튼
    st.markdown("---")
    if st.button("🔁 다시 실험하기"):
        st.experimental_rerun()
