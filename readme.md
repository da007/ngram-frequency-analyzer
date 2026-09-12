# N-gram Frequency Analyzer

Программа для статического анализа частотности n-грамм в тексте. Позволяет эффективно подбирать наборы n-грамм для дальнейшей обработки (составления кодов, токенизации и т.д.).

## Основные возможности
- Анализ уникальности слов (на основе лемм).
- Поддержка алгоритмов выбора n-грамм:
  - **GSC** (Greedy Search Algorithm)
  - **BPE** (Byte Pair Encoding)
- Чистая архитектура с использованием DataClasses.

## Установка
```bash
# Клонирование
git clone https://github.com/da007/ngram-frequency-analyzer.git
cd ngram-frequency-analyzer

# Установка зависимостей (для тестов)
pip install -r dev-requirements.txt
```

## Тестирование
Для запуска тестов используй:
```bash
pytest
```

## Лицензия
MIT