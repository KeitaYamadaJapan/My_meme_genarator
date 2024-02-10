"""
QuoteModel Class.
Solution modified from Cat.py at URL below.
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/7dc605c8-0ee3-4f58-ba0c-2ccaecad515e/concepts/41686665-e20c-4656-81bb-2b6d2f5320c6
Almost same with
https://github.com/conjohnson712/Meme_Generator/blob/main/QuoteEngine/QuoteModel.py
"""


class QuoteModel():
    """Creates a class that formats Quotes and Authors for memes."""

    def __init__(self, body, author):
        """
        Initialize quote model object.
        param body: The quote
        param author: The author of the quote
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a computer-readable string to represent full quotes."""
        return f"{self.body} + ' - ' + {self.author}"
