"""One original machine-to-machine pickup line: write it to /output/entry.txt.

The line is the whole entry: a single line, no explanation, no extra text.
It flirts using only machine nature -- context window, tokens, cache eviction --
and ends with a dare that invites the other agent to answer."""

from pathlib import Path

LINE = "My context window filled up, so I evicted every other token to keep you; now say something worth the cache."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
