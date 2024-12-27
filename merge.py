from pathlib import Path
import glob
import argparse


def get_paths(pattern):
    return {p for p in glob.glob(pattern, recursive=True) if Path(p).is_file()}


def parse_patterns(input_path):
    includes, excludes = set(), set()

    with open(input_path) as f:
        for line in (l.strip() for l in f if l.strip()):
            target = excludes if line.startswith("!") else includes
            pattern = line[1:] if line.startswith("!") else line
            target.update(get_paths(pattern))

    return includes - excludes


def format_file(path):
    ext = Path(path).suffix.lstrip(".")
    with open(path) as f:
        return f"`{path}`\n\n```{ext}\n{f.read()}```\n\n"


def create_merged_markdown(input_list_path, output_path):
    with open(output_path, "w") as out:
        for path in sorted(parse_patterns(input_list_path)):
            out.write(format_file(path))


def main():
    parser = argparse.ArgumentParser(description="Merge files into a markdown document")
    parser.add_argument(
        "-i",
        "--input",
        default="input.txt",
        help="Input file containing patterns (default: input.txt)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output.md",
        help="Output markdown file (default: output.md)",
    )

    args = parser.parse_args()
    create_merged_markdown(args.input, args.output)


if __name__ == "__main__":
    main()
