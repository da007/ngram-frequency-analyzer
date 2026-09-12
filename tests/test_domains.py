import pytest
from app.domains import WordItem, OptimizerConfig, NGramVocab
from dataclasses import FrozenInstanceError


# --- WordItem ---

@pytest.mark.parametrize("word, weight", [
    ("hello", 0),
    ("Def", 1.2),
])
def test_word_item_valid(word, weight):
    item = WordItem(word, weight)
    assert item.text == word
    assert item.weight == weight
    assert item.length == len(word)


@pytest.mark.parametrize("word, weight", [
    ("", 0),
    ("   ", 1.2),
])
def test_word_item_empty(word, weight):
    with pytest.raises(ValueError, match="empty"):
        WordItem(word, weight)


@pytest.mark.parametrize("word, weight", [
    ("hello", -2),
    ("22", -1),
])
def test_word_item_negative_weight(word, weight):
    with pytest.raises(ValueError, match=">= 0"):
        WordItem(word, weight)


# --- OptimizerConfig ---

@pytest.mark.parametrize("max_vocab_size, min_word_length", [
    (3, 5),
    (1_000_000, 10),
])
def test_optimizer_config_valid(max_vocab_size, min_word_length):
    config = OptimizerConfig(max_vocab_size, min_word_length)
    assert config.max_vocab_size == max_vocab_size
    assert config.min_word_length == min_word_length


@pytest.mark.parametrize("max_vocab_size, min_word_length", [
    (0, 0),
    (100, -1),
    (-1, 232),
])
def test_optimizer_config_invalid(max_vocab_size, min_word_length):
    with pytest.raises(ValueError, match="must be"):
        OptimizerConfig(max_vocab_size, min_word_length)


# ---Immutebilitty---

def test_word_item():
    item = WordItem("_", 1)
    with pytest.raises(FrozenInstanceError):
        item.text = "232"    
    with pytest.raises(FrozenInstanceError):
        item.weight = 23


def test_optimizer_config():
    config = OptimizerConfig(1, 1)
    with pytest.raises(FrozenInstanceError):
        config.max_vocab_size = 2   
    with pytest.raises(FrozenInstanceError):
        config.min_word_length = 2


# ---NGramVocab---

def test_ngram_vocab_success():
    vocab = NGramVocab(
        max_size=5,
        grams={"ab", "bc", "cd"}
    )
    assert vocab.max_size == 5
    assert vocab.grams == {"ab", "bc", "cd"}


def test_ngram_vocab_size_exceeds_max():
    with pytest.raises(ValueError, match="exceeds max_size"):
        NGramVocab(
            max_size=2,
            grams={"ab", "bc", "cd"}
        )


def test_ngram_vocab_empty_string():
    with pytest.raises(ValueError, match="empty strings"):
        NGramVocab(
            max_size=5,
            grams={"ab", "", "cd"}
        )