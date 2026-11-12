# 🐍 Python & AI/Data Science 핵심 치트시트 완벽 가이드북

**Python 및 8대 핵심 데이터 사이언스·AI 라이브러리(NumPy, Pandas, Polars, Scikit-Learn, PyTorch, TensorFlow, Matplotlib, Seaborn)** 치트시트 카드 9종의 전체 내용과 실전 예제, 동작 원리를 체계적으로 정리한 학습 문서입니다.

---

## 📂 수록 치트시트 목록

1. **[Core Python](#1--core-python-치트시트-기초-문법-및-핵심-개념)** (변수, 자료형, 컬렉션, 제어문, 함수, 클래스, 가상환경 등)
2. **[NumPy](#2--numpy-치트시트-고성능-다차원-수치-계산)** (배열 생성, 형태 변환, 브로드캐스팅, 통계 집계, 행렬 연산 등)
3. **[Pandas](#3--pandas-치트시트-데이터-조작-및-분석)** (데이터 입출력, 필터링, 그룹 집계, 병합, 결측치 처리, 불리언 마스킹 등)
4. **[Polars](#4--polars-치트시트-차세대-초고속-데이터프레임)** (Rust 기반 초고속 연산, 지연 실행 LazyFrame, 표현식 등)
5. **[Scikit-Learn](#5--scikit-learn-치트시트-전통적-머신러닝-파이프라인)** (전처리, 모델 학습, 교차 검증, 하이퍼파라미터 튜닝, 전체 워크플로우)
6. **[PyTorch](#6--pytorch-치트시트-동적-신경망-및-딥러닝)** (텐서 연산, Autograd 자동 미분, 신경망 설계, 학습 및 추론 루프)
7. **[TensorFlow & Keras](#7--tensorflow--keras-치트시트-엔터프라이즈-ai--배포)** (tf.data 파이프라인, 모델 빌드, 조기 종료, TFLite 변환)
8. **[Matplotlib](#8--matplotlib-치트시트-데이터-시각화)** (플롯 유형, 서브플롯, 스타일링, 고해상도 저장 및 출력)
9. **[Seaborn](#9--seaborn-치트시트-통계적-데이터-시각화)** (통계 차트, 범주형/분포형 플롯, 히트맵, 페어플롯, 테마 & 팔레트)

---

## 1. 🐍 Core Python 치트시트 (기초 문법 및 핵심 개념)

![Core Python](./slides/slide_1.jpg)

### 핵심 문법 정리표
| 항목 | 문법 / 코드 | 상세 설명 |
| :--- | :--- | :--- |
| **Variables** | `x = 10` | 변수 선언 시 데이터 타입을 명시하지 않아도 인터프리터가 자동으로 타입을 추론하여 메모리를 할당합니다. |
| **Data Types** | `int, float, str, bool, list, dict, set, tuple` | 파이썬의 표준 기본 자료형 및 기본 컬렉션 컨테이너입니다. |
| **List** | `nums = [1, 2, 3]` | 순서가 있고(Ordered) 자유롭게 요소를 수정/추가/삭제(Mutable)할 수 있는 동적 배열입니다. |
| **Tuple** | `t = (1, 2, 3)` | 수정 불가능한(Immutable) 읽기 전용 시퀀스로, 딕셔너리의 키나 함수의 다중 반환값으로 유용합니다. |
| **Set** | `s = {1, 2, 3}` | 중복을 허용하지 않고 순서가 없는 집합으로, 집합 연산(교/합/차집합)과 $O(1)$ 속도의 포함 여부 검사에 최적화되어 있습니다. |
| **Dictionary** | `d = {"key": "value"}` | Key-Value 매핑 구조로, 키를 통해 값을 $O(1)$ 시간 복잡도로 빠르게 검색할 수 있습니다. |
| **If / Elif / Else** | `if x > 0: ... elif x == 0: ...` | 들여쓰기(Indentation, 통상 공백 4칸)를 블록 단위로 사용하여 다중 조건을 분기합니다. |
| **For Loop** | `for i in range(5): ...` | `range(시작, 종료, 간격)`나 이터러블 객체를 순차적으로 순회합니다. |
| **While Loop** | `while condition: ...` | 특정 불리언 조건식이 `True`인 동안 블록을 반복 실행합니다. |
| **Functions** | `def add(a, b): return a + b` | `def` 키워드로 함수를 정의하며, 기본값 인자(Default argument) 지정도 가능합니다. |
| **Lambda** | `square = lambda x: x**2` | 별도의 함수 정의 없이 한 줄로 표현하는 익명 함수로, 정렬 키나 고차 함수의 인자로 자주 쓰입니다. |
| **List Comprehension** | `squares = [x**2 for x in nums]` | 반복문과 조건문을 축약하여 새 리스트를 매우 간결하고 빠르게 생성하는 파이써닉한 기법입니다. |
| **Exception Handling** | `try: ... except Exception as e: ...` | 예외 발생 가능성이 있는 코드를 감싸 런타임 오류 시에도 프로그램이 비정상 종료되지 않도록 방어합니다. |
| ***args / \*\*kwargs** | `def func(*args, **kwargs): ...` | `*args`는 튜플 형태로 임의 개수의 위치 인수를, `**kwargs`는 딕셔너리 형태로 임의의 키워드 인수를 수신합니다. |
| **Classes** | `class Person: def __init__(self, name): self.name = name` | 객체지향 프로그래밍의 기초 단위로, `__init__` 생성자를 통해 인스턴스 멤버 변수를 초기화합니다. |
| **Modules** | `import math`, `from datetime import datetime` | 외부 파일 또는 표준 라이브러리의 함수와 클래스를 네임스페이스로 가져와 재사용합니다. |
| **map()** | `list(map(int, ["1", "2", "3"]))` | 컬렉션의 모든 요소에 지정된 변환 함수를 일괄 적용합니다. |
| **filter()** | `list(filter(lambda x: x > 0, nums))` | 조건 함수(Predicate)가 `True`를 반환하는 요소만 걸러냅니다. |
| **zip()** | `list(zip([1, 2], ["a", "b"]))` | 길이가 같은 여러 개의 시퀀스를 인덱스별로 묶어 튜플 형태로 반환합니다. |
| **File Handling** | `with open("file.txt", "r") as f: data = f.read()` | 컨텍스트 매니저(`with`)를 사용해 파일 작업 완료 시 자동으로 `close()`를 호출하여 자원 누수를 방지합니다. |
| **Virtual Environment** | `python -m venv venv` | 프로젝트별 패키지 의존성 충돌을 방지하기 위해 독립된 파이썬 가상환경을 생성합니다. |

---

## 2. 🔢 NumPy 치트시트 (고성능 다차원 수치 계산)

![NumPy](./slides/slide_2.jpg)

### 핵심 코드 및 기능
```python
import numpy as np

# 1. 배열 생성
np.array([1, 2, 3])         # 기본 1D/2D 배열 생성
np.zeros((2, 3))             # 2x3 영행렬
np.ones((2, 3))              # 2x3 1행렬
np.arange(0, 10, 2)          # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)         # 0부터 1까지 균등한 간격으로 5개 값 생성
np.random.rand(2, 3)         # 0~1 사이의 균일 분포 난수 배열
np.eye(3)                    # 3x3 단위 행렬 (Identity Matrix)

# 2. 형상(Shape) 및 속성
arr = np.array([[1, 2, 3], [4, 5, 6]])
arr.shape                    # (2, 3)
arr.reshape((3, 2))          # 형상 재배치 (총 원소 수 일치 필요)
arr.ndim                     # 차원 수 (2)
arr.dtype                    # 데이터 타입 (예: int64, float32)

# 3. 인덱싱 & 슬라이싱 & 불리언 마스킹
arr[0, 1]                    # 0행 1열 원소 (2)
arr[1:4]                     # 슬라이스 추출
arr[arr > 0]                 # 조건 필터링 (Boolean Masking)

# 4. 브로드캐스팅 & 행렬 연산
arr + 5                      # 루프 없이 모든 요소에 5를 더함
A @ B                        # 행렬 곱셈 (Matrix Multiplication)

# 5. 통계 및 집계 함수
np.sum(arr)                  # 원소 전체 합
np.mean(arr)                 # 평균
np.std(arr)                  # 표준편차
np.min(arr) / np.max(arr)    # 최솟값, 최댓값
np.argmax(arr)               # 최대 원소의 인덱스

# 6. 결합 및 분할
np.concatenate((a, b))       # 배열 결합
np.vstack((a, b))            # 수직(행) 스택
np.split(arr, 3)             # 3개 파트로 균등 분할
```

---

## 3. 🐼 Pandas 치트시트 (데이터 조작 및 분석)

![Pandas](./slides/slide_3.jpg)

### 주요 기능별 사용법
```python
import pandas as pd

# 1. 데이터 입출력 및 탐색
df = pd.read_csv('file.csv') # CSV 파일 읽기
df.head()                    # 처음 5개 행 미리보기
df.info()                    # 열 이름, 결측치 유무, 데이터 타입 요약
df.describe()                # 수치 컬럼 통계 요약 (평균, 사분위수 등)
df.shape                     # (행 수, 열 수)
df.columns                   # 컬럼 리스트
df.dtypes                    # 각 컬럼의 자료형

# 2. 열 선택 및 조건 필터링
df['col']                    # 단일 컬럼 선택 (Series)
df[['col1', 'col2']]         # 다중 컬럼 선택 (DataFrame)
df[df['col'] > 10]           # 단일 조건 행 필터링
df[(df['A'] > 5) & (df['B'] < 10)] # 다중 조건 불리언 마스킹 (Boolean Masking)
df.sort_values('col', ascending=False) # 내림차순 정렬

# 3. 그룹화 및 집계
df.groupby('col')
df.groupby('col')['value'].agg(['sum', 'mean']) # 다중 집계 함수 적용
df.pivot_table(values='val', index='A', columns='B', aggfunc='sum')

# 4. 결합 및 조인
pd.merge(df1, df2, on='id', how='inner') # SQL 스타일 조인
pd.concat([df1, df2], axis=0)            # 행 방향 수직 결합

# 5. 데이터 정제 및 변환
df.drop(columns=['col'])     # 컬럼 삭제
df.rename(columns={'old': 'new'}) # 컬럼명 변경
df.fillna(value) / df.dropna()    # 결측치 대체 및 제거
df['col'].apply(lambda x: x * 2)  # 커스텀 함수 적용
df['col'].value_counts()     # 범주별 출현 빈도수
df['col'].unique()           # 고유값(Unique Values) 추출
pd.to_datetime(df['date'])   # 날짜 시간 타입 변환
df['col'].str.lower()        # 문자열 소문자 변환 (.upper(), .contains() 등)
```

---

## 4. ⚡ Polars 치트시트 (차세대 초고속 데이터프레임)

![Polars](./slides/slide_4.jpg)

### 핵심 개념 및 문법
```python
import polars as pl

# 1. 데이터 입출력 및 생성
df = pl.read_csv('data.csv')
df = pl.read_parquet('data.parquet')
df = pl.DataFrame({"name": ["A", "B"], "score": [90, 85]})

# 2. 데이터 탐색
df.head()                    # 상위 5개 행
df.shape                     # (행 수, 열 수)
df.schema                    # 컬럼 이름 및 데이터 타입

# 3. 컬럼 선택, 필터링, 정렬 (Expression 중심 문법)
df.select(["name", "score"])
df.filter(pl.col("score") > 80)
df.sort("score", descending=True)

# 4. 컬럼 추가/수정 (with_columns) & 집계
df.with_columns((pl.col("score") * 1.1).alias("boosted"))
df.group_by("team").agg(pl.col("score").mean().alias("avg_score"))

# 5. 조인 및 결측치 처리
df.join(df2, on="id", how="inner")
pl.concat([df1, df2], how="vertical")
df.fill_null(0)
df.drop_nulls()

# 6. 초고속 지연 실행 (Lazy Execution)
result = (
    df.lazy()
    .filter(pl.col("score") > 80)
    .select("name", "score")
    .collect()
)

# 7. 데이터 저장 및 유용한 함수
df.write_csv("output.csv")
df.write_parquet("output.parquet")
df.unique()                  # 중복 제거 고유 행
df.sample(n=5)               # 무작위 표본 추출
df.describe()                # 요약 통계량 확인
```

---

## 5. 🤖 Scikit-Learn 치트시트 (전통적 머신러닝 파이프라인)

![Scikit-Learn](./slides/slide_5.jpg)

### 머신러닝 모델 구축 표준 절차 (`Load Data → Split → Preprocess → Train → Evaluate → Save`)
```python
import sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.pipeline import Pipeline
import joblib

# 1. 데이터 로드 및 분할
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 2. 파이프라인 구성 (전처리 + 모델)
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestClassifier())
])

# 3. 교차 검증 및 하이퍼파라미터 튜닝
scores = cross_val_score(pipe, X_train, y_train, cv=5)
grid = GridSearchCV(pipe, param_grid={'model__n_estimators': [50, 100]}, cv=5)
grid.fit(X_train, y_train)

# 4. 모델 평가 및 저장
y_pred = grid.predict(X_test)
acc = accuracy_score(y_test, y_pred)
joblib.dump(grid.best_estimator_, 'model.pkl')
model = joblib.load('model.pkl')
```

---

## 6. 🔥 PyTorch 치트시트 (동적 신경망 및 딥러닝)

![PyTorch](./slides/slide_6.jpg)

### PyTorch 핵심 패턴
```python
import torch

# 1. 장치 설정 및 텐서 연산
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x = torch.tensor([1, 2, 3])
zeros = torch.zeros((2, 3))
ones = torch.ones((2, 3))
matmul_res = torch.matmul(x, y) # or x @ y

# 2. 자동 미분 (Autograd)
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward()
print(x.grad) # 4.0

# 3. 신경망 아키텍처 및 옵티마이저
model = torch.nn.Sequential(
    torch.nn.Linear(10, 32),
    torch.nn.ReLU(),
    torch.nn.Linear(32, 1)
)
criterion = torch.nn.MSELoss() # or CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 4. 표준 학습 루프 (Training Loop)
for epoch in range(epochs):
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

# 5. 모델 저장, 로드 및 추론 (Inference)
torch.save(model, "model.pth")
model = torch.load("model.pth")

model.eval()
with torch.no_grad():
    preds = model(x)
```

---

## 7. 🔶 TensorFlow & Keras 치트시트 (엔터프라이즈 AI & 배포)

![TensorFlow](./slides/slide_7.jpg)

### TensorFlow / Keras 워크플로우
```python
import tensorflow as tf

# 1. 텐서 및 GPU 확인
tf.config.list_physical_devices('GPU')
x = tf.constant([1, 2, 3])
x_reshaped = tf.reshape(x, (3, 1))

# 2. 데이터 파이프라인 (tf.data)
dataset = (
    tf.data.Dataset.from_tensor_slices(x)
    .batch(32)
    .prefetch(tf.data.AUTOTUNE)
)

# 3. 모델 빌드, 컴파일 및 훈련
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=3)
model.fit(x_train, y_train, epochs=10, batch_size=32, callbacks=[early_stop])

# 4. 평가, 예측 및 TFLite 변환 배포
model.evaluate(x_test, y_test)
preds = model.predict(x_new)
tf.argmax(preds, axis=1)

model.save('model.h5')
tf.saved_model.save(model, 'saved_model')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
```

---

## 8. 📊 Matplotlib 치트시트 (데이터 시각화)

![Matplotlib](./slides/slide_8.jpg)

### 다양한 차트 생성 및 레이아웃 제어
```python
import matplotlib.pyplot as plt

# 1. 기본 차트 유형
plt.plot(x, y)               # 선 그래프 (Line Plot)
plt.bar(x, y)                # 막대 그래프 (Bar Plot)
plt.hist(data, bins=10)      # 히스토그램 (Histogram)
plt.scatter(x, y)            # 산점도 (Scatter Plot)
plt.pie(sizes, labels=labels, autopct='%1.1f%%') # 파이 차트 (Pie Chart)
plt.boxplot(data)            # 박스 플롯 (Box Plot)
plt.fill_between(x, y, color='skyblue', alpha=0.4) # 영역 차트 (Area Plot)

# 2. 서브플롯 및 스타일 제어
fig, ax = plt.subplots(2, 2, figsize=(8, 6))
plt.figure(figsize=(8, 6))
plt.title('My Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.plot(x, y, color='red', linestyle='--', marker='o', linewidth=2)

# 3. 파일 저장 및 화면 출력
plt.savefig('plot.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## 9. 🌊 Seaborn 치트시트 (통계적 데이터 시각화)

![Seaborn](./slides/slide_9.jpg)

### 주요 기능 및 API 일람표
| 기능 구분 | API 코드 문법 | 핵심 설명 및 옵션 |
| :--- | :--- | :--- |
| **설치 & 임포트** | `pip install seaborn`<br>`import seaborn as sns` | 통계적 그래픽 표현에 특화된 Matplotlib 기반 고수준 라이브러리 |
| **테마 / 스타일** | `sns.set_theme(style="whitegrid")` | 전체 차트 스타일(`whitegrid`, `darkgrid`, `ticks`, `white`) 일괄 적용 |
| **산점도 (Scatter)** | `sns.scatterplot(data=df, x='x', y='y', hue='c')` | 범주별 색상(`hue`), 마커 크기(`size`), 스타일(`style`) 자동 매핑 |
| **선 그래프 (Line)** | `sns.lineplot(data=df, x='x', y='y', errorbar='ci')` | 시계열 추세선 및 신뢰구간(Confidence Interval) 음영 자동 계산 |
| **관계형 그리드** | `sns.relplot(data=df, x='x', y='y', col='cat')` | 서브플롯을 컬럼별(`col`), 행별(`row`)로 분할 생성하는 인터페이스 |
| **막대 그래프 (Bar)** | `sns.barplot(data=df, x='cat', y='val')` | 범주별 평균값(기본값) 및 신뢰구간 오차 막대 자동 표시 |
| **빈도 막대 (Count)** | `sns.countplot(data=df, x='category')` | 범주형 데이터의 빈도수(Frequency)를 집계하여 막대 차트로 시각화 |
| **상자 그림 (Box)** | `sns.boxplot(data=df, x='cat', y='val')` | 사분위수(IQR), 중앙값, 이상치(Outlier)를 직관적으로 비교 |
| **바이올린 플롯** | `sns.violinplot(data=df, x='cat', y='val', split=True)` | 상자 그림에 커널 밀도 추정(KDE) 곡선을 결합하여 다봉 분포 표현 |
| **히스토그램** | `sns.histplot(data=df, x='val', kde=True, bins=20)` | 연속형 변수 구간별 빈도 및 KDE 곡선 동시 표출 |
| **밀도 함수 (KDE)** | `sns.kdeplot(data=df, x='val', fill=True)` | 데이터의 확률 밀도 추정 함수(Kernel Density Estimate) 부드러운 곡선 |
| **히트맵 (Heatmap)** | `sns.heatmap(df.corr(), annot=True, cmap='coolwarm')` | 상관계수 행렬 및 2차원 매트릭스 수치와 컬러맵 시각화 |
| **페어 플롯 (Pair)** | `sns.pairplot(df, hue='species', corner=True)` | 모든 수치형 변수 간의 쌍대 산점도 및 대각선 분포 일괄 생성 |
| **조인트 플롯 (Joint)** | `sns.jointplot(data=df, x='x', y='y', kind='reg')` | 두 변수의 2차원 산점도와 각 축의 1차원 한계 분포(Marginal) 결합 |
| **회귀선 (Regression)**| `sns.regplot(data=df, x='x', y='y', order=1)` | 산점도 위에 1차/다항식 회귀선 및 95% 신뢰구간 밴드 자동 피팅 |
| **클러스터맵** | `sns.clustermap(df, cmap='vlag', standard_scale=1)` | 계층적 군집화(Hierarchical Clustering) 덴드로그램과 히트맵 결합 |
| **색상 팔레트** | `sns.color_palette("mako", as_cmap=True)` | `mako`, `rocket`, `crest`, `viridis`, `Set2` 등 감각적인 컬러 매핑 |
| **패싯 그리드** | `g = sns.FacetGrid(df, col='col'); g.map(...)` | 다차원 범주형 변수를 다중 서브플롯 그리드로 매핑하는 커스텀 빌더 |
| **저장 & 연동** | `plt.savefig('sns.png', dpi=300, bbox_inches='tight')` | Matplotlib 기반이므로 `plt.title()`, `plt.savefig()`와 100% 호환 |

### Seaborn 실전 예제 코드
```python
import seaborn as sns
import matplotlib.pyplot as plt

# 1. 전역 테마 및 스타일 설정
sns.set_theme(style="whitegrid", font_scale=1.1)

# 2. 범주형 분포 및 통계 비교 (Box & Violin)
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
sns.boxplot(data=df, x='day', y='total_bill', hue='sex', palette='pastel', ax=axes[0])
axes[0].set_title("Box Plot with Quartiles")

sns.violinplot(data=df, x='day', y='total_bill', hue='sex', split=True, palette='muted', ax=axes[1])
axes[1].set_title("Violin Plot with Split KDE")
plt.tight_layout()

# 3. 상관관계 분석 히트맵 (Heatmap)
plt.figure(figsize=(8, 6))
correlation_matrix = df.corr(numeric_only=True)
sns.heatmap(
    correlation_matrix,
    annot=True,          # 상관계수 숫자 표시
    cmap='coolwarm',     # 블루-화이트-레드 발산 컬러맵
    fmt=".2f",          # 소수점 둘째 자리
    vmin=-1, vmax=1,     # 컬러바 범위 고정
    linewidths=0.5
)
plt.title("Correlation Matrix Heatmap")

# 4. 다변량 쌍대 관계 분석 (Pair Plot)
pair_fig = sns.pairplot(df, hue='species', corner=True, palette='Set2')

# 5. 고해상도 이미지 저장
plt.savefig('seaborn_complete_analysis.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## 💡 Matplotlib vs Seaborn 완벽 비교 및 활용 가이드

| 비교 항목 | Matplotlib 📊 | Seaborn 🌊 |
| :--- | :--- | :--- |
| **추상화 수준** | 저수준 (Low-level): 모든 선·축·여백을 세밀하게 직접 제어 | 고수준 (High-level): 한 줄 코드로 정교한 통계 차트 완성 |
| **Pandas 데이터프레임 연동**| `x=df['col1'], y=df['col2']` 컬럼을 수동 전달 | `data=df, x='col1', y='col2', hue='category'` 컬럼명 직접 지정 |
| **통계 연산 기능** | 통계값(평균, 신뢰구간 등)을 사전에 직접 계산 필요 | 평균, 신뢰구간(CI), 커널 밀도(KDE), 회귀선 자동 계산 |
| **디자인 & 컬러 팔레트** | 기본 스타일이 다소 투박하여 세밀한 스타일링 필요 | 모던한 기본 테마(`whitegrid`) 및 데이터 과학 특화 컬러 팔레트 |
| **추천 활용 시점** | 커스텀 인포그래픽, 복합 레이아웃, 독창적 대시보드 | **탐색적 데이터 분석 (EDA)**, 통계 보고서, 상관관계 및 다변량 분석 |

> [!TIP]
> **실무 권장 시너지 전략**:  
> Seaborn으로 아름다운 통계 그래프를 빠르게 그린 후, Matplotlib의 `plt.title()`, `ax.set_ylim()`, `plt.savefig()`를 결합하여 제목, 축 범위, 주석(Annotation)을 세밀하게 조정하는 혼합 방식이 현업 데이터 과학의 표준입니다.
