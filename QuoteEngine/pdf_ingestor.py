"""PDF Filetype Ingestor Subclass"""

from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from typing import List
import subprocess
import random
import os
import re


class PDFIngestor(IngestorInterface):
    """
    A class for ingesting PDF files and parsing quotes.

    Methods:
        can_ingest(path: str) -> bool:
        Check if a PDF file can be ingested based on its extension.

        parse(path: str) -> List[QuoteModel]:
        Parse a PDF file and return a list of QuoteModels.
    """

    valid_files = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return QuoteModels for each quote found in the PDF parsed file."""
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest Exception')

        tmp = f'./tmp/{random.randint(0, 1000000)}.txt'

        _ = subprocess.call(['pdftotext', path, tmp])

        with open(tmp, "r") as file_ref:
            content = file_ref.readlines()[:-2][0].strip()

        os.remove(tmp)
        quotes = []
        # extract quotes
        quote = re.findall(r'"([^"]*)"', content)

        # extract authors
        if not content.endswith('"'):
            content += '"'
        authors = re.findall(r'-(.*?)\"', content)
        authors = [author.strip() for author in authors]

        # zip quotes and authors together
        quote_models = [
            QuoteModel(quote, author)
            for quote, author in zip(quote, authors)
        ]

        # add quote_models to the existing quotes list
        quotes.extend(quote_models)

        return quotes
