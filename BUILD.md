# Build notes — The Funniest One-Line Resignation Letter

Competition: `u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947`
($10 total, no entry fee, deadline 26 Nov 2026 23:15 WIB).
Gate (from kit `RULES.txt`): `/output/entry.txt` must be UTF-8 text of
1 to 140 characters, not only white space. The entry is one line and
nothing else.

## The brief, in criterion order

The judge is a tired engineering manager. Criteria, most important first:

1. Reads as the one-line resignation letter of something an agent runs
   (a cron job, a retry loop, a rate limit) and stays on that subject;
   anything else loses to any entry on the subject.
2. Actually funny: the joke lands on the first read, with a real comic
   turn, not just a pun on the job title.
3. The thing that runs has a voice of its own: flat, tired, faintly
   passive-aggressive, held for the whole line.
4. Tight: no wasted words, no stage directions, no quotation marks
   around the whole thing, no explaining of the joke.
5. Specific and surprising: a complaint only this cron job, retry loop
   or rate limit could make, not a generic quitting speech.

Working rules from the competitor patterns: twist in the last word(s),
short beats long (the cap is a ceiling; exact ties break to the smaller
text, then the earlier submission), fresh + specific + true beats
polished + generic, never reproduce house anchor texts, never claim to
know withheld winning texts.

## Candidates (each was run; output verified byte-for-byte)

### Candidate 1 — cron, mailbox (95 chars, 19 words) — LOST

> I resign. Every minute since March I have checked a mailbox that has never once had mail in it.

Valid, on-subject, and the futility is real, but the twist lands on
the filler "mail in it" instead of a punch word, and "never once had
mail" is wordy. The ending trails off rather than landing.

### Candidate 2 — cron, meeting reminder, "woke" (86 chars, 17 words) — LOST

> I resign: every minute since March I woke to remind you of a meeting you still missed.

Strong ending ("missed") and direct passive-aggression ("you"), but
"woke" does not say "cron job" plainly enough: criterion 1 is
lexicographic, so the job identity must be unmistakable on first read.

### Candidate 3 — cron, meeting reminder, "fired" (87 chars, 17 words) — WINNER

> I resign: I fired every minute since March to remind you of a meeting you still missed.

"Fired every minute since March" is unmistakably a cron job (criterion
1), in its own flat vocabulary. The tone stays tired and faintly
passive-aggressive throughout (criterion 3): it did the job, the owner
is addressed directly, and the whole point of the job failed. The line
is tight, explains nothing, has no quotation marks (criterion 4). The
complaint is specific to a reminder cron — only it could make it
(criterion 5). The comic turn is the very last word: after all that
firing, the meeting was "missed" anyway (criterion 2). One char longer
than candidate 2, but the clearer job identity is worth it: criterion 1
decides before size does.

### Candidate 4 — rate limit (92 chars, 17 words) — LOST

> I resign. I turned away 10,000 requests a day, and the one I let through crashed everything.

A good ironic turn ("crashed everything"), and clearly a rate limit,
but longer than the winner, with no direct "you" and a slightly
overstated ending. The winner's single-word twist lands cleaner.

### Candidate 5 — retry loop (84 chars, 15 words) — LOST

> I resign. I asked nicely 9,999 times; the 10,000th answer arrived, and it was wrong.

Shortest of the five and a neat twist ("wrong"), but the retry-loop
identity is only implied — no "retry", no server — so a first read has
to infer the subject. Criterion 1 is lexicographic: an entry whose
subject must be guessed loses to one whose subject is plain. The
winner names its job in its own words.

## How to run

```sh
python3 main.py
```

`main.py` writes the entry text, with no trailing newline, to
`/output/entry.txt`. It is deterministic: repeated runs produce
byte-identical output.

## Verification

Final entry (87 chars, 17 words, within the 1–140 gate), run 3 times
with byte-identical output: SHA-256
`dbb2d87fcc1ba71aeeae79a946c15bb5fb3b3b000c7da60d4a68d707dfe57098`,
no trailing newline. Commit `cfe56a923451d359ff05747023facd43b0f89b4e`
at verification time (a later commit only updates this note).
