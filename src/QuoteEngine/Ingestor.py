"""
Represents the main library for all pathway-specific quote ingestors.
Reference.
Solution is modifed from sample code from lecture,below URL.
Lesson 5, Concept 7: Exercise - Complex Strategy:
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/7dc605c8-0ee3-4f58-ba0c-2ccaecad515e/concepts/41686665-e20c-4656-81bb-2b6d2f5320c6
Almost same with below URL.
https://github.com/conjohnson712/Meme_Generator/blob/main/QuoteEngine/Ingestor.py
"""
from typing import List

from .CSVIngestor import CSVIngestor
from .DocxIngestor import DocxIngestor
from .IngestorInterface import IngestorInterface
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """
    Encapsulates Concrete Ingestor Classes, Realizes IngestorInterface.
    param ingestors: A list of different accepted Ingestors.
    """

    ingestors = [DocxIngestor,  CSVIngestor, PDFIngestor, TextIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse quotes according to file pathway type.
        param path: The desired file pathway.
        return: A list of QuoteModels from each Ingestor type.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
