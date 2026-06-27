"""
Text Cleaning Engine

Responsible for cleaning raw text extracted from PDF documents.
"""

import re


class TextCleaner:
    """
    Cleans raw PDF text before content extraction.
    """

    def clean(self, text: str) -> str:
        """
        Clean extracted PDF text.

        Args:
            text: Raw extracted text.

        Returns:
            Cleaned text.
        """

        if not text:
            return ""

        # Normalize line endings
        text = text.replace("\r\n", "\n")
        text = text.replace("\r", "\n")

        # Remove tabs
        text = text.replace("\t", " ")

        # Remove multiple spaces
        text = re.sub(r"[ ]{2,}", " ", text)

        # Remove excessive blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        # Remove page numbers on separate lines
        text = re.sub(r"^\s*\d+\s*$", "", text, flags=re.MULTILINE)

        # Remove trailing spaces
        text = "\n".join(line.rstrip() for line in text.splitlines())

        return text.strip()
