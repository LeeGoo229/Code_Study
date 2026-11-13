"""
diff_viewer.py
사용자 작성 코드와 모범 답안 코드를 비교하여
추가/삭제/수정된 라인을 시각적으로 표시하는 모듈
"""

import difflib

def generate_diff_html(user_code: str, answer_code: str) -> str:
    """
    사용자 코드와 모범 답안의 라인별 차이점을 HTML로 서식화하여 반환합니다.
    """
    user_lines = [l for l in user_code.strip().splitlines()]
    answer_lines = [l for l in answer_code.strip().splitlines()]
    
    matcher = difflib.SequenceMatcher(None, user_lines, answer_lines)
    
    html_lines = []
    html_lines.append("<div style='font-family: monospace; font-size: 13px; line-height: 1.6; background: #0f172a; color: #f8fafc; padding: 12px; border-radius: 8px;'>")
    html_lines.append("<div style='margin-bottom: 8px; font-weight: bold; color: #94a3b8;'>코드 비교 (내 코드 vs 모범 답안)</div>")
    
    diff = list(difflib.unified_diff(user_lines, answer_lines, fromfile="내 작성 코드", tofile="모범 답안", lineterm=""))
    
    if not diff:
        html_lines.append("<div style='color: #4ade80;'>🎉 작성한 코드가 모범 답안과 완전히 일치합니다!</div>")
    else:
        for line in diff:
            if line.startswith("---") or line.startswith("+++") or line.startswith("@@"):
                html_lines.append(f"<div style='color: #64748b;'>{escape_html(line)}</div>")
            elif line.startswith("-"):
                html_lines.append(f"<div style='background: rgba(239, 68, 68, 0.2); color: #f87171;'>{escape_html(line)}</div>")
            elif line.startswith("+"):
                html_lines.append(f"<div style='background: rgba(34, 197, 94, 0.2); color: #4ade80;'>{escape_html(line)}</div>")
            else:
                html_lines.append(f"<div style='color: #cbd5e1;'>{escape_html(line)}</div>")
                
    html_lines.append("</div>")
    return "\n".join(html_lines)

def escape_html(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace(" ", "&nbsp;")
    )
