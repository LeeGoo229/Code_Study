# 💻 Code Study — 인터랙티브 코딩 & 데이터 분석 학습 플랫폼

> **Python 데이터 분석 & 시각화 & 기초 통계 & SQL 쿼리 실습을 한곳에서 제공하는 인터랙티브 웹 대시보드**
>
> 🌐 **GitHub Repository**: [https://github.com/LeeGoo229/Code_Study](https://github.com/LeeGoo229/Code_Study)

---

## 🌟 주요 특징

1. **원스톱 인터랙티브 학습 환경 (Zero-Setup)**:
   - 로컬에 Python이나 Jupyter Notebook을 설치하지 않아도, 웹 브라우저에서 바로 **이론 학습 ➔ 문제 풀이 ➔ 실시간 코드 실행 ➔ 모범 답안 비교**가 가능합니다.
2. **검증된 주피터 노트북 84종 완벽 연동**:
   - `Study_Python`의 핵심 개념과 연습문제(`_Practice.ipynb`), 그리고 `Study_Python_Answer`의 모범 답안(`_Answer.ipynb`)이 실시간 동기화됩니다.
3. **인메모리 SQL 실습실 (DuckDB/SQLite 내장)**:
   - 복잡한 데이터베이스 서버 설치 없이도 브라우저에서 바로 `SELECT`, `JOIN`, `GROUP BY` 등 실전 SQL 쿼리를 실행하고 결과를 데이터프레임으로 확인할 수 있습니다.
4. **라인별 코드 Diff 비교**:
   - 내가 작성한 코드와 모범 답안을 한눈에 비교해 다른 점과 개선점을 파악할 수 있습니다.
5. **학습 진도율 관리**:
   - 단원별 완료 체크박스와 실시간 프로그레스 바를 지원합니다.

---

## 📚 커리큘럼 구성

```text
Code_Study/
├── app.py                      # 메인 Streamlit 웹 대시보드
├── requirements.txt            # 클라우드 배포용 의존성 목록
├── modules/
│   ├── notebook_loader.py      # .ipynb 파서 및 커리큘럼 카탈로그
│   ├── python_runner.py        # 파이썬 코드 안전 실행 & 시각화/표 캡처
│   ├── sql_runner.py           # DuckDB/SQLite 인메모리 쿼리 엔진
│   └── diff_viewer.py          # 사용자 코드 vs 정답 비교 (Diff Viewer)
│
├── Study_Python/               # [학습자용/업로드용] 교재 및 실습 문제
│   ├── [0] Python_CheatSheet/  # Python 핵심 문법 가이드 (HTML / MD / PDF)
│   ├── [1] Numpy/              # Numpy 핵심 문제지 및 정답지
│   ├── [2] Pandas/             # 데이터 로드, 병합, 피벗, 정렬, EDA 실습 (데이터셋 포함)
│   ├── [3] Visualization/      # Seaborn, Matplotlib, Folium 지도 시각화
│   └── [4] Statistics/         # 기술통계, 정규분포/CLT, 확률, 통계적 추론
│
├── Study_Python_Answer/        # [관리자용/정답] 모든 실습의 모범 정답지 (.ipynb)
│
└── Study_SQL/                  # [추후 확장] SQL 학습 자료 및 문제
```

---

## 🚀 배포 및 로컬 실행 방법

### 1. Streamlit Community Cloud를 통한 무료 웹 호스팅 (추천)

1. [Streamlit Community Cloud](https://share.streamlit.io/)에 접속하여 GitHub 계정으로 로그인합니다.
2. **`New app`** 버튼을 클릭합니다.
3. 설정 입력:
   - **Repository**: `LeeGoo229/Code_Study`
   - **Branch**: `main`
   - **Main file path**: `app.py`
   - **App URL**: 원하는 도메인 입력 (예: `code-study.streamlit.app`)
4. **`Deploy!`** 버튼을 클릭하면 1~2분 내에 고유 URL이 발급되며 누구나 접속할 수 있습니다.
5. 이후 GitHub에 `git push`할 때마다 웹사이트가 자동으로 업데이트됩니다.

### 2. 로컬(Local)에서 실행하기

```bash
# 1. 리포지토리 클론
git clone https://github.com/LeeGoo229/Code_Study.git
cd Code_Study

# 2. 가상환경 생성 및 패키지 설치
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 3. 대시보드 실행
streamlit run app.py
```

브라우저가 자동으로 열리며 `http://localhost:8501`에서 대시보드를 사용할 수 있습니다.

---

## ☁️ Google Drive 연동 구조 (`Study_code`)

Google Drive의 특정 폴더인 **`Study_code`** 내부는 용도에 따라 3개로 명확히 분리 관리됩니다:

| 구분 | Google Drive 폴더명 | 설명 | 포함 내용 |
| :--- | :--- | :--- | :--- |
| **[1] 업로드용** | `업로드용` | 학습자 공유 및 대외 배포용 | `Study_Python` (치트시트, 실습 문제, 데이터셋) |
| **[2] 관리용** | `관리용` | 관리자 및 소스 코드 관리용 | `Study_Python_Answer` (모범 답안 노트북) |
| **[3] 백업용** | `백업용` | 원본 불변 보존 백업용 | `Study_Python_Backup` (최초 원본 아카이브) |

---

## 📈 추후 SQL 확장 가이드

- `modules/sql_runner.py`에 DuckDB 기반 인메모리 테이블(`customers`, `products`, `orders`)이 기본 구성되어 있습니다.
- 새로운 SQL 실습 문제를 추가하려면 `modules/sql_runner.py`의 `SQL_CURRICULUM` 리스트에 문제 제목, 설명, 템플릿 쿼리, 모범 정답을 추가하면 웹 화면에 자동으로 반영됩니다.
- 향후 `Study_SQL/` 폴더에 `.ipynb` 또는 마크다운 문서를 추가하여 대단원을 확장할 수 있습니다.
