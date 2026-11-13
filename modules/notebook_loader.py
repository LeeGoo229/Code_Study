"""
notebook_loader.py
Jupyter Notebook (.ipynb) 파싱 및 단원별 이론/실습/정답 로더
"""

import json
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

def load_theory_content(unit_info: Dict[str, Any]) -> str:
    """이론 노트북의 내용을 읽어 Markdown 문자열로 변환"""
    if unit_info.get("type") == "html_md":
        md_path = unit_info.get("md_path")
        if md_path and md_path.exists():
            return md_path.read_text(encoding="utf-8")
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
            md_parts.append(text)
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
                "description": src,
                "starter_code": starter_code,
                "solution_code": solution_code,
                "interpretation": interpretation
            })
            
    return {
        "setup_code": setup_code,
        "questions": questions,
        "data_dir": str(unit_info.get("data_dir", ""))
    }
