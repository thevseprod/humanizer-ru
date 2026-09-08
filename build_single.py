#!/usr/bin/env python3
"""Собрать SKILL.md из двух файлов правил — чтобы скилл ставился одним файлом.

Скилл раньше подгружал `humanizer.ru.md` и `humanizer.en.md` рядом с собой. Для
установки одной командой это нормально, а вот перенести его куда-то одним
файлом было нельзя: правила остались бы снаружи, и скилл искал бы их впустую.

Источник правды — по-прежнему два файла с правилами. Этот скрипт просто
вклеивает их в SKILL.md. Правила правим в них, потом запускаем:

    python3 build_single.py
"""

from pathlib import Path

ROOT = Path(__file__).parent
HEAD = """---
name: humanizer-ru
version: {version}
description: {description}
license: MIT
compatibility: any-agent
allowed-tools:
  - Read
  - Write
  - Edit
---

# Humanizer

Когда просят «оживить» текст, убрать «запах ИИ», сделать по-человечески:

1. Определи язык текста.
2. Возьми нужный набор правил ниже: русский текст - русские правила,
   английский - английские.
3. Перепиши по правилам. Смысл, факты и цифры сохрани. Ничего не добавляй и не
   выдумывай.
4. Пройди дважды: сначала перепиши, потом перечитай и спроси себя, что здесь
   всё ещё пахнет нейросетью. Дочисти.
5. Если человек дал примеры своего текста - подгони результат под его манеру.
6. Отдай только переписанный текст. Без предисловий и без «вот ваша
   человечная версия».

Правила ниже - единственный источник правды, следуй им точно.

<!-- СОБРАНО АВТОМАТИЧЕСКИ из humanizer.ru.md и humanizer.en.md.
     Руками не править: правь файлы правил и запусти build_single.py -->
"""

DESCRIPTION = (
    'Rewrite text so it reads like a real person wrote it, not an AI. '
    'Auto-detects Russian vs English and applies the matching rule set. '
    'Use when the user asks to humanize text, remove the "AI smell", de-AI, '
    'or make AI output sound natural - especially for Russian.'
)


def strip_intro(text: str, marker: str) -> str:
    """Отрезать вступление файла правил: в собранном скилле оно лишнее."""
    i = text.find(marker)
    return text[i:].rstrip() if i != -1 else text.strip()


def main() -> None:
    version = "1.3.0"
    ru = strip_intro((ROOT / "humanizer.ru.md").read_text(encoding="utf-8"),
                     "## ЗАДАЧА")
    en = strip_intro((ROOT / "humanizer.en.md").read_text(encoding="utf-8"),
                     "## TASK")

    out = (
        HEAD.format(version=version, description=DESCRIPTION)
        + "\n---\n\n# Правила для русского текста\n\n" + ru
        + "\n\n---\n\n# Rules for English text\n\n" + en + "\n"
    )
    (ROOT / "SKILL.md").write_text(out, encoding="utf-8")
    print(f"SKILL.md собран: {len(out)} знаков")


if __name__ == "__main__":
    main()
