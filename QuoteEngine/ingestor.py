"""
Bundled Subclass "Ingestor" that combines the loading
from from following supported file types: text, docx, csv, pdf.
"""

from typing import List
from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from .docx_ingestor import DocxIngestor
from .txt_ingestor import TxtIngestor
from .csv_ingestor import CSVIngestor
from .pdf_ingestor import PDFIngestor


class Ingestor(IngestorInterface):
    """
    Subclass Ingests data files.
    """
    ingestors = [CSVIngestor,
                 DocxIngestor,
                 PDFIngestor,
                 TxtIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """
        Parse the given file and return a list of QuoteModel objects.
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
