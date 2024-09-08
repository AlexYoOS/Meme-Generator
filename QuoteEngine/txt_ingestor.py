from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from typing import List


class TxtIngestor(IngestorInterface):
    """
    Ingestor for TXT files.

    """

    valid_files = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a TXT file and return a list of QuoteModel objects.

        Args:
            path (str): The path of the TXT file to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing
            the quotes found in the file.
        """
        quotes = []
        with open(path, 'r', encoding='utf-8-sig') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split('-')
                    if len(parts) == 2:
                        body_text = parts[0].strip()
                        author = parts[1].strip()
                        quote = QuoteModel(body_text, author)
                        quotes.append(quote)
        return quotes
