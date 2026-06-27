"""
Document Analysis Engine

Responsible for analyzing the document
and generating the initial Document Blueprint.
"""

from pdf_reader import PDFReader


class DocumentAnalysisEngine:

    def __init__(self):
        self.reader = PDFReader()

    def execute(self, pdf_path):

        print(f"Reading document: {pdf_path}")

        try:

            pdf = self.reader.read(pdf_path)

            metadata = pdf["metadata"]

            blueprint = {
                "title": metadata.get("title") or "Unknown",
                "author": metadata.get("author") or "Unknown",
                "subject": metadata.get("subject") or "Unknown",
                "language": metadata.get("language") or "Unknown",

                "pages": pdf["page_count"],
                "characters": pdf["character_count"],
                "words": pdf["word_count"]
            }

            print("\n========== Document Blueprint ==========\n")

            for key, value in blueprint.items():
                print(f"{key.capitalize():12}: {value}")

            print("\n========== PDF Statistics ==========\n")

            print(f"Pages      : {pdf['page_count']}")
            print(f"Characters : {pdf['character_count']}")
            print(f"Words      : {pdf['word_count']}")

            print("\nDocument Blueprint Created Successfully.")

            return blueprint

        except Exception as e:

            print(f"\nError reading PDF: {e}")

            return None
