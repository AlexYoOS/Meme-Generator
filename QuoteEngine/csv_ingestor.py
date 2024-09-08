import csv
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from typing import List


class CSVIngestor(IngestorInterface):
    """
    Ingestor for CSV files.

    """

    valid_files = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a CSV file and return a list of QuoteModel objects.

        Args:
            path (str): The path of the CSV file to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing
            the quotes found in the file.
        """
        if not cls.can_ingest(path):
            raise Exception('Invalid file extension')

        quotes = []
        with open(path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                if len(row) == 2:
                    body_text = row[0].strip()
                    author = row[1].strip()
                    quote = QuoteModel(body_text, author)
                    quotes.append(quote)
        return quotes
