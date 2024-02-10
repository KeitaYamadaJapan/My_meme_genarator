"""Module responsible for superimposing quotes onto images
References:
Lesson 4, Concept 6: Exercise - Pillow:
https://learn.udacity.com/nanodegrees/nd303/parts/cd0011/lessons/e8eebe0e-903c-4200-a280-f260d01eec0d/concepts/34bb1bf3-5794-438c-96f9-c9dd7a01c36a
Knowledge Solution for Corrupted Font:
https://knowledge.udacity.com/questions/542475

Using sample code from lecture, created solution is almost same with below.
https://github.com/conjohnson712/Meme_Generator/blob/main/MemeEngine/MemeEngine.py
"""
from PIL import Image, ImageDraw, ImageFont
from random import randint
import os
import textwrap


class MemeEngine():
    """Creates memes by placing quotes onto images."""

    def __init__(self, out_folder: str):
        """Initialize the MemeEngine object.
        param out_folder: Storage location of finished memes
        """
        self.out_folder = out_folder

    def make_meme(self, in_path: str,
                  body: str, author: str, width: int = 500) -> str:
        """Create a memes a meme by superimposing a random quote over
        a random image.
        param in_path: The file pathway for the input image.
        param body: The quote that will be superimposed on the image.
        param author: The author of the quote, displayed with quote.
        param width: The width of the displayed image.
        Return:
            str: The file pathway for the output image.
        """

        with Image.open(in_path) as image:
            # resize
            if width is not None:
                ratio = width/float(image.size[0])
                height = int(ratio*float(image.size[1]))
                image = image.resize((width, height), Image.NEAREST)

            if body is not None:
                message = f'{body}\n - {author}'
                import textwrap
                wrapper = textwrap.TextWrapper(width=40)
                message = wrapper.fill(text=message)

                draw = ImageDraw.Draw(image)
                font = ImageFont.truetype(
                    "./MemeGenerator/font/LilitaOne-Regular.ttf", size=22)

                x = randint(0, 100)
                y = randint(0, 200)
                draw.multiline_text((x, y), message, font=font,
                                    fill='white', stroke_width=2,
                                    stroke_fill='black')

            pic = f'/{randint(0,1000)}.jpg'
            out_path = f'{self.out_folder}/{pic}'
            image.save(out_path)

        return out_path
