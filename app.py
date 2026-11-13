"""
app.py
Code Study — 파이썬 및 SQL 인터랙티브 학습 플랫폼 & 대시보드
"""

import os
import streamlit as st
import pandas as pd
from pathlib import Path

# 모듈 임포트
from modules.notebook_loader import (
    CURRICULUM,
    get_unit_by_key,
    load_theory_content,
    load_practice_and_answers,
    BASE_DIR
)
from modules.python_runner import run_python_code
from modules.sql_runner import SQLEngine, SQL_CURRICULUM
from modules.diff_viewer import generate_diff_html

# 페이지 기본 설정
st.set_page_config(
    page_title="Code Study — 파이썬 & SQL 학습 플랫폼",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 모던 CSS 스타일 주입
st.markdown("""
<style>
    /* 전체 폰트 및 여백 */
    .main { background-color: #f8fafc; }
    h1, h2, h3 { color: #0f172a; font-weight: 700; }
    
    /* 탭 디자인 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #f1f5f9;
        padding: 6px;
        border-radius: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 8px 18px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 15px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffffff !important;
        color: #2563eb !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    
    /* 카드 컴포넌트 */
    .study-card {
        background: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 16px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    /* 결과 콘솔 */
    .console-box {
        background-color: #0f172a;
        color: #38bdf8;
        padding: 14px;
        border-radius: 8px;
        font-family: monospace;
        font-size: 13px;
        white-space: pre-wrap;
    }
</style>
""", unsafe_allow_html=True)

# 세션 상태 초기화 (진도율 및 사용자 작성 코드 보존)
if "user_codes" not in st.session_state:
    st.session_state["user_codes"] = {}
if "completed_units" not in st.session_state:
    st.session_state["completed_units"] = set()
if "sql_engine" not in st.session_state:
    st.session_state["sql_engine"] = SQLEngine()

# ----------------------------------------------------
# 1. 상단 글로벌 네비게이션 (과목 전환)
# ----------------------------------------------------
top_col1, top_col2 = st.columns([3, 1])
with top_col1:
    st.title("💻 Code Study 실습 플랫폼")
    st.caption("파이썬 데이터 분석, 시각화, 기초통계 및 SQL 쿼리를 웹에서 직접 실습하고 정답을 확인하세요.")
with top_col2:
    selected_subject = st.segmented_control(
        "과목 선택",
        options=["🐍 Python 실습실", "🗄️ SQL 실습실"],
        default="🐍 Python 실습실"
    )

st.divider()

# ====================================================
# [모드 1] 🐍 Python 실습실
# ====================================================
if selected_subject == "🐍 Python 실습실":
    # 사이드바: 커리큘럼 네비게이션
    with st.sidebar:
        st.header("📚 Python 커리큘럼")
        
        categories = CURRICULUM["python"]["categories"]
        cat_names = [c["name"] for c in categories]
        selected_cat_name = st.selectbox("대단원 선택", cat_names)
        
        selected_cat = next(c for c in categories if c["name"] == selected_cat_name)
        unit_names = [u["title"] for u in selected_cat["units"]]
        selected_unit_title = st.selectbox("소단원 선택", unit_names)
        
        unit_info = next(u for u in selected_cat["units"] if u["title"] == selected_unit_title)
        
        st.markdown("---")
        # 학습 완료 체크
        is_done = unit_info["key"] in st.session_state["completed_units"]
        if st.checkbox("✅ 이 단원 학습 완료 체크", value=is_done):
            st.session_state["completed_units"].add(unit_info["key"])
        else:
            st.session_state["completed_units"].discard(unit_info["key"])
            
        # 전체 진도율 계산
        total_units = sum(len(c["units"]) for c in categories)
        done_count = len(st.session_state["completed_units"])
        progress_pct = done_count / total_units if total_units > 0 else 0
        st.write(f"📊 **전체 학습 진도율**: {done_count}/{total_units} ({int(progress_pct*100)}%)")
        st.progress(progress_pct)
        
        st.markdown("---")
        st.info("💡 **배포 안내**: GitHub에 푸시된 최신 코드로 실시간 실행 중입니다.")

    # [케이스 A] 치트시트 단원
    if unit_info.get("type") == "html_md":
        st.subheader(f"📌 {unit_info['title']}")
        cheat_tabs = st.tabs(["📄 마크다운 가이드", "🌐 원본 HTML 리포트"])
        
        with cheat_tabs[0]:
            content = load_theory_content(unit_info)
            st.markdown(content)
            
        with cheat_tabs[1]:
            html_path = unit_info.get("html_path")
            if html_path and html_path.exists():
                html_bytes = html_path.read_text(encoding="utf-8")
                st.components.v1.html(html_bytes, height=900, scrolling=True)
            else:
                st.warning("HTML 파일을 찾을 수 없습니다.")

    # [케이스 B] 일반 실습 단원 (Pandas, Visualization, Statistics)
    else:
        st.subheader(f"{selected_cat_name} ➔ {unit_info['title']}")
        
        tab_theory, tab_practice, tab_answer = st.tabs([
            "📖 1. 핵심 개념 & 이론",
            "✍️ 2. 연습문제 & 코드 실행기",
            "💡 3. 모범 답안 & 해설"
        ])
        
        # ----------------------------------------------------
        # 탭 1: 핵심 개념 & 이론
        # ----------------------------------------------------
        with tab_theory:
            with st.spinner("이론 노트북 불러오는 중..."):
                theory_md = load_theory_content(unit_info)
                st.markdown(theory_md)
                
            # 데이터 폴더 미리보기 (Pandas 단원인 경우)
            data_dir = unit_info.get("data_dir")
            if data_dir and Path(data_dir).exists():
                with st.expander("📂 제공 실습 데이터셋 목록 및 미리보기"):
                    files = list(Path(data_dir).glob("*.*"))
                    for f in files:
                        st.write(f"• `{f.name}` ({f.stat().st_size / 1024:.1f} KB)")
                        if f.suffix == ".csv":
                            try:
                                sample_df = pd.read_csv(f, nrows=5)
                                st.dataframe(sample_df, use_container_width=True)
                            except Exception:
                                pass

        # ----------------------------------------------------
        # 탭 2: 연습문제 & 코드 실행기
        # ----------------------------------------------------
        with tab_practice:
            data_bundle = load_practice_and_answers(unit_info)
            setup_code = data_bundle.get("setup_code", "")
            questions = data_bundle.get("questions", [])
            data_dir_str = data_bundle.get("data_dir", "")
            
            if not questions:
                st.warning("이 단원에 등록된 연습문제가 없습니다.")
            else:
                # 문제 선택 셀렉트박스
                q_options = [f"Q{q['id']}. {q['title']}" for q in questions]
                selected_q_label = st.selectbox("풀이할 문제를 선택하세요:", q_options)
                q_idx = int(selected_q_label.split(".")[0].replace("Q", "")) - 1
                curr_q = questions[q_idx]
                
                # 문제 지시문 카드
                st.markdown(f"""
                <div class="study-card">
                    <h4>{curr_q['title']}</h4>
                    {curr_q['description']}
                </div>
                """, unsafe_allow_html=True)
                
                # 코드 에디터
                code_key = f"code_{unit_info['key']}_{curr_q['id']}"
                if code_key not in st.session_state["user_codes"]:
                    st.session_state["user_codes"][code_key] = curr_q["starter_code"]
                    
                user_code = st.text_area(
                    "💻 나의 풀이 코드 작성:",
                    value=st.session_state["user_codes"][code_key],
                    height=200,
                    key=f"editor_{code_key}"
                )
                st.session_state["user_codes"][code_key] = user_code
                
                btn_col1, btn_col2, btn_col3 = st.columns([1.5, 1.5, 5])
                with btn_col1:
                    run_clicked = st.button("▶ 코드 실행", type="primary", use_container_width=True)
                with btn_col2:
                    if st.button("↺ 초기화", use_container_width=True):
                        st.session_state["user_codes"][code_key] = curr_q["starter_code"]
                        st.rerun()
                        
                # 실행 결과 출력
                if run_clicked:
                    st.markdown("#### 🚀 실행 결과")
                    with st.spinner("파이썬 코드를 실행 중입니다..."):
                        res = run_python_code(
                            code=user_code,
                            setup_code=setup_code,
                            data_dir=data_dir_str
                        )
                        
                        if res["success"]:
                            if res["stdout"].strip():
                                st.markdown(f'<div class="console-box">{res["stdout"]}</div>', unsafe_allow_html=True)
                            if res["dataframe"] is not None:
                                st.markdown("**출력 데이터프레임:**")
                                st.dataframe(res["dataframe"], use_container_width=True)
                            if res["figures"]:
                                st.markdown("**시각화 차트:**")
                                for fig in res["figures"]:
                                    st.pyplot(fig)
                            if not res["stdout"].strip() and res["dataframe"] is None and not res["figures"]:
                                st.success("코드가 오류 없이 성공적으로 실행되었습니다. (출력값 없음)")
                        else:
                            st.error("코드 실행 중 에러가 발생했습니다.")
                            st.code(res["error"], language="python")

        # ----------------------------------------------------
        # 탭 3: 모범 답안 & 해설
        # ----------------------------------------------------
        with tab_answer:
            data_bundle = load_practice_and_answers(unit_info)
            questions = data_bundle.get("questions", [])
            
            if not questions:
                st.info("정답지가 준비 중입니다.")
            else:
                ans_q_options = [f"Q{q['id']}. {q['title']}" for q in questions]
                ans_selected_label = st.selectbox("정답을 확인할 문제 선택:", ans_q_options, key="ans_select")
                ans_idx = int(ans_selected_label.split(".")[0].replace("Q", "")) - 1
                target_q = questions[ans_idx]
                
                st.markdown(f"### 💡 {target_q['title']} 정답 및 해설")
                
                show_ans = st.checkbox("모범 답안 코드 확인하기", value=False)
                if show_ans:
                    st.markdown("#### 📝 모범 답안 코드")
                    st.code(target_q["solution_code"], language="python")
                    
                    if target_q["interpretation"].strip():
                        st.markdown("#### 🔍 결과 해석 및 주요 체크포인트")
                        st.markdown(target_q["interpretation"])
                        
                    # 작성한 코드와 모범 답안 Diff 비교
                    code_key = f"code_{unit_info['key']}_{target_q['id']}"
                    current_user_code = st.session_state["user_codes"].get(code_key, "")
                    if current_user_code.strip():
                        with st.expander("🔍 내 작성 코드 vs 모범 답안 라인별 비교 (Diff)"):
                            diff_html = generate_diff_html(current_user_code, target_q["solution_code"])
                            st.markdown(diff_html, unsafe_allow_html=True)

# ====================================================
# [모드 2] 🗄️ SQL 실습실 (추후 확장 및 DuckDB 엔진)
# ====================================================
else:
    sql_engine = st.session_state["sql_engine"]
    
    with st.sidebar:
        st.header("🗄️ SQL 실습 데이터베이스")
        st.caption("인메모리 분석 엔진(DuckDB/SQLite)으로 작동합니다.")
        
        with st.expander("📋 고객(customers) 테이블 구조"):
            st.code("""
customer_id (INT)
name (VARCHAR)
gender (VARCHAR)
age (INT)
city (VARCHAR)
grade (VARCHAR)
join_date (DATE)
            """)
            
        with st.expander("📦 상품(products) 테이블 구조"):
            st.code("""
product_id (INT)
product_name (VARCHAR)
category (VARCHAR)
price (INT)
stock (INT)
            """)
            
        with st.expander("🛒 주문(orders) 테이블 구조"):
            st.code("""
order_id (INT)
customer_id (INT)
product_id (INT)
quantity (INT)
order_date (DATE)
status (VARCHAR)
            """)
            
        st.markdown("---")
        st.info("💡 **확장 로드맵**: 추후 `Study_SQL/` 폴더에 교재 문서를 추가하면 자동으로 커리큘럼에 등록됩니다.")

    st.subheader("🗄️ SQL 쿼리 인터랙티브 실습실")
    
    sql_q_options = [q["title"] for q in SQL_CURRICULUM]
    selected_sql_title = st.selectbox("실습할 SQL 문제를 선택하세요:", sql_q_options)
    sql_q = next(q for q in SQL_CURRICULUM if q["title"] == selected_sql_title)
    
    st.markdown(f"""
    <div class="study-card">
        {sql_q['desc']}
    </div>
    """, unsafe_allow_html=True)
    
    sql_editor_key = f"sql_code_{sql_q['id']}"
    if sql_editor_key not in st.session_state["user_codes"]:
        st.session_state["user_codes"][sql_editor_key] = sql_q["starter"]
        
    user_sql = st.text_area(
        "SQL 쿼리 작성:",
        value=st.session_state["user_codes"][sql_editor_key],
        height=180,
        key=f"editor_{sql_editor_key}"
    )
    st.session_state["user_codes"][sql_editor_key] = user_sql
    
    col1, col2, col3 = st.columns([1.5, 1.5, 5])
    with col1:
        run_sql = st.button("▶ SQL 실행", type="primary", use_container_width=True)
    with col2:
        if st.button("↺ 초기화", key="sql_reset", use_container_width=True):
            st.session_state["user_codes"][sql_editor_key] = sql_q["starter"]
            st.rerun()
            
    if run_sql:
        st.markdown("#### 📊 쿼리 실행 결과")
        res = sql_engine.run_query(user_sql)
        if res["success"]:
            st.success(f"조회 성공: 총 **{res['row_count']}건**의 레코드가 반환되었습니다.")
            st.dataframe(res["df"], use_container_width=True)
        else:
            st.error(f"SQL 오류: {res['error']}")
            
    st.divider()
    with st.expander("💡 모범 SQL 정답 쿼리 및 해설 확인"):
        st.code(sql_q["solution"], language="sql")
        st.markdown(f"**해설:** {sql_q['explanation']}")
