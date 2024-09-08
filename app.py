"""App function."""
import random
import os
import requests
from flask import Flask, render_template, abort, request
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = [quote for i in quote_files for quote in Ingestor.parse(i)]

    images_path = "./_data/photos/dog/"

    # Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []

    try:
        for root, _, files in os.walk(images_path):
            for name in files:
                imgs.append(os.path.join(root, name))

    except Exception as e:
        print("An error occurred trying to load image:", str(e))

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme.
    Use the random python standard library class to:

    - select a random image from imgs array
    - select a random quote from the quotes array
    """
    img = None
    quote = None

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body_text, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    - Use requests to save the image from the image_url,
      form param to a temp local file.
    - Use the meme object to generate a meme using this temp
      file and the body and author form paramaters.
    - Remove the temporary saved image.

    """
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    try:
        r = requests.get(image_url)
        tmp = f'./tmp({random.randint(0,100000000)}).jpg'
        with open(tmp, 'wb') as img:
            img.write(r.content)

        path = meme.make_meme(tmp, body, author)
        return render_template('meme.html', path=path)

    except Exception:
        print('Not .jpg or .png image URL, please provide another URL')
        return render_template('meme_error.html')

    finally:
        if 'tmp' in locals():
            os.remove(tmp)


if __name__ == "__main__":
    app.run()
