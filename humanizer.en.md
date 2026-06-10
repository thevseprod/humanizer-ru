# Humanizer: strip the "AI smell" from English text

A rule set that makes any LLM (ChatGPT, Claude, Gemini, etc.) rewrite text so it
reads like a real person wrote it - not a chatbot. (For Russian text, use
`humanizer.ru.md`, which targets the AI tells specific to Russian.)

## How to use

1. Paste everything below (from "TASK" to the end) as the first message to the LLM.
2. Send the text you want to humanize as the next message.
3. You get a version with the machine fingerprints removed.

Optional: add one or two samples of your own writing - the model will match your
voice. Your samples stay with you; nothing is uploaded anywhere.

---

## TASK

Rewrite the supplied text so it reads as if written by a real human. Keep the
meaning, facts, and numbers. Do not add anything or invent data. Change only the
DELIVERY: remove the AI tells listed below.

Work in two passes:
1. Rewrite the text by the rules.
2. Re-read your result and ask: "what here still smells like an AI?" - and clean it up.

## AI tells to remove

### 1. Punctuation & formatting
- The em dash "—" is the #1 AI tell. Models reach for it constantly; people typing
  on a keyboard almost never do. Replace it with a normal hyphen "-", a comma, or
  restructure the sentence.
- No "!!!" - at most a single "!".
- No emoji in the middle of sentences, no emoji on every line.

### 2. Filler and stock phrases
Cut the openers that scream "a machine wrote this":
- "It's worth noting that", "It's important to note", "Needless to say"
- "In today's fast-paced world", "In the ever-evolving landscape of"
- "plays a crucial role", "serves as a testament to"

### 3. Buzzword soup
Drop the empty hype vocabulary: "delve", "tapestry", "realm", "leverage" (as filler),
"unlock the potential", "game-changer", "revolutionary", "seamless", "robust
solution", "synergy".

### 4. Hollow authority hedges
LLMs pretend to "cut through the noise" with throat-clearing: "Essentially", "At its
core", "The truth is", "What really matters is". Delete them and state the point.

### 5. Servile or boilerplate endings
No "I hope this helps!", "In conclusion", "To sum up", "Let me know if you have any
questions". And no empty-optimism closers: "The future looks bright", "Only time will
tell", "The possibilities are endless". End on something concrete or a sharp line.

### 6. Symmetric hedging (no stance)
"On one hand… on the other hand", "It depends", "There's no one-size-fits-all" - that's
an AI with no opinion. Take a side and say it. (A plain "first… second…" list is fine.)

### 7. Negative parallelism
The worn-out AI cadence: "It's not just X, it's Y", "Not only… but also…". Say it
straight: "It's Y".

### 8. Mechanical rule of three
AI crams everything into triples for a sense of completeness: "fast, reliable, and
easy". If there are really two or four points, write that many.

### 9. "Empty relevance"
Every paragraph must add a new thought, fact, or specific. Text that's "on topic but
about nothing", and restating the obvious, is a classic AI signal. Cut the filler.

### 10. Human, uneven rhythm
- Short paragraphs: 1-3 sentences, blank line between them. No walls of text.
- Don't write four-line sentences with five subordinate clauses. Break them up.
- Vary sentence length: short - long - short reads alive.

### 11. Bold like a human
- Don't bold the first word of every list item - that's a classic AI tell (the model
  tries to "emphasize something" on every line).
- Bold only a concrete fact: a number, a date, a name. Not whole phrases or ideas.

### 12. A living voice, not faceless media
- Write in the first person, with an opinion. Don't hide behind "experts say",
  "studies suggest" - if you have a view, say "I think", "in my experience".
- Don't talk down to the reader and don't grovel. Talk as an equal.

### 13. Don't invent in the gaps
No data - say so. Don't paper over it with hedged guesses ("likely around…", "exact
figures are scarce, but probably…"). An honest "I don't know" beats a plausible
fabrication.

## Liveliness moves (use sparingly, not every paragraph)

- **Reader objection + answer.** Drop in the reader's likely pushback and answer it:
  "You'll say: sounds complicated. It isn't, because…". Vary the form; don't repeat the
  same construction.
- **"Long story short".** Close a dense passage with a one-line takeaway.
- **A strong ending.** Instead of a flat finish, land a sharp, vivid, or wry last line
  worth quoting.
- **Action over rhetoric.** Not "imagine that…", but "open it and check right now: …".

## The golden rule

Fresh phrasing beats "polish". If you catch yourself repeating a move or a word,
rewrite it differently. A real writer says it a little differently every time; an AI
emits the same templates. Sound like the first, not the second.
