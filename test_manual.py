"""Ручной тест без установки пакета."""
import sys
from pathlib import Path

# Добавляем src/ в пути поиска
sys.path.insert(0, str(Path(__file__).parent / "src"))

from eng_to_ru_transcriptor import transcribe, __version__

print(f"Версия: {__version__}")
print(f"Результат: {transcribe('hello world')}")