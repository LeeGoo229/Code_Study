"""
notebook_loader.py
Jupyter Notebook (.ipynb) 파싱 및 단원별 이론/실습/정답 로더
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

BASE_DIR = Path(__file__).resolve().parent.parent
STUDY_PY_DIR = BASE_DIR / "Study_Python"
STUDY_ANS_DIR = BASE_DIR / "Study_Python_Answer"

# 전체 커리큘럼 카탈로그
CURRICULUM = {
    "python": {
        "title": "🐍 Python 데이터 분석 실습",
        "categories": [
            {
                "id": "cheatsheet",
                "name": "📌 [0] Python Cheat Sheet",
                "units": [
                    {
                        "key": "cheatsheet_guide",
                        "title": "Python 핵심 문법 & 치트시트 가이드",
                        "type": "html_md",
                        "html_path": STUDY_PY_DIR / "[0] Python_CheatSheet" / "Python_Cheat_Sheets_Complete_Guide.html",
                        "md_path": STUDY_PY_DIR / "[0] Python_CheatSheet" / "Python_Cheat_Sheets_Complete_Guide.md"
                    }
                ]
            },
            {
                "id": "pandas",
                "name": "🐼 [2] Pandas & EDA",
                "units": [
                    {
                        "key": "pandas_1",
                        "title": "1. 데이터 확인 및 탐색 (Data Checked)",
                        "theory": STUDY_PY_DIR / "[2] Pandas" / "Pandas_1_Data_Checked.ipynb",
                        "practice": STUDY_PY_DIR / "[2] Pandas" / "Pandas_1_Data_Checked_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Pandas_1_Data_Checked_Answer.ipynb",
                        "data_dir": STUDY_PY_DIR / "[2] Pandas" / "data"
                    },
                    {
                        "key": "pandas_2",
                        "title": "2. 데이터 병합과 결합 (Merge & Concat)",
                        "theory": STUDY_PY_DIR / "[2] Pandas" / "Pandas_2_merge_concat.ipynb",
                        "practice": STUDY_PY_DIR / "[2] Pandas" / "Pandas_2_merge_concat_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Pandas_2_merge_concat_Answer.ipynb",
                        "data_dir": STUDY_PY_DIR / "[2] Pandas" / "data"
                    },
                    {
                        "key": "pandas_3",
                        "title": "3. 그룹 집계 및 피벗 (Groupby & Pivot Table)",
                        "theory": STUDY_PY_DIR / "[2] Pandas" / "Pandas_3_groupby_pivot_table.ipynb",
                        "practice": STUDY_PY_DIR / "[2] Pandas" / "Pandas_3_groupby_pivot_table_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Pandas_3_groupby_pivot_table_Answer.ipynb",
                        "data_dir": STUDY_PY_DIR / "[2] Pandas" / "data"
                    },
                    {
                        "key": "pandas_4",
                        "title": "4. 데이터 정렬 및 구조 재편 (Arrange Method)",
                        "theory": STUDY_PY_DIR / "[2] Pandas" / "Pandas_4_arrange_method.ipynb",
                        "practice": STUDY_PY_DIR / "[2] Pandas" / "Pandas_4_arrange_method_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Pandas_4_arrange_method_Answer.ipynb",
                        "data_dir": STUDY_PY_DIR / "[2] Pandas" / "data"
                    },
                    {
                        "key": "eda",
                        "title": "5. 실전 탐색적 데이터 분석 (EDA 종합)",
                        "theory": STUDY_PY_DIR / "[2] Pandas" / "EDA.ipynb",
                        "practice": STUDY_PY_DIR / "[2] Pandas" / "EDA_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "EDA_Answer.ipynb",
                        "data_dir": STUDY_PY_DIR / "[2] Pandas" / "data"
                    }
                ]
            },
            {
                "id": "visualization",
                "name": "📊 [3] Data Visualization",
                "units": [
                    {
                        "key": "vis_1",
                        "title": "1. 단일 변수 및 분포 시각화 (Distribution)",
                        "theory": STUDY_PY_DIR / "[3] Visualization" / "Visualization_1_distribution.ipynb",
                        "practice": STUDY_PY_DIR / "[3] Visualization" / "Visualization_1_distribution_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Visualization_1_distribution_Answer.ipynb"
                    },
                    {
                        "key": "vis_2",
                        "title": "2. 두 변수 간 관계 시각화 (Relationship)",
                        "theory": STUDY_PY_DIR / "[3] Visualization" / "Visualization_2_relationship.ipynb",
                        "practice": STUDY_PY_DIR / "[3] Visualization" / "Visualization_2_relationship_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Visualization_2_relationship_Answer.ipynb"
                    },
                    {
                        "key": "vis_3",
                        "title": "3. 범주형 그룹 비교 시각화 (Comparison)",
                        "theory": STUDY_PY_DIR / "[3] Visualization" / "Visualization_3_comparison.ipynb",
                        "practice": STUDY_PY_DIR / "[3] Visualization" / "Visualization_3_comparison_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Visualization_3_comparison_Answer.ipynb"
                    },
                    {
                        "key": "vis_4",
                        "title": "4. 시계열 및 추세 시각화 (Trend)",
                        "theory": STUDY_PY_DIR / "[3] Visualization" / "Visualization_4_trend.ipynb",
                        "practice": STUDY_PY_DIR / "[3] Visualization" / "Visualization_4_trend_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Visualization_4_trend_Answer.ipynb"
                    },
                    {
                        "key": "vis_5",
                        "title": "5. 텍스트 워드클라우드 & Folium 지도 (Wordcloud & Folium)",
                        "theory": STUDY_PY_DIR / "[3] Visualization" / "Visualization_5_wordcloud_folium.ipynb",
                        "practice": STUDY_PY_DIR / "[3] Visualization" / "Visualization_5_wordcloud_folium_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Visualization_5_wordcloud_folium_Answer.ipynb"
                    }
                ]
            },
            {
                "id": "statistics",
                "name": "📐 [4] Statistics",
                "units": [
                    {
                        "key": "stat_1",
                        "title": "1. 기술통계와 데이터 분포 (Descriptive)",
                        "theory": STUDY_PY_DIR / "[4] Statistics" / "Statistics_1_descriptive.ipynb",
                        "practice": STUDY_PY_DIR / "[4] Statistics" / "Statistics_1_descriptive_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Statistics_1_descriptive_Answer.ipynb"
                    },
                    {
                        "key": "stat_2",
                        "title": "2. 정규분포, Z점수, 중심극한정리 (Normal & CLT)",
                        "theory": STUDY_PY_DIR / "[4] Statistics" / "Statistics_2_normal_clt.ipynb",
                        "practice": STUDY_PY_DIR / "[4] Statistics" / "Statistics_2_normal_clt_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Statistics_2_normal_clt_Answer.ipynb"
                    },
                    {
                        "key": "stat_3",
                        "title": "3. 확률과 핵심 확률분포 (Probability)",
                        "theory": STUDY_PY_DIR / "[4] Statistics" / "Statistics_3_probability.ipynb",
                        "practice": STUDY_PY_DIR / "[4] Statistics" / "Statistics_3_probability_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Statistics_3_probability_Answer.ipynb"
                    },
                    {
                        "key": "stat_4",
                        "title": "4. 추론통계, 상관, 회귀분석 (Inference & Regression)",
                        "theory": STUDY_PY_DIR / "[4] Statistics" / "Statistics_4_inference_extension.ipynb",
                        "practice": STUDY_PY_DIR / "[4] Statistics" / "Statistics_4_inference_extension_Practice.ipynb",
                        "answer": STUDY_ANS_DIR / "Statistics_4_inference_extension_Answer.ipynb"
                    }
                ]
            }
        ]
    }
}

def get_unit_by_key(unit_key: str) -> Optional[Dict[str, Any]]:
    """유닛 키로 단원 정보 조회"""
    for category in CURRICULUM["python"]["categories"]:
        for unit in category.get("units", []):
            if unit["key"] == unit_key:
                return unit
    return None

def sanitize_markdown(text: str) -> str:
    """
    마크다운 문자열에서 불필요한 Jupyter 특화 안내문구를 정리하고,
    취소선 오류를 유발하는 물결표(~) 범위 표기를 안전한 공백 표기(' ~ ')로 정제합니다.
    """
    if not text:
        return ""
    
    # 1. Jupyter 특화 안내문구 ("셀은 실행 단위입니다...")를 웹 실습 안내로 치환/정리
    jupyter_boilerplate = (
        r"셀은 실행 단위입니다\.\s*Shift\+Enter로 한 셀씩 위에서 아래로 실행합니다\..*?"
        r"\*\*완료할 때는 계산 결과 하나와 그 의미 한 문장을 함께 남기세요\.\*\*"
    )
    web_guidance = (
        "💡 **온라인 실습 가이드:** 본 플랫폼에서는 각 문제별로 제공되는 **[✍️ 2. 연습문제 & 코드 실행기]** "
        "탭에서 코드를 작성하고 실시간으로 실행해 볼 수 있습니다. 실행 결과와 그래프를 즉시 확인하고 모범 답안과 비교해 보세요."
    )
    text = re.sub(jupyter_boilerplate, web_guidance, text, flags=re.DOTALL)
    
    # 2. 설명 전용 자료 문구 정리
    text = text.replace(
        "**설명 전용 자료:** 개념·예제·주의점을 Markdown 셀로 제공합니다. 연습문제와 빈 풀이 셀은 같은 이름의 `_Practice.ipynb`에 있습니다.",
        "**학습 안내:** 핵심 개념과 예제를 학습한 후, 상단 탭에서 실습 문제 풀이와 모범 정답 확인을 진행할 수 있습니다."
    )
    
    # 3. 물결표(~) 범위 표기 정제 (취소선 파싱 방지)
    # 3-1. 백틱 코드쌍: `C01`~`C10` -> `C01` ~ `C10`
    text = re.sub(r'(`[^`]+`)\s*~\s*(`[^`]+`)', r'\1 ~ \2', text)
    # 3-2. 따옴표쌍: 'A'~'E' -> 'A' ~ 'E'
    text = re.sub(r"(['\"][^'\"]+['\"])\s*~\s*(['\"][^'\"]+['\"])", r'\1 ~ \2', text)
    # 3-3. 숫자/단위 범위: 100원~2,000원, 1일~5일, 1~3, 159~171, 2024.01.01~02.05
    text = re.sub(r'([\d.,]+[가-힣]*)\s*~\s*([\d.,]+[가-힣]*)', r'\1 ~ \2', text)
    # 3-4. 영문 식별자: Q1~Q3
    text = re.sub(r'([A-Za-z0-9]+)\s*~\s*([A-Za-z0-9]+)', r'\1 ~ \2', text)
    # 3-5. 한글 범위: 1월~3월
    text = re.sub(r'([가-힣]+)\s*~\s*([가-힣]+)', r'\1 ~ \2', text)
    # 3-6. 대략 표기: ~37 -> 약 37
    text = re.sub(r'(^|[^\w\d`])~(\d+)', r'\1약 \2', text)
    
    return text

def load_cheat_sheet_sections(md_path: Optional[Path]) -> Dict[str, str]:
    """치트시트 마크다운 문서를 9대 주제 및 비교 가이드 섹션별로 분할하여 반환"""
    if not md_path or not md_path.exists():
        return {}
    
    text = md_path.read_text(encoding="utf-8")
    
    section_patterns = [
        ("1. 🐍 Core Python", r'(<span id="sec-1"></span>\s*\n## 1\. 🐍 Core Python.*?(?=<span id="sec-2">|\Z))'),
        ("2. 🔢 NumPy", r'(<span id="sec-2"></span>\s*\n## 2\. 🔢 NumPy.*?(?=<span id="sec-3">|\Z))'),
        ("3. 🐼 Pandas", r'(<span id="sec-3"></span>\s*\n## 3\. 🐼 Pandas.*?(?=<span id="sec-4">|\Z))'),
        ("4. ⚡ Polars", r'(<span id="sec-4"></span>\s*\n## 4\. ⚡ Polars.*?(?=<span id="sec-5">|\Z))'),
        ("5. 🤖 Scikit-Learn", r'(<span id="sec-5"></span>\s*\n## 5\. 🤖 Scikit-Learn.*?(?=<span id="sec-6">|\Z))'),
        ("6. 🔥 PyTorch", r'(<span id="sec-6"></span>\s*\n## 6\. 🔥 PyTorch.*?(?=<span id="sec-7">|\Z))'),
        ("7. 🔶 TensorFlow & Keras", r'(<span id="sec-7"></span>\s*\n## 7\. 🔶 TensorFlow.*?(?=<span id="sec-8">|\Z))'),
        ("8. 📊 Matplotlib", r'(<span id="sec-8"></span>\s*\n## 8\. 📊 Matplotlib.*?(?=<span id="sec-9">|\Z))'),
        ("9. 🌊 Seaborn", r'(<span id="sec-9"></span>\s*\n## 9\. 🌊 Seaborn.*?(?=<span id="sec-10">|\Z))'),
        ("💡 Matplotlib vs Seaborn 비교 가이드", r'(<span id="sec-10"></span>\s*\n## 💡 Matplotlib vs Seaborn.*?\Z)'),
    ]
    
    sections = {"📖 전체 가이드북 한눈에 보기": text}
    for title, pat in section_patterns:
        m = re.search(pat, text, re.DOTALL)
        if m:
            sections[title] = m.group(1).strip()
            
    return sections

def load_theory_content(unit_info: Dict[str, Any]) -> str:
    """이론 노트북의 내용을 읽어 Markdown 문자열로 변환"""
    if unit_info.get("type") == "html_md":
        md_path = unit_info.get("md_path")
        if md_path and md_path.exists():
            return sanitize_markdown(md_path.read_text(encoding="utf-8"))
        return "치트시트 문서를 불러올 수 없습니다."
    
    theory_path = unit_info.get("theory")
    if not theory_path or not theory_path.exists():
        return "이론 설명 노트북이 존재하지 않습니다."
    
    with open(theory_path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    md_parts = []
    for cell in nb.get("cells", []):
        cell_type = cell.get("cell_type")
        source = cell.get("source", "")
        text = "".join(source) if isinstance(source, list) else source
        
        if cell_type == "markdown":
            cleaned = sanitize_markdown(text)
            if cleaned.strip():
                md_parts.append(cleaned)
        elif cell_type == "code":
            if text.strip():
                md_parts.append(f"```python\n{text}\n```")
                
    return "\n\n".join(md_parts)

def load_practice_and_answers(unit_info: Dict[str, Any]) -> Dict[str, Any]:
    """실습 문제와 정답을 파싱하여 반환"""
    practice_path = unit_info.get("practice")
    answer_path = unit_info.get("answer")
    
    if not practice_path or not practice_path.exists():
        return {"setup_code": "", "questions": []}
    
    with open(practice_path, "r", encoding="utf-8") as f:
        p_nb = json.load(f)
        
    a_nb = {}
    if answer_path and answer_path.exists():
        with open(answer_path, "r", encoding="utf-8") as f:
            a_nb = json.load(f)
            
    p_cells = p_nb.get("cells", [])
    a_cells = a_nb.get("cells", [])
    
    # 1. Setup 코드 추출 (첫 문제 전까지의 코드 셀들)
    setup_lines = []
    first_q_idx = len(p_cells)
    for i, c in enumerate(p_cells):
        src = "".join(c.get("source", ""))
        if c.get("cell_type") == "markdown" and ("## 문제" in src or "### 문제" in src):
            first_q_idx = i
            break
        if c.get("cell_type") == "code":
            code = src.strip()
            if code and not code.startswith("%pip"):
                setup_lines.append(code)
                
    setup_code = "\n\n".join(setup_lines)
    
    # 2. 문제 및 정답 추출
    questions = []
    for i in range(first_q_idx, len(p_cells)):
        c = p_cells[i]
        src = "".join(c.get("source", ""))
        
        if c.get("cell_type") == "markdown" and ("## 문제" in src or "### 문제" in src):
            # 문제 제목 추출
            title_lines = [l.strip().lstrip("#").strip() for l in src.split("\n") if "문제" in l]
            title = title_lines[0] if title_lines else f"문제 {len(questions)+1}"
            
            # 실습 시작 코드 (다음 코드 셀)
            starter_code = ""
            if i + 1 < len(p_cells) and p_cells[i+1].get("cell_type") == "code":
                starter_code = "".join(p_cells[i+1].get("source", ""))
                
            # 정답지에서 매칭되는 코드 및 해석 추출
            solution_code = ""
            interpretation = ""
            if i + 1 < len(a_cells) and a_cells[i+1].get("cell_type") == "code":
                solution_code = "".join(a_cells[i+1].get("source", ""))
            if i + 2 < len(a_cells) and a_cells[i+2].get("cell_type") == "markdown":
                interpretation = "".join(a_cells[i+2].get("source", ""))
                
            questions.append({
                "id": len(questions) + 1,
                "title": title,
                "description": sanitize_markdown(src),
                "starter_code": starter_code,
                "solution_code": solution_code,
                "interpretation": sanitize_markdown(interpretation)
            })
            
    return {
        "setup_code": setup_code,
        "questions": questions,
        "data_dir": str(unit_info.get("data_dir", ""))
    }
