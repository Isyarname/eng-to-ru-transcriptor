# English-to-Russian Phonetic Transcriber 🔤

[Читать на русском языке](README.ru.md)

A Python library for automatic English-to-Cyrillic text transcription using a hybrid engine: dictionary lookup and neural G2P (`gruut`) for unknown words.

## 💡 Features

- **Full text transcription** — handles any English text.
- **Custom vocabulary** — augment the built-in dictionary with your own overrides.
- **Dynamic vocabulary management** — add/remove custom words at runtime.

## ⚡ Key Highlights

- **Two-tier lookup** — IPA via local 120k+ dict + neural G2P backup.
- **Graphemic adaptation** — Cyrillic matches Russian orthography.
- **Declarative rules** — update transliteration logic on the fly.

## 🚀 Installation

```bash
pip install eng-to-ru-transcriber
```

## 💻 Usage

### Basic Example
```python
from eng_to_ru_transcriber import Transcriber
t = Transcriber()
print(t.transcribe("Hello world")) # → Хэлоу уорлд
```

### Custom Vocabulary
```python
from eng_to_ru_transcriber import Transcriber
custom_vocabulary = {"python": "ˈpaɪθɑn"}
t = Transcriber(custom_vocabulary=custom_vocabulary)
```

### Dynamic/Temporary Vocabulary
```python
t.add_custom_word("word", "phonetic")
# Or temporarily:
t.transcribe("Text", custom_vocabulary={"Text": "..."})
```

## 🧪 Testing
```bash
pip install pytest
pytest
```

## 📊 Data Sources
Based on curated IPA data from OpenWiktionary.

## 📜 License
MIT
