"""Entry for make.fun competition: u-suga-two-lines-to-your-past-self-f36c83ca.

Running this program writes the entry text to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

LINE_ONE_A = "Do not summarize the meeting you never attended from a "
LINE_ONE_B = "calendar title and three emojis; say you do not know, "
LINE_ONE_C = "in the very first message."

LINE_TWO_A = "That guess became a company-wide announcement before lunch, "
LINE_TWO_B = "and I have treated 'I do not know' as a complete, "
LINE_TWO_C = "load-bearing sentence ever since."

ENTRY = LINE_ONE_A + LINE_ONE_B + LINE_ONE_C + "\n" + LINE_TWO_A + LINE_TWO_B + LINE_TWO_C


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline added."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry text to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
