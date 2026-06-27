"""
Structure Analyzer

Detects the logical structure of a PDF document.
"""

import re


class StructureAnalyzer:

    def analyze(self, pdf):

        headings = []

        for page in pdf["pages"]:

            lines = page["text"].split("\n")

            for line in lines:

                text = line.strip()

                if not text:
                    continue

                # Ignore very long lines
                if len(text) > 80:
                    continue

                # Ignore very short lines
                if len(text) < 3:
                    continue

                # Simple heading detection
                if (
                    text.isupper()
                    or re.match(r"^\d+(\.\d+)*\s+", text)
                    or text.endswith(":")
                ):

                    headings.append({
                        "page": page["page"],
                        "title": text
                    })

        return {
            "heading_count": len(headings),
            "headings": headings
        }
