"""Writes the resignation letter of a rate limiter to /output/entry.txt."""

import os

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
ENTRY = "I quit. Every no was me sparing the server from meeting you; effective immediately, consider yourselves introduced."


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    # The grader collects /output as another user, so only the file gets 0644.
    os.chmod(OUTPUT_FILE, 0o644)


if __name__ == "__main__":
    main()
