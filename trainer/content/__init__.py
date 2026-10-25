"""Question content registry. Importing the chapter modules registers their templates."""
from . import calc_ch1, calc_ch1b, explain_ch1, written_ch1b, calc_ch2b, explain_ch2, written_ch2b, calc_ch3x, explain_ch3, written_ch3x, calc_ch4x, explain_ch4, written_ch4x, calc_ch5x, explain_ch5, written_ch5x, calc_ch6x, explain_ch6, written_ch6x, calc_ch7x, explain_ch7, written_ch7x, calc_ch8x, explain_ch8, written_ch8x, calc_ch9x, explain_ch9, written_ch9x, calc_ch10x, explain_ch10, written_ch10x, calc_ch11x, explain_ch11, written_ch11x, calc_ch12x, explain_ch12, written_ch12x, calc_ch13x, explain_ch13, written_ch13x, calc_ch14x, explain_ch14, written_ch14x, calc_ch15x, explain_ch15, written_ch15x, calc_ch10, calc_ch11, calc_ch11b, calc_ch12, calc_ch13, calc_ch14, calc_ch15, calc_ch16, calc_ch17, calc_ch18, calc_ch19, calc_ch2, calc_ch20, calc_ch3, calc_ch3b, calc_ch4, calc_ch5, calc_ch6, calc_ch6b, calc_ch7, calc_ch8, calc_ch9, recall, recall2, recall3, recall4, written_ch1, written_ch12, written_ch13, written_ch14, written_ch15, written_ch16, written_ch17, written_ch18, written_ch19, written_ch20, written_ch10, written_ch11, written_ch2, written_ch3, written_ch3b, written_ch4, written_ch6, written_ch7, written_ch8  # noqa: F401
from .base import TEMPLATES, Question, Template


def chapters_with_content(category: str):
    return sorted({t.chapter for t in TEMPLATES if t.category == category})


def inventory():
    """{(category, chapter): {level: count}}"""
    out = {}
    for t in TEMPLATES:
        out.setdefault((t.category, t.chapter), {}).setdefault(t.level, 0)
        out[(t.category, t.chapter)][t.level] += 1
    return out


__all__ = ["TEMPLATES", "Question", "Template", "chapters_with_content", "inventory"]
