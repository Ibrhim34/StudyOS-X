"""
StudyOS X Pipeline
"""

from document_analysis import DocumentAnalysisEngine


class StudyPipeline:

    def __init__(self):
        self.document_engine = DocumentAnalysisEngine()

    def run(self, pdf_path):

        print("\n[Stage 1] Document Analysis")

        blueprint = self.document_engine.execute(pdf_path)

        print("\nPipeline Finished Successfully.")

        return blueprint
