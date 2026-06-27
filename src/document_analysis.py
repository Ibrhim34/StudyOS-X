"""
Document Analysis Engine

Responsible for analyzing the document
and generating the initial Document Blueprint.
"""

from pdf_reader import PDFReader
from structure_analyzer import StructureAnalyzer


class DocumentAnalysisEngine:

    def __init__(self):
        self.reader = PDFReader()
        self.structure = StructureAnalyzer()

    def execute(self, pdf_path):

        print(f"\nReading document: {pdf_path}")

        try:

            # ==========================
            # Read PDF
            # ==========================

            pdf = self.reader.read(pdf_path)

            # ==========================
            # Analyze Structure
            # ==========================

            structure = self.structure.analyze(pdf)

            metadata = pdf["metadata"]

            # ==========================
            # Build Blueprint
            # ==========================

            blueprint = {
                "title": metadata.get("title") or "Unknown",
                "author": metadata.get("author") or "Unknown",
                "subject": metadata.get("subject") or "Unknown",
                "language": metadata.get("language") or "Unknown",

                "pages": pdf["page_count"],
                "characters": pdf["character_count"],
                "words": pdf["word_count"],

                "headings": structure["heading_count"]
            }

            # ==========================
            # Print Blueprint
            # ==========================

            print("\n" + "=" * 60)
            print("DOCUMENT BLUEPRINT")
            print("=" * 60)

            for key, value in blueprint.items():
                print(f"{key.capitalize():15}: {value}")

            # ==========================
            # Print Statistics
            # ==========================

            print("\n" + "=" * 60)
            print("PDF STATISTICS")
            print("=" * 60)

            print(f"Pages      : {pdf['page_count']}")
            print(f"Characters : {pdf['character_count']}")
            print(f"Words      : {pdf['word_count']}")

            # ==========================
            # Print Structure
            # ==========================

            print("\n" + "=" * 60)
            print("DOCUMENT STRUCTURE")
            print("=" * 60)

            print(f"Detected Headings : {structure['heading_count']}")

            if structure["heading_count"] == 0:
                print("No headings detected.")
            else:
                print()

                for heading in structure["headings"][:10]:
                    print(f"[Page {heading['page']}] {heading['title']}")

                if structure["heading_count"] > 10:
                    print(
                        f"\n... and {structure['heading_count'] - 10} more headings."
                    )

            print("\nDocument Blueprint Created Successfully.")

            return {
                "blueprint": blueprint,
                "structure": structure,
                "pdf": pdf
            }

        except FileNotFoundError:

            print("\nERROR: PDF file not found.")

            return None

        except Exception as e:

            print(f"\nERROR: {e}")

            return None
