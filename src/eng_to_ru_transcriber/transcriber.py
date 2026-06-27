"""Класс-оркестратор транслитерации."""
from __future__ import annotations
import json
from importlib import resources
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path
import pickle
from platformdirs import user_cache_dir
from . import dsl_translator, ipa_to_ru, eng_to_ipa_hybrid

_PACKAGE_DATA = resources.files("eng_to_ru_transcriber.data")

def _default_cache_dir() -> Path:
    return Path(user_cache_dir("eng_to_ru_transcriber", appauthor=False))

def _default_rules_path() -> Path:
    return Path(str(_PACKAGE_DATA.joinpath("transliteration_rules.py")))

def _default_eng_rules_path() -> Path:
    return Path(str(_PACKAGE_DATA.joinpath("eng_to_ipa_rules.py")))

def _default_dict_path() -> Path:
    return Path(str(_PACKAGE_DATA.joinpath("en_dict.pkl")))

class Transcriber:
    """
    Оркестратор транслитерации английского текста в кириллицу.
    Лениво загружает ресурсы при первом вызове и кэширует их в памяти.
    Пользовательский словарь дополняет встроенный, а не заменяет его.
    """

    def __init__(
        self,
        rules_path: Path | None = None,
        eng_rules_path: Path | None = None,
        dict_path: Path | None = None,
        cache_dir: Path | None = None,
        custom_vocabulary: dict[str, str] | None = None,
    ) -> None:
        """
        Args:
            rules_path: Путь к правилам транслитерации (IPA -> RU).
            eng_rules_path: Путь к правилам транскрипции (EN -> IPA).
            dict_path: Путь к словарю исключений.
            cache_dir: Папка для кэша JSON.
            custom_vocabulary: Пользовательский словарь (дополняет встроенный).
        """
        self._rules_path = rules_path or _default_rules_path()
        self._eng_rules_path = eng_rules_path or _default_eng_rules_path()
        self._dict_path = dict_path or _default_dict_path()
        self._cache_dir = cache_dir or _default_cache_dir()
        self._cache_dir.mkdir(parents=True, exist_ok=True)

        # Лениво загружаемые ресурсы
        self._transliteration_rules: list[tuple[str, str]] | None = None
        self._eng_to_ipa_rules: list[tuple[str, str]] | None = None
        self._dict_cache: dict[str, str] | None = None

        # Пользовательский словарь
        self._custom_vocabulary: dict[str, str] = dict(custom_vocabulary) if custom_vocabulary else {}

    # ─────────────────────────── Публичный API ───────────────────────────

    def transcribe(self, text: str) -> str:
        """Транслитерирует английский текст в кириллицу."""
        transliteration_rules = self.get_transliteration_rules()
        eng_to_ipa_rules = self.get_eng_to_ipa_rules()
        vocabulary = self.get_vocabulary()

        # 1. Английский текст -> IPA (с использованием правил и словаря)
        ipa_text = eng_to_ipa_hybrid.transcribe(text, vocabulary, eng_to_ipa_rules)
        #print(ipa_text)
        # 2. IPA -> Кириллица
        return ipa_to_ru.convert(ipa_text, transliteration_rules)

    # ─────────────────────────── Доступ к ресурсам ───────────────────────

    def get_transliteration_rules(self) -> list[tuple[str, str]]:
        """Возвращает скомпилированные правила IPA → кириллица."""
        if self._transliteration_rules is None:
            self._transliteration_rules = self._compile_dsl(self._rules_path, "transliteration_rules.json")
        return self._transliteration_rules

    def get_eng_to_ipa_rules(self) -> list[tuple[str, str]]:
        """Возвращает скомпилированные правила English → IPA."""
        if self._eng_to_ipa_rules is None:
            self._eng_to_ipa_rules = self._compile_dsl(self._eng_rules_path, "eng_to_ipa_rules.json")
        return self._eng_to_ipa_rules

    def get_vocabulary(self) -> dict[str, str]:
        """Возвращает объединённый словарь: встроенный + пользовательский."""
        if self._dict_cache is None:
            self._dict_cache = self._load_ipa_dictionary(self._dict_path)
        return {**self._dict_cache, **self._custom_vocabulary}

    # ─────────────────────────── Управление состоянием ───────────────────

    def reload_rules(self) -> None:
        """Перекомпилирует правила """
        self._transliteration_rules = self._compile_dsl(self._rules_path, "transliteration_rules.json", force=True)
        self._eng_to_ipa_rules = self._compile_dsl(self._eng_rules_path, "eng_to_ipa_rules.json", force=True)

    def reload_dictionary(self) -> None:
        """Перечитывает встроенный словарь с диска."""
        self._dict_cache = self._load_ipa_dictionary(self._dict_path)

    def reload_all(self) -> None:
        """Перезагружает всё: и словарь, и все правила транслитерации."""
        self.reload_dictionary()
        self.reload_rules()

    def clear_cache(self) -> None:
        """Удаляет JSON-кэши с диска."""
        for filename in ("transliteration_rules.json", "eng_to_ipa_rules.json"):
            cache_file = self._cache_dir / filename
            if cache_file.exists():
                cache_file.unlink()
        self._transliteration_rules = None
        self._eng_to_ipa_rules = None

    # ─────────────────────────── Внутренние методы ───────────────────────

    def _compile_dsl(self, rules_path: Path, cache_filename: str, force: bool = False) -> list[tuple[str, str]]:
        """
        Универсальный метод: загружает правила из JSON-кэша или компилирует из DSL.
        """
        cache_file = self._cache_dir / cache_filename

        if cache_file.exists() and not force:
            with open(cache_file, "r", encoding="utf-8") as f:
                return [tuple(pair) for pair in json.load(f)]

        if not rules_path.exists():
            raise FileNotFoundError(f"Файл правил не найден: {rules_path}")

        spec = spec_from_file_location("rules_module", str(rules_path))
        if spec is None or spec.loader is None:
            raise ImportError(f"Не удалось загрузить модуль: {rules_path}")

        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        raw_macros = getattr(module, "macros", {})
        raw_rules = getattr(module, "rules", "")

        rules = dsl_translator.build_rules(raw_rules, raw_macros)

        with open(cache_file, "w", encoding="utf-8") as f:
            json.dump(rules, f, ensure_ascii=False, indent=4)

        return rules

    @staticmethod
    def _load_ipa_dictionary(dict_path: Path) -> dict[str, str]:
        """Загружает словарь IPA-исключений из pickle."""
        if not dict_path.exists():
            raise FileNotFoundError(f"Словарь не найден: {dict_path}")

        with open(dict_path, "rb") as f:
            return pickle.load(f)

    # ─────────────────────────── Магические методы ────────────────────────

    def __repr__(self) -> str:
        return (
            f"Transcriber("
            f"ipa_rules={'загружены' if self._transliteration_rules else 'нет'}, "
            f"eng_rules={'загружены' if self._eng_to_ipa_rules else 'нет'}, "
            f"dict={'загружен' if self._dict_cache else 'нет'}"
            f")"
        )