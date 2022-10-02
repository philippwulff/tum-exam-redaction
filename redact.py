import fitz
import argparse

# (horizontal, vertical)
first_page_areas = [
    [(550, 25), (590, 25), (550, 60), (590, 60)],   # top right BC
]
areas = [
    [(540, 15), (585, 15), (540, 40), (585, 40)],   # top right BC
    [(15, 15), (60, 15), (15, 40), (60, 40)],   # top left BC
    [(410, 810), (585, 810), (410, 830), (585, 830)],   # bottom right BC
    [(15, 810), (165, 810), (15, 830), (165, 830)],   # bottom left BC
    [(5, 230), (15, 230), (5, 350), (15, 350)],   # lu vertical text
    [(5, 500), (15, 500), (5, 620), (15, 620)],   # ll vertical text
    [(580, 90), (590, 90), (580, 200), (590, 200)],   # ru vertical text
    [(580, 360), (590, 360), (580, 480), (590, 480)],   # rm vertical text
    [(580, 650), (590, 650), (580, 780), (590, 780)],   # rl vertical text
]


def main(args):

    pdf = fitz.open(args.input)
    for i, page in enumerate(pdf):
        if i == 0:
            [page.add_redact_annot(area, fill=(0,0,0)) for area in first_page_areas]
        
        # page._wrapContents()

        [page.add_redact_annot(area, fill=(0,0,0)) for area in areas]
        page.apply_redactions()

    output_path = args.output if args.output else args.input.split("/")[-1].split(".pdf")[0] + "_redacted.pdf"
    pdf.save(output_path)
    print("DONE")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="TUM Exam Redaction Tool")

    parser.add_argument("--input", "-i", type=str, required=True, help="Path to input PDF")
    parser.add_argument("--output", "-o", type=str, default="", help="Path to output file")

    main(args=parser.parse_args())


