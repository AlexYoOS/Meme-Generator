from QuoteEngine import PDFIngestor
from QuoteEngine import QuoteModel

# Path to the PDF file
pdf_path = '_data/DogQuotes/DogQuotesPDF.pdf'

# Call the parse method of the PDFIngestor class
quotes = PDFIngestor.parse(pdf_path)

# Iterate over the quotes and print the quote and author
for quote in quotes:
    print(f'Quote: {quote.body_text}')
    print(f'Author: {quote.author}')
    print()
