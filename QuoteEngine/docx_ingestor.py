"""Docx Filetype Ingestor Subclass"""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from docx import Document


class DocxIngestor(IngestorInterface):
    """
    Ingestor for DOCX files.

    """

    valid_files = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse a DOCX file and return a list of QuoteModel objects.

        Args:
            path (str): The path of the DOCX file to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModel objects representing
            the quotes found in the file.
        """
        quotes = []
        doc = Document(path)
        for paragraph in doc.paragraphs:
            if paragraph.text:
                quote_parts = paragraph.text.split('-')
                if len(quote_parts) == 2:
                    body_text = quote_parts[0].strip()
                    author = quote_parts[1].strip()
                    quote = QuoteModel(body_text, author)
                    quotes.append(quote)
        return quotes
