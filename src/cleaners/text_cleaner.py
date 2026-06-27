"""
Text Cleaning Engine

Responsible for cleaning raw text extracted from PDF documents.
"""

import re


class TextCleaner:
    """
    Cleans raw PDF text before further processing.
    """

    def clean(self, text: str) -> str:
        """
        Clean raw extracted text.

        Args:
            text: Raw text extracted from the PDF.

        Returns:
            Cleaned text.
        """

        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Replace tabs with spaces
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Remove trailing spaces
        text = "\n".join(line.rstrip() for line in text.splitlines())

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove standalone page numbers
        text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)

        return text.strip()