"""Модуль транскрипции английского текста в IPA с помощью rule_engine."""
from __future__ import annotations
import re
from . import rule_engine

# Предкомпилированные regex
_ABBR_SPLIT = re.compile(r'(?<=[a-zа-яё])(?=[A-ZА-ЯЁ]{2,})')
_CAMEL_CASE = re.compile(r'([A-Z])(?=[a-z])')


def smart_lower(text: str) -> str:
    """Умная обработка регистра с учётом аббревиатур и CamelCase."""
    text = _ABBR_SPLIT.sub('-', text)
    text = _CAMEL_CASE.sub(lambda m: m.group(1).lower(), text)
    return text


def transcribe(text: str, transcription_rules: list[tuple[str, str]]) -> str:
    #print(text)
    text = smart_lower(text)
    #print(text)
    return rule_engine.process_text(text, transcription_rules)