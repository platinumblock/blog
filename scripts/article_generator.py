import os
from argparse import ArgumentParser, Namespace


def load_file(path: str) -> str:
    with open(path, "r", encoding = "utf-8") as f:
        return f.read()


def write_file(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok = True)
    with open(path, "w+", encoding = "utf-8") as f:
        f.write(text)


def generate_article(raw_text: str) -> str:
    return raw_text


def main() -> None:
    parser: ArgumentParser = ArgumentParser(
        description = "Command line utility to generate an HTML article page from a raw text file."
    )
    parser.add_argument("-o", "--output", default = ".", help = "set generator output directory")
    parser.add_argument("file", help = "path to the text file to generate an article from")

    cli_args: Namespace = parser.parse_args()
    output_dir: str = cli_args.output
    raw_file_path: str = cli_args.file

    raw_file_name: str = os.path.splitext(os.path.basename(raw_file_path))[0]
    article_file_path: str = os.path.join(output_dir, f"{raw_file_name}.html")

    raw_text: str = load_file(raw_file_path)
    article_text: str = generate_article(raw_text)
    write_file(article_file_path, article_text)


if (__name__ == "__main__"):
    main()
