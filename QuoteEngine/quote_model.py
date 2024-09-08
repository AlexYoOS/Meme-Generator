"""
Python class that defines a Quote object,
which contains text fields for body and author.
The class overrides the correct methods to instantiate the class
and print the model contents as: ”body text” - author
"""


class QuoteModel:
    """
    Represents a quote object.
    """

    def __init__(self, body_text, author):
        """
        Initialize a QuoteModel instance.

        Args:
            body_text (str): The text of the quote.
            author (str): The author of the quote.
        """
        self.body_text = body_text
        self.author = author

    def __str__(self):
        """
        Return a string representation of the QuoteModel object.

        Returns:
            str: The quote in a meme format.
        """
        return self.body_text + '-' + self.author
