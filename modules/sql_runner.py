"""
sql_runner.py
추후 SQL 학습 확장을 위한 인메모리 SQL 엔진 (DuckDB / SQLite 지원)
기본 분석용 테이블(고객, 주문, 상품)을 자동 탑재하여
웹에서 실시간 쿼리 실행 및 결과 표(DataFrame)를 반환합니다.
"""

import traceback
from typing import Dict, Any, List, Optional
import pandas as pd

try:
    import duckdb
    HAS_DUCKDB = True
except ImportError:
    HAS_DUCKDB = False
    import sqlite3

class SQLEngine:
    def __init__(self):
        self.conn = None
        self._init_database()
        
    def _init_database(self):
        """인메모리 DB 연결 및 분석용 예제 테이블 생성"""
        if HAS_DUCKDB:
            self.conn = duckdb.connect(database=":memory:")
            self._seed_sample_data_duckdb()
        else:
            self.conn = sqlite3.connect(":memory:")
            self._seed_sample_data_sqlite()
            
    def _seed_sample_data_duckdb(self):
        # 1. 고객 테이블 (customers)
        self.conn.execute("""
            CREATE TABLE customers (
                customer_id INT PRIMARY KEY,
                name VARCHAR,
                gender VARCHAR,
                age INT,
                city VARCHAR,
                grade VARCHAR,
                join_date DATE
            );
            INSERT INTO customers VALUES
            (1, '김철수', 'M', 28, 'Seoul', 'Gold', '2023-01-15'),
            (2, '이영희', 'F', 34, 'Busan', 'Platinum', '2022-11-20'),
            (3, '박민수', 'M', 45, 'Seoul', 'Silver', '2023-03-01'),
            (4, '최지은', 'F', 23, 'Incheon', 'Bronze', '2023-05-12'),
            (5, '정현우', 'M', 31, 'Daegu', 'Gold', '2022-08-30'),
            (6, '강서연', 'F', 29, 'Seoul', 'Silver', '2023-02-14'),
            (7, '조상원', 'M', 52, 'Busan', 'Platinum', '2021-09-05'),
            (8, '윤하은', 'F', 38, 'Seoul', 'Gold', '2022-12-01');
        """)
        
        # 2. 상품 테이블 (products)
        self.conn.execute("""
            CREATE TABLE products (
                product_id INT PRIMARY KEY,
                product_name VARCHAR,
                category VARCHAR,
                price INT,
                stock INT
            );
            INSERT INTO products VALUES
            (101, '무선 마우스', 'Electronics', 25000, 150),
            (102, '기계식 키보드', 'Electronics', 89000, 80),
            (103, '커피 원두 1kg', 'Food', 22000, 300),
            (104, '텀블러', 'Living', 18000, 200),
            (105, '게이밍 모니터 27인치', 'Electronics', 350000, 45),
            (106, '유기농 녹차', 'Food', 15000, 120),
            (107, '노트북 거치대', 'Living', 32000, 90);
        """)
        
        # 3. 주문 테이블 (orders)
        self.conn.execute("""
            CREATE TABLE orders (
                order_id INT PRIMARY KEY,
                customer_id INT,
                product_id INT,
                quantity INT,
                order_date DATE,
                status VARCHAR
            );
            INSERT INTO orders VALUES
            (1001, 1, 101, 2, '2023-06-01', 'COMPLETED'),
            (1002, 2, 105, 1, '2023-06-02', 'COMPLETED'),
            (1003, 1, 103, 3, '2023-06-05', 'COMPLETED'),
            (1004, 3, 102, 1, '2023-06-08', 'CANCELLED'),
            (1005, 4, 104, 2, '2023-06-10', 'COMPLETED'),
            (1006, 5, 101, 1, '2023-06-12', 'COMPLETED'),
            (1007, 2, 102, 1, '2023-06-15', 'COMPLETED'),
            (1008, 6, 106, 4, '2023-06-18', 'COMPLETED'),
            (1009, 7, 105, 2, '2023-06-20', 'COMPLETED'),
            (1010, 8, 107, 1, '2023-06-22', 'COMPLETED'),
            (1011, 1, 104, 1, '2023-06-25', 'COMPLETED'),
            (1012, 5, 103, 2, '2023-06-28', 'COMPLETED');
        """)

    def _seed_sample_data_sqlite(self):
        cur = self.conn.cursor()
        cur.executescript("""
            CREATE TABLE customers (
                customer_id INTEGER PRIMARY KEY,
                name TEXT, gender TEXT, age INTEGER, city TEXT, grade TEXT, join_date TEXT
            );
            INSERT INTO customers VALUES
            (1, '김철수', 'M', 28, 'Seoul', 'Gold', '2023-01-15'),
            (2, '이영희', 'F', 34, 'Busan', 'Platinum', '2022-11-20'),
            (3, '박민수', 'M', 45, 'Seoul', 'Silver', '2023-03-01'),
            (4, '최지은', 'F', 23, 'Incheon', 'Bronze', '2023-05-12');
            
            CREATE TABLE products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT, category TEXT, price INTEGER, stock INTEGER
            );
            INSERT INTO products VALUES
            (101, '무선 마우스', 'Electronics', 25000, 150),
            (102, '기계식 키보드', 'Electronics', 89000, 80);
            
            CREATE TABLE orders (
                order_id INTEGER PRIMARY KEY,
                customer_id INTEGER, product_id INTEGER, quantity INTEGER, order_date TEXT, status TEXT
            );
            INSERT INTO orders VALUES
            (1001, 1, 101, 2, '2023-06-01', 'COMPLETED');
        """)
        self.conn.commit()

    def run_query(self, query: str) -> Dict[str, Any]:
        """SQL 쿼리를 실행하고 pandas DataFrame 및 통계를 반환"""
        clean_query = query.strip()
        if not clean_query:
            return {"success": False, "df": None, "error": "쿼리가 비어 있습니다.", "row_count": 0}
            
        try:
            if HAS_DUCKDB:
                df = self.conn.execute(clean_query).fetchdf()
            else:
                df = pd.read_sql_query(clean_query, self.conn)
                
            return {
                "success": True,
                "df": df,
                "error": None,
                "row_count": len(df)
            }
        except Exception as e:
            return {
                "success": False,
                "df": None,
                "error": str(e),
                "row_count": 0
            }

