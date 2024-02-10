"""
Creates a web-based application to generate memes.
Reference:
Lesson 6, Concept 5: Exercise - Saving with Requests
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/1c6dd7cd-274b-4fa6-a5e2-7d7fc3596f1f/concepts/9a79277b-1d13-4aa6-a63d-b81d54cbe587
Lesson 6, Concept 7: Exercise - Flask App
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/1c6dd7cd-274b-4fa6-a5e2-7d7fc3596f1f/concepts/066d651e-d4ae-454f-91ff-7c83d4217aea
And
https://github.com/conjohnson712/Meme_Generator/blob/main/app.py
"""


import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeGenerator import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quotes.extend(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """
    Get content from meme.html at templates folder

    param img: A randomized image from images.
    param quote: A randomized quote from quotes.
    param path: Gathers the materials to make a meme.
    return: A rendered template containing the random choiced contents of path.
    """

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """
    Using flask create GET method, get meme content from meme_form.html
    placed at templates folder.
    """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():

    """
    Using flask create POST method, get meme content from meme.html
    placed at templates folder.

    param image_url: Request the url of the image file.
    param quote_body: Request the body of the quote.
    param quote_author: Request the author of the quote.
    """
    image_url = request.form.get('image_url')

    quote_body = request.form.get('body')
    quote_author = request.form.get('author')

    try:
        r = requests.get(image_url)
    except requests.exceptions.ConnectionError as e:
        return "Invalid URL. Please Try Again :)"

    out_path = f'./tmp/{random.randint(0, 100000000)}.jpg'
    with open(out_path, 'wb') as img:
        img.write(r.content)
        img.close()

    path = meme.make_meme(out_path, quote_body, quote_author)
    print(out_path)
    os.remove(out_path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
