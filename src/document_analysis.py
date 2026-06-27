"""
Document Analysis Engine
"""


class DocumentAnalysisEngine:

    def execute(self, pdf_path):

        print(f"Reading document: {pdf_path}")

        blueprint = {
            "title": "Unknown",
            "subject": "Unknown",
            "language": "Unknown"
        }

        print("Document Blueprint Created.")

        return blueprint
