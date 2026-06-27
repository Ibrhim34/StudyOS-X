"""
PDF Reader
Responsible for reading PDF files and extracting raw text/statistics.
"""

import fitz


class PDFReader:

    def read(self, pdf_path: str):

        doc = fitz.open(pdf_path)

        pages = []
        full_text = ""

        for page_number, page in enumerate(doc, start=1):

            text = page.get_text("text")

            pages.append({
                "page": page_number,
                "text": text
            })

            full_text += text + "\n"

        metadata = doc.metadata

        result = {
            "metadata": metadata,
            "pages": pages,
            "full_text": full_text,
            "page_count": len(doc),
            "character_count": len(full_text),
            "word_count": len(full_text.split())
        }

        doc.close()

        return result
