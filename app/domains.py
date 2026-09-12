from dataclasses import dataclass, field

@dataclass(frozen=True)
class WordItem:
    """Сontainer for a word.

    Attributes:
        text: The word(must not be empty).
        weight: Importance weight (must be >= 0).
    
    Raises:
        ValueError: If text is empty or weight is negative.
    """
    text: str
    weight: float

    def __post_init__(self):
        if not self.text.strip():
            raise ValueError("text must not be empty or whitespace")
        if self.weight < 0:
            raise ValueError("weight must be >= 0")
    
    @property
    def length(self)->int:
        return len(self.text)

@dataclass(frozen=True)
class OptimizerConfig:
    """Configuration for the optimizer.

    Attributes:
        max_vocab_size: Maximum allowed vocabulary size (must be > 0).
        min_word_length: Minimum length of words to consider (must be > 0).

    Raises:
        ValueError: If max_vocab_size <= 0 or min_word_length <= 0.
    """
    max_vocab_size: int
    min_word_length: int = 5

    def __post_init__(self):
        if self.max_vocab_size <= 0:
            raise ValueError("max_vocab_size must be > 0")
        if self.min_word_length <= 0:
            raise ValueError("min_word_length must be > 0")

@dataclass(frozen=True)
class NGramVocab:
    """NGram vocabulary container.

    Attributes:
        max_size: Maximum vocabulary size (must be > 0).
        grams: Set of n-grams (must not contain empty strings).

    Raises:
        ValueError: If max_size <= 0 or grams contain empty strings.
    """
    max_size: int
    grams: set[str]
    
    def __post_init__(self):
        if self.max_size <= 0:
            raise ValueError("max_size must be > 0")
        if len(self.grams) > self.max_size:
            raise ValueError("grams size exceeds max_size")
        if any(not gram.strip() for gram in self.grams):
            raise ValueError("grams must not contain empty strings")