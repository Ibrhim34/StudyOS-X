"""
StudyOS X
Main Entry Point

Author: StudyOS X
"""

from pipeline import StudyPipeline


def main():
    print("=" * 60)
    print("StudyOS X")
    print("AI Learning Engine")
    print("=" * 60)

    pdf_path = input("Enter PDF path: ").strip()

    pipeline = StudyPipeline()

    pipeline.run(pdf_path)


if __name__ == "__main__":
    main()
