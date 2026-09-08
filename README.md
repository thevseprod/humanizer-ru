# humanizer-ru

![humanizer-ru - убираем «запах ИИ» из текста, заточен под русский](assets/banner.webp)

> Делает текст нейросети живым, как будто писал человек. Заточен под русский, есть и английская версия.
> Makes AI text read like a human wrote it. Built for Russian, works for English too.

[🇷🇺 Русский](#-русский) · [🇬🇧 English](#-english)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg) ![Stars](https://img.shields.io/github/stars/thevseprod/humanizer-ru?style=flat&color=yellow) ![Install](https://img.shields.io/badge/install-npx%20skills%20add-black) ![Works in](https://img.shields.io/badge/works%20in-any%20AI%20agent-blue)

<a id="русский"></a>

## 🇷🇺 Русский

Почти все «хьюманайзеры» англоязычные и не ловят то, что выдаёт русскую нейросеть:
длинное тире «—», канцелярит, маркетинговые слова-пустышки. Этот ловит. И английский
набор правил тоже внутри.

Кода нет, ставить ничего не нужно: это markdown-файл с правилами, который ты
вставляешь в любую нейросеть. Плюс есть скилл, который ставится одной командой в
Claude Code, Cursor, Codex и другие агенты.

### Почему работает

Не просто меняет слова на синонимы. Он охотится за конкретными признаками машинного
текста и переписывает их: привычку к длинному тире, штампы-затычки («важно отметить»),
буллшит-лексикон, подобострастные концовки, безличный хедж без позиции, механическое
«правило тройки», стены текста и прочее. Потом проходит вторым проходом и проверяет
три вещи: что ещё пахнет ботом, не пропало ли по дороге что-то из фактов и не
превратился ли текст в обезличенный.

И знает, чего трогать нельзя. Повтор термина, длинная фраза, вводные слова автора,
его сомнения - это живая речь, а не следы нейросети. Если чистить нечего, текст
возвращается без правок.

### Пример

![До и после humanizer-ru - один смысл без «запаха нейросети»](assets/before-after.webp)

Слева типичный AI-текст со всеми признаками машины, справа - та же мысль после humanizer-ru: без штампов, канцелярита и длинного тире, зато с позицией и живым ритмом.

Если картинка не грузится, вот то же самое текстом:

| Было (нейросеть) | Стало |
|---|---|
| В современном мире важно отметить, что данный инструмент играет ключевую роль — он не просто ускоряет работу, он трансформирует подход. | Инструмент экономит мне часа три в неделю. Не «трансформирует подход», просто убирает рутину. |
| Стоит подчеркнуть, что подход имеет как преимущества, так и недостатки, всё зависит от ситуации. | Мне подход зашёл. Минус один: на длинных текстах он тупит. |
| Разберём по пунктам, почему падают охваты. Забегая вперёд: причина одна. | Охваты падают из-за одной вещи: алгоритм режет посты со ссылками. |

**Чем меряем.** Читателем, а не детектором. Проценты «AI detected» у разных сервисов разные и меняются каждый месяц, а подгонка под них ломает нормальный текст. Если человек читает и не спотыкается - задача выполнена.

### Быстрый старт

**Установить одной командой в любой AI-агент** (Claude Code, Cursor, Codex, Windsurf и другие) - через кросс-агентный установщик [skills](https://github.com/vercel-labs/skills):

```
npx skills add thevseprod/humanizer-ru
```

Во все агенты сразу: `npx skills add thevseprod/humanizer-ru --agent '*'`. Обновить потом: `npx skills update humanizer-ru`.

**Claude Code, как плагин:**

```
/plugin marketplace add thevseprod/humanizer-ru
/plugin install humanizer-ru@humanizer-ru
```

**Без установки, любая нейросеть (ChatGPT / Claude / Gemini / …):**

- **Одним файлом куда угодно** - скачай [`SKILL.md`](SKILL.md) и положи его в папку скиллов своего агента. Внутри уже оба набора правил, ничего больше не нужно.
- **Отдать файл агенту** - дай [`humanizer.ru.md`](humanizer.ru.md) своему AI (Cursor, кастомный GPT и т.п.), он сам прочитает правила.
- **Скопировать в чат** - открой [`humanizer.ru.md`](humanizer.ru.md) и вставь часть от `ЗАДАЧА` до конца первым сообщением.

Потом кинь текст, который надо оживить. Готово.

**Калибровка под себя (по желанию):** дай 1-2 примера своего текста, и модель
подстроится под твою манеру. Твои примеры остаются у тебя.

### Что внутри

| Файл | Что это |
|---|---|
| [`SKILL.md`](SKILL.md) | Скилл целиком в одном файле - можно просто скачать и положить куда угодно |
| [`humanizer.ru.md`](humanizer.ru.md) | Правила для **русского** текста |
| [`humanizer.en.md`](humanizer.en.md) | Правила для **английского** текста |
| `build_single.py` | Пересобирает `SKILL.md` из двух файлов правил |
| `LICENSE` | MIT |

### Версии

- **1.4.0** - инструмент научился не портить хороший текст. Новый раздел «Что НЕ дефект»: повтор термина, длинное предложение, вводные слова автора и его сомнения - это живая речь, а не следы нейросети. Нет находок - текст возвращается без правок. Синоним больше не считается лечением: «важно отметить» → «стоит подчеркнуть» это тот же штамп. Добавлены жанр (в инструкции сухость это норма, для договоров правила не применяются), чистка технического мусора после копирования из чата и режим проверки без переписывания.
- **1.3.0** - правила переставлены по силе: первым идёт то, что чаще всего выдаёт нейросеть в русском тексте. Новое требование к чистке: не терять утверждения - слова «первый», «единственный», «впервые» несут факт, а не пафос, и убирать их нельзя. Второй проход теперь проверяет и это.
- **1.2.0** - скилл собран в один файл: скачал `SKILL.md` и положил куда угодно, соседние файлы больше не нужны. Новое правило: анонс вместо содержания («погнали», «разберём по пунктам»). Приём структурный, поэтому не лечится сменой тона на разговорный.
- **1.1.0** - установка одной командой в любой агент, плагин для Claude Code, баннер и пример «до/после» в README.
- **1.0.0** - первый выпуск: правила для русского и английского, скилл с автоопределением языка.

### Автор

Пишу и показываю про VSЁ о нейросетях, ИИ-агентах и вайбкодинге – для облегчения
жизни и заработка:

- 📢 Telegram: [@buyonhigh](https://t.me/buyonhigh)
- ▶️ YouTube: [@thevseproduction](https://www.youtube.com/@thevseproduction)

---

<a id="english"></a>

## 🇬🇧 English

Most "humanize AI" tools are English-only and miss the tells that give away a
Russian-language LLM (the long em dash «—», officialese, marketing buzzwords). This
one catches them, and ships an English rule set too.

No code, nothing to install: it's a markdown instruction file you paste into any LLM.
There's also a skill that installs into Claude Code, Cursor, Codex and other agents
with one command.

### Why it works

It doesn't just swap synonyms. It hunts the specific patterns that mark machine
writing and rewrites them: the em-dash habit, stock filler ("it's worth noting"),
buzzword soup, servile closers, opinion-free hedging, the mechanical rule of three,
walls of text, and more. Then it runs a second pass that checks three things: what
still smells like an AI, whether any fact went missing along the way, and whether
the text lost the author's voice.

It also knows what to leave alone. A repeated term, a long sentence, the author's
asides and doubts are human writing, not machine tells. If there is nothing to
clean, the text comes back untouched.

### Example

**Before:** In today's fast-paced world, AI is a game-changer that unlocks unprecedented potential — it doesn't just automate tasks, it transforms everything.

**After:** AI already changed how a lot of work gets done. Not a "game-changer", just a tool that pays off once you learn where it fits.

What got cut: "in today's fast-paced world", "game-changer", "unlocks unprecedented potential", the "it doesn't just X, it Y" cadence, the em dash. What got added: a stance and a normal rhythm.

**What we measure by.** The reader, not a detector. "AI detected" percentages differ from service to service and change every month, and tuning a text to them breaks it. If a person reads it without stumbling, the job is done.

### Quick start

**Install into any AI agent with one command** (Claude Code, Cursor, Codex, Windsurf and more) - via the cross-agent [skills](https://github.com/vercel-labs/skills) installer:

```
npx skills add thevseprod/humanizer-ru
```

Into every agent at once: `npx skills add thevseprod/humanizer-ru --agent '*'`. Update later: `npx skills update humanizer-ru`.

**Claude Code, as a plugin:**

```
/plugin marketplace add thevseprod/humanizer-ru
/plugin install humanizer-ru@humanizer-ru
```

**No install, any LLM (ChatGPT / Claude / Gemini / …):**

- **Hand the file to your agent** - give [`humanizer.en.md`](humanizer.en.md) to your AI (Cursor, a custom GPT, etc.) and it reads the rules itself.
- **Copy into the chat** - open [`humanizer.en.md`](humanizer.en.md) and paste the part from `TASK` to the end as your first message.

Then send the text you want to humanize. Done.

**Optional voice calibration:** paste one or two samples of your own writing and the
model matches your style. Your samples stay with you.

### Versions

- **1.4.0** - the tool learned not to ruin good text. New section "What is NOT a defect": a repeated term, a long sentence, the author's asides and doubts are human writing, not machine tells. Nothing found - the text comes back untouched. A synonym no longer counts as a fix: "it's worth noting" → "it bears emphasis" is the same stock phrase. Added genre awareness (dryness is the norm in a spec; don't apply the rules to contracts), clean-up of technical debris left by copy-paste from a chat, and a check-only mode.
- **1.3.0** - rules reordered by strength: the most common tells come first. New constraint: do not lose claims - words like "first", "only", "record" carry a fact, not hype, and must survive the cleanup. The second pass now checks for it.
- **1.2.0** - the skill ships as a single file: download `SKILL.md`, drop it anywhere, no neighbouring files needed. New rule: announcing instead of saying ("let's dive in", "here's the thing"). It is structural, so switching to a casual tone does not remove it.
- **1.1.0** - one-command install into any agent, Claude Code plugin, banner and a before/after example in the README.
- **1.0.0** - first release: Russian and English rule sets, skill with language auto-detection.

### Author

I write and show everything about neural nets, AI agents and vibe-coding, to make life
and earning easier:

- 📢 Telegram: [@buyonhigh](https://t.me/buyonhigh)
- ▶️ YouTube: [@thevseproduction](https://www.youtube.com/@thevseproduction)

---

## License

MIT, see [`LICENSE`](LICENSE). Use it, fork it, ship it.
