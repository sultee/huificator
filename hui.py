# -*- coding: utf-8 -*-
"""
Ху-трансформер для русских слов.
Если ввод содержит несколько слов — каждое преобразуется отдельно.
"""

from typing import List

VOWELS = set("аеёиоуэюыя")

V_MAP = {
    "а": "я",
    "я": "я",
    "е": "е",
    "о": "е",
    "и": "и",
    "ё": "ё",
    "ы": "и",
    "ю": "ю",
    "у": "ю",
    # "э" не задана → дефолт "е"
}


def split_syllables(word: str) -> List[str]:
    """Разделяем слово на слоги по гласным (гласная включается в слог)."""
    chunks: List[str] = []
    start = 0
    for i, ch in enumerate(word):
        if ch.lower() in VOWELS:
            chunks.append(word[start : i + 1])
            start = i + 1
    chunks.append(word[start:])
    return [c for c in chunks if c]


def choose_button(syllable: str) -> str:
    """Выбираем подходящую гласную для 'ху' по таблице соответствий."""
    btn = "е"
    for ch in syllable:
        m = V_MAP.get(ch.lower())
        if m:
            btn = m
    return btn


def hu_transform(word: str) -> str:
    """Основное преобразование одного слова."""
    slogs = split_syllables(word)
    endword = "ху"

    if not slogs:
        return endword

    if len(slogs) < 4:
        endword += choose_button(slogs[0])
        endword += "".join(slogs[1:])
    elif len(slogs) > 3:
        endword += choose_button(slogs[1])
        endword += "".join(slogs[2:])
    return endword


if __name__ == "__main__":
    try:
        user_input = input("Enter word(s): ").strip()
    except EOFError:
        user_input = ""

    # Разделяем строку на слова по пробелам и обрабатываем каждое
    words = user_input.split()
    result = [hu_transform(w) for w in words]
    print(" ".join(result))
