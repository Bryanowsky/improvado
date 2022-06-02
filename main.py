import argparse

from improvado.improvado import Improvado


def main():
    parser = argparse.ArgumentParser(description="Extract data from some files and export it into a new file")
    parser.add_argument("files", metavar="F", type=str, nargs="+", help="File(s) whose data will be extracted")
    parser.add_argument(
        "--out", dest="output_file", metavar="O", type=str, nargs="?", default="output.tsv",
        help='File that will store the final data'
    )
    args = parser.parse_args()

    improvado = Improvado()
    improvado.extract_data(filenames=args.files)
    improvado.export_data(filename=args.output_file)


if __name__ == "__main__":
    main()
