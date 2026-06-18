# Руководство контрибьютора

## Установка для разработки

```bash
git clone https://github.com/Isyarname/eng-to-ru-transcriptor
cd eng-to-ru-transcriptor
pip install -e .
```

## Запуск тестов

```bash
pip install pytest
pytest
```

## Как добавить новое правило транслитерации

1. Откройте `src/eng_to_ru_transcriptor/data/transliteration_rules.py`
2. Добавьте правило в формате `исходная -> результат`
3. Удалите `~/.cache/eng_to_ru_transcriptor/compiled_rules.json`
4. Запустите тесты: `pytest`
5. Создайте PR

## Как добавить слово в словарь исключений

1. Откройте `src/eng_to_ru_transcriptor/data/en_dict.txt`
2. Добавьте строку: `слово\tтранскрипция`
3. Создайте PR