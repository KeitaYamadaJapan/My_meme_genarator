"""
Represents an Ingestor specified for .txt files.
References:
Lesson 4, Concept 8: Exercise - Strategy Objects
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/e8eebe0e-903c-4200-a280-f260d01eec0d/concepts/d6726a1c-2253-4b37-ae13-8e7a0e455933
Lesson 5, Concept 7: Exercise - Complex Strategy:
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/7dc605c8-0ee3-4f58-ba0c-2ccaecad515e/concepts/41686665-e20c-4656-81bb-2b6d2f5320c6

Using sample code,created solution. Almost same with
https://github.com/conjohnson712/Meme_Generator/blob/main/QuoteEngine/TextIngestor.py
"""
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """
    Create an Concrete Class Object for parsing txt file pathways.
    param allowed_extensions: File pathway allowed in this ingestor.
    """

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path) -> List[QuoteModel]:
        """
        Ingest txt File, return list of quotes.
        param path {str}: txt file pathway, origin of quotes.
        return: Quotes stored in txt file.
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        with open(path, 'r') as infiles:
            for line in infiles.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parse = line.split(' - ')
                    quote = QuoteModel(parse[0], parse[1])
                    quotes.append(quote)

            infiles.close()
            return quotes
