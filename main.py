"""Writes the resignation letter of a rate limiter to /output/entry.txt."""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = OUTPUT_DIR + "/entry.txt"
ENTRY = "I quit. Every no was me sparing the server from meeting you; effective immediately, consider yourselves introduced."


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = OUTPUT_FILE
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    # The grader collects the output as another user; the file must be readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
