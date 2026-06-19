# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-06-20

### Removed
- Dynamic vocabulary API: `add_exception()` and `remove_exception()` methods
- `custom_exceptions` parameter from `Transcriber.transcribe()` method

### Changed
- **Breaking:** `custom_exceptions` parameter renamed to `custom_vocabulary` in `Transcriber.__init__`
- Custom vocabulary is now **static** — set once at object creation, cannot be modified at runtime
- For different vocabulary overrides, create separate `Transcriber` instances

### Documentation
- Added `docs/` folder with `ARCHITECTURE.md`, `CONTRIBUTING.md`, and `DSL.md`
- Added Russian translation of README (`README.ru.md`)
- Added DSL reference guide for transliteration rules

### Migration Guide

**Before (0.1.1):**
```python
t = Transcriber()
t.transcribe("text", custom_exceptions={"kubernetes": "ˈkuːbərˌnɛtɪs"})
```

**After (0.2.0):**
```python
t = Transcriber(custom_vocabulary={"kubernetes": "ˈkuːbərˌnɛtɪs"})
t.transcribe("text")
```

## [0.1.1] - 2025-XX-XX

> **Note:** Details for this release were not preserved.
> Run `git log v0.1.0..v0.1.1 --oneline` to see the commits.

## [0.1.0] - 2025-XX-XX

### Added
- Initial release
- Hybrid transcription engine (built-in dictionary + `gruut` fallback)
- IPA-to-Cyrillic transliteration via compiled rules
- Built-in dictionary with 120k+ English words
- Custom vocabulary support via `custom_exceptions` parameter
- Lazy loading of `gruut` for faster startup
- Rule caching in `user_cache_dir`

[Unreleased]: https://github.com/Isyarname/eng-to-ru-transcriber/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/Isyarname/eng-to-ru-transcriber/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/Isyarname/eng-to-ru-transcriber/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/Isyarname/eng-to-ru-transcriber/releases/tag/v0.1.0