# SQL 실습용 샘플 커리큘럼 프리셋
SQL_CURRICULUM = [
    {
        "id": "sql_1",
        "title": "SQL 1. 기초 데이터 조회 (SELECT & WHERE)",
        "desc": """
### [문제 1] 서울에 거주하는 Gold 등급 이상의 고객 조회
고객(`customers`) 테이블에서 서울(`city = 'Seoul'`)에 거주하며 등급이 `'Gold'` 또는 `'Platinum'`인 고객의 `customer_id`, `name`, `grade`, `age`를 조회하세요.
""",
        "starter": "-- 여기에 SQL 쿼리를 작성하세요\nSELECT customer_id, name, grade, age\nFROM customers\nWHERE ",
        "solution": "SELECT customer_id, name, grade, age\nFROM customers\nWHERE city = 'Seoul' AND grade IN ('Gold', 'Platinum');",
        "explanation": "WHERE 절의 AND 연산자와 IN ('Gold', 'Platinum')을 사용하여 다중 조건을 필터링합니다."
    },
    {
        "id": "sql_2",
        "title": "SQL 2. 데이터 결합 (INNER JOIN)",
        "desc": """
### [문제 2] 주문별 고객명과 상품명, 결제금액 계산
주문(`orders`), 고객(`customers`), 상품(`products`) 테이블을 JOIN하여,
완료된 주문(`status = 'COMPLETED'`)에 대해 `order_id`, 고객명(`name`), 상품명(`product_name`), 수량(`quantity`), 총금액(`quantity * price AS total_price`)을 조회하세요.
""",
        "starter": "SELECT o.order_id, c.name, p.product_name, o.quantity, (o.quantity * p.price) AS total_price\nFROM orders o\nJOIN customers c ON o.customer_id = c.customer_id\nJOIN products p ON o.product_id = p.product_id\nWHERE ",
        "solution": "SELECT o.order_id, c.name, p.product_name, o.quantity, (o.quantity * p.price) AS total_price\nFROM orders o\nJOIN customers c ON o.customer_id = c.customer_id\nJOIN products p ON o.product_id = p.product_id\nWHERE o.status = 'COMPLETED'\nORDER BY o.order_id;",
        "explanation": "주문-고객, 주문-상품 간의 다대일(N:1) 관계를 INNER JOIN으로 결합하고 계산 열을 생성합니다."
    },
    {
        "id": "sql_3",
        "title": "SQL 3. 그룹별 집계 (GROUP BY & HAVING)",
        "desc": """
### [문제 3] 카테고리별 총 판매 수량 및 매출 합계
주문과 상품을 조인하여, 완료된 주문을 기준으로 카테고리(`category`)별 주문 건수(`order_count`), 총 판매수량(`total_qty`), 총 매출액(`total_revenue`)을 계산하고 총 매출액 내림차순으로 정렬하세요.
""",
        "starter": "SELECT p.category,\n       COUNT(o.order_id) AS order_count,\n       SUM(o.quantity) AS total_qty,\n       SUM(o.quantity * p.price) AS total_revenue\nFROM orders o\nJOIN products p ON o.product_id = p.product_id\nWHERE o.status = 'COMPLETED'\nGROUP BY ",
        "solution": "SELECT p.category,\n       COUNT(o.order_id) AS order_count,\n       SUM(o.quantity) AS total_qty,\n       SUM(o.quantity * p.price) AS total_revenue\nFROM orders o\nJOIN products p ON o.product_id = p.product_id\nWHERE o.status = 'COMPLETED'\nGROUP BY p.category\nORDER BY total_revenue DESC;",
        "explanation": "GROUP BY p.category로 묶고 집계 함수(COUNT, SUM)를 적용한 뒤 ORDER BY DESC로 정렬합니다."
    }
]
