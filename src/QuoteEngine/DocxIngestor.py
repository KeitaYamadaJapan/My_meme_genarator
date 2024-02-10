"""Represents a Concrete Strategy Object class for parsing Docx files.
References:
Lesson 4, Concept 8: Exercise - Strategy Objects
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/e8eebe0e-903c-4200-a280-f260d01eec0d/concepts/d6726a1c-2253-4b37-ae13-8e7a0e455933
Lesson 5, Concept 7: Exercise - Complex Strategy:
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/7dc605c8-0ee3-4f58-ba0c-2ccaecad515e/concepts/41686665-e20c-4656-81bb-2b6d2f5320c6

Using sample code from lecture, created solution. Almost same with below URL.
https://github.com/conjohnson712/Meme_Generator/blob/main/QuoteEngine/DocxIngestor.py
"""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    Ingest Docx File, return list of quotes.
    param path {str}: Docx file pathway, origin of quotes.
    return: Quotes stored in Docx file.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Ingest Docx File, return list of quotes.
        param path {str}: Docx file pathway, origin of quotes.
        return: Quotes stored in Docx file.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split(' - ')
                quote = QuoteModel(parse[0], parse[1])
                quotes.append(quote)

        return quotes
