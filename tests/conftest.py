"""Общие fixtures для всех тестов."""
import pytest


@pytest.fixture
def sample_rules():
    """Простой набор правил для тестов."""
    return [
        ("a", "x"),
        ("b", "y"),
        ("c", "z"),
    ]


@pytest.fixture
def sample_ipa_text():
    """Пример IPA-текста."""
    return "hɛˈloʊ wɝːld"