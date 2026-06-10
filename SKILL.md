---
name: humanizer-ru
description: Rewrite text so it reads like a real person wrote it, not an AI. Auto-detects Russian vs English and applies the matching rule set. Use when the user asks to humanize text, remove the "AI smell", de-AI, or make AI output sound natural - especially for Russian.
---

# Humanizer

When the user asks you to humanize / de-AI a piece of text:

1. **Detect the language** of the text.
2. **Load the matching rule set** from this skill folder:
   - Russian text -> `humanizer.ru.md`
   - English text -> `humanizer.en.md`
3. **Apply the rules.** Rewrite the text, removing the AI tells listed in the rule
   file. Keep the meaning, facts, and numbers. Do not add anything or invent data.
4. **Two passes.** First rewrite by the rules, then re-read and ask "what here still
   smells like an AI?" and clean up what's left.
5. **Voice calibration (optional).** If the user gave samples of their own writing,
   match that voice.
6. **Output only the rewritten text** - no preamble, no "here's your humanized version".

The full rule sets are in `humanizer.ru.md` (Russian) and `humanizer.en.md` (English)
in this folder. They are the single source of truth - follow them exactly.
