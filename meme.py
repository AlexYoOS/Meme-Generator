import os
import random
from argparse import ArgumentParser

# Module imports
from QuoteEngine import Ingestor
from QuoteEngine import QuoteModel
from MemeEngine import MemeEngine


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
    path = meme.make_meme(img, quote.body_text, quote.author)
    return path


# Main
if __name__ == "__main__":
    parser = ArgumentParser(description='Meme Generator')
    parser.add_argument('--path', type=str, help='path to an image file')
    parser.add_argument('--body_text', type=str,
                        help='quote body to add to the image')
    parser.add_argument('--author', type=str,
                        help='quote author to add to the image')
    args = parser.parse_args()

    print(generate_meme(args.path, args.body_text, args.author))
