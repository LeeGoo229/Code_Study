"""
python_runner.py
사용자가 입력한 파이썬 코드를 안전하게 실행하고
표준 출력, 에러, Matplotlib/Seaborn 차트, DataFrame을 캡처하여 반환하는 모듈
"""

import sys
import io
import os
import traceback
from pathlib import Path
from typing import Dict, Any, List, Optional
import matplotlib
matplotlib.use("Agg")  # GUI 없는 환경(웹 서버)용 백엔드
import matplotlib.pyplot as plt

def run_python_code(code: str, setup_code: str = "", data_dir: str = "") -> Dict[str, Any]:
    """
    제공된 파이썬 코드를 실행하고 결과를 캡처하여 반환합니다.
    """
    stdout_capture = io.StringIO()
    stderr_capture = io.StringIO()
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    
    # Matplotlib 이전 플롯 초기화
    plt.close("all")
    
    # 글로벌 실행 컨텍스트 생성
    exec_globals: Dict[str, Any] = {
        "__name__": "__main__",
        "Path": Path
    }
    
    # 데이터 경로가 있으면 DATA_DIR 환경 설정
    if data_dir and os.path.exists(data_dir):
        exec_globals["DATA_DIR"] = Path(data_dir)
        exec_globals["colab_data"] = Path(data_dir)
        
    figures = []
    dataframe_result = None
    success = False
    error_msg = None
    
    try:
        sys.stdout = stdout_capture
        sys.stderr = stderr_capture
        
        # 1. Setup 코드 사전 실행 (임포트, 데이터 로드, 사전 변수)
        if setup_code and setup_code.strip():
            # openpyxl 무조건 설치 등 %pip 매직 커맨드 제거
            clean_setup = "\n".join(
                line for line in setup_code.split("\n") 
                if not line.strip().startswith("%") and not line.strip().startswith("!")
            )
            exec(clean_setup, exec_globals)
            
        # 2. 사용자 작성 코드 실행
        # 주피터 매직 커맨드 필터링
        clean_user_code = "\n".join(
            line for line in code.split("\n")
            if not line.strip().startswith("%") and not line.strip().startswith("!")
        )
        
        # 코드가 표현식인 경우(예: df.head() 마지막 줄) 값 캡처 시도
        lines = [l for l in clean_user_code.strip().split("\n") if l.strip()]
        if lines:
            last_line = lines[-1]
            # 할당문, 제어문이 아니면 eval 시도
            if not any(last_line.strip().startswith(kw) for kw in ["import ", "from ", "def ", "class ", "for ", "if ", "while ", "return ", "assert "]) and "=" not in last_line:
                body = "\n".join(lines[:-1])
                if body.strip():
                    exec(body, exec_globals)
                eval_res = eval(last_line, exec_globals)
                if eval_res is not None:
                    # pandas DataFrame / Series 인지 확인
                    type_str = str(type(eval_res))
                    if "DataFrame" in type_str or "Series" in type_str:
                        dataframe_result = eval_res
                    else:
                        print(eval_res)
            else:
                exec(clean_user_code, exec_globals)
        else:
            exec(clean_user_code, exec_globals)
            
        success = True
        
        # 3. 생성된 Matplotlib Figure 캡처
        fig_nums = plt.get_fignums()
        for num in fig_nums:
            fig = plt.figure(num)
            if fig.axes:  # 축이 그려진 유효한 그래프만
                figures.append(fig)
                
    except Exception as e:
        success = False
        error_msg = traceback.format_exc()
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        
    return {
        "success": success,
        "stdout": stdout_capture.getvalue(),
        "stderr": stderr_capture.getvalue(),
        "figures": figures,
        "dataframe": dataframe_result,
        "error": error_msg
    }
