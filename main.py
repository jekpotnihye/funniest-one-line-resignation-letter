"""One-line resignation letter of a cron job.

Writes the entry text, and nothing else, to /output/entry.txt.
"""

ENTRY = "I resign: I fired every minute since March to remind you of a meeting you still missed."


def main():
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
