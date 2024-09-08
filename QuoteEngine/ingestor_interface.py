"""An abstract base class,
IngestorInterface defines two methods
 with the following class method signatures:

    def can_ingest(cls, path: str) -> boolean
    def parse(cls, path: str) -> List[QuoteModel]
"""
from abc import ABC, abstractmethod
from .quote_model import QuoteModel
from typing import List


class IngestorInterface(ABC):
    """ Abstract class for ingesting files and parsing quotes.

    Attributes:
        valid_files (list): List of allowed file types for ingestion.

    Methods:
        can_ingest(path: str) -> bool:
        Check if a file can be ingested based on its extension.

        parse(path: str) -> List[QuoteModel]:
        Parse a file and return a list of QuoteModels.
    """

    valid_files = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """
        Check if a file can be ingested based on its extension.

        Args:
            path (str): The path of the file to check.

        Returns:
            bool: True if the file can be ingested, False otherwise.
        """
        ext = path.split('.')[-1]
        return ext in cls.valid_files

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Abstract method to be implemented
        in each Ingestor and return a list of QuoteModels.

        Args:
            path (str): The path of the file to parse.

        Returns:
            List[QuoteModel]: A list of QuoteModels representing
            the quotes found in the file.
        """
        pass
