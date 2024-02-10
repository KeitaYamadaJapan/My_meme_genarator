"""
File responsible for generating a meme via CLI.

Reference:
Lesson 5, Concept 4: Exercise - Argparser:
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/7dc605c8-0ee3-4f58-ba0c-2ccaecad515e/concepts/f37bc335-d6fb-4e18-b483-ba7b2c34a30e

Using sample code from lecture, created solution. Almost same with URL blow.
https://github.com/conjohnson712/Meme_Generator/blob/main/meme.py
"""

import os
import random
import argparse

from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":

    """
    Use ArgumentParser to parse CLI arguments.

    param path: path to an image file
    param body: quote body to add to the image
    param author: quote author to add to the image
    Return: A generated meme
    """
    parser = argparse.ArgumentParser(description="Meme Generator")
    parser.add_argument('--path', type=str, default=None,
                        help="The written origin of the quote.")
    parser.add_argument('--body', type=str, default=None,
                        help="The wisdom of our canine friends")
    parser.add_argument('--author', type=str, default=None,
                        help="The canine friend who bestowed the wisdom")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
