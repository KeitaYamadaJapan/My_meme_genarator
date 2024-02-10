"""
Represents an interface to parse different data types.
References:
Lesson 3: Concept 6:
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/21ad8849-a08d-4f00-a81c-62a9ff148e9e/concepts/5e30405b-ab29-4593-8e6b-1ef917766f79
Lesson 3: Concept 8:
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/21ad8849-a08d-4f00-a81c-62a9ff148e9e/concepts/e729f00a-7f75-469d-a7bf-d7fe9966a513
Lesson 5, Concept 7: Exercise: Complex Strategy(sample code)
https://classroom.udacity.com/nanodegrees/nd303/parts/bdd52131-b22e-4c57-b3f2-a03951c9d514/modules/5fe343a0-2926-4953-81bc-485ee835e1c6/lessons/93decac5-5e75-4573-b28e-ad1218ec04d3/concepts/6733fc76-b1a7-4c42-9a67-622af43b8cd5

Solution is modified sampl code from lecture. Almost same with below URL.
https://github.com/conjohnson712/Meme_Generator/blob/main/QuoteEngine/Ingestor.py
"""
from abc import ABC, abstractmethod

from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """
    Creates an AbstractBaseClass to ingest various file pathways.
    param allowed_extensions: A list of file extensions.
    """
    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """
        Check if a class can be ingested and parsed.
        param path: The path for the file extension.
        """
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Ingest an extension pathway and return a list of QuoteModels."""
        pass
