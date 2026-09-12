from abc import ABC, abstractmethod
from domains import WordItem

class ITextPreprocessor(ABC):
    @abstractmethod
    def preprocess(self, raw_lines: list[str]) -> list[WordItem]:
        """Preprocess raw words and prepare data.

        Args:
            raw_lines (list[str]): word list for preprocess.

        Returns:
            list[WordItem]: list of word dataclasses.
        """
        ...