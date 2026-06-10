# humanizer-ru

> Делает текст нейросети живым, как будто писал человек. Заточен под русский, есть и английская версия.
> Makes AI text read like a human wrote it. Built for Russian, works for English too.

[🇷🇺 Русский](#-русский) · [🇬🇧 English](#-english)

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

<a id="русский"></a>

## 🇷🇺 Русский

Почти все «хьюманайзеры» англоязычные и не ловят то, что выдаёт русскую нейросеть:
длинное тире «—», канцелярит, маркетинговые слова-пустышки. Этот ловит. И английский
набор правил тоже внутри.

Кода нет, ставить ничего не нужно: это markdown-файл с правилами, который ты
вставляешь в любую нейросеть. Плюс есть скилл для Claude Code в одно касание.

### Почему работает

Не просто меняет слова на синонимы. Он охотится за конкретными признаками машинного
текста и переписывает их: привычку к длинному тире, штампы-затычки («важно отметить»),
буллшит-лексикон, подобострастные концовки, безличный хедж без позиции, механическое
«правило тройки», стены текста и прочее. Потом проходит вторым проходом: «что тут всё
ещё пахнет ботом?».

### Пример

**До:** В современном мире нейросети играют ключевую роль в трансформации бизнеса — это не просто инструмент, это настоящий прорыв.

**После:** Нейронки уже переписывают то, как работает бизнес. Не «прорыв десятилетия» - просто рабочий инструмент, если знаешь, куда приткнуть.

Что ушло: «в современном мире», «играют ключевую роль», «настоящий прорыв», длинное тире, оборот «это не просто X, это Y». Что появилось: позиция и живой ритм.

### Быстрый старт

**Любая нейросеть (ChatGPT / Claude / Gemini / …):** два способа, как удобнее.

- **Отдать файл агенту** - просто дай [`humanizer.ru.md`](humanizer.ru.md) своему AI-агенту (Claude Code, Cursor, кастомный GPT и т.п.), он сам прочитает правила.
- **Скопировать в чат** - открой [`humanizer.ru.md`](humanizer.ru.md) и вставь часть от `ЗАДАЧА` до конца первым сообщением.

Потом кинь текст, который надо оживить. Готово.

**Claude Code (скилл):**
```
git clone https://github.com/thevseprod/humanizer-ru ~/.claude/skills/humanizer-ru
```
Потом зови `/humanizer` с текстом. *(Упаковку скилла добавлю в первом релизе.)*

**Калибровка под себя (по желанию):** дай 1-2 примера своего текста, и модель
подстроится под твою манеру. Твои примеры остаются у тебя.

### Что внутри

| Файл | Что это |
|---|---|
| [`SKILL.md`](SKILL.md) | Скилл для Claude Code |
| [`humanizer.ru.md`](humanizer.ru.md) | Правила для **русского** текста |
| [`humanizer.en.md`](humanizer.en.md) | Правила для **английского** текста |
| `LICENSE` | MIT |

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
There's also a Claude Code skill for one-tap use.

### Why it works

It doesn't just swap synonyms. It hunts the specific patterns that mark machine
writing and rewrites them: the em-dash habit, stock filler ("it's worth noting"),
buzzword soup, servile closers, opinion-free hedging, the mechanical rule of three,
walls of text, and more. Then it runs a second "what still smells like an AI?" pass.

### Example

**Before:** In today's fast-paced world, AI is a game-changer that unlocks unprecedented potential — it doesn't just automate tasks, it transforms everything.

**After:** AI already changed how a lot of work gets done. Not a "game-changer", just a tool that pays off once you learn where it fits.

What got cut: "in today's fast-paced world", "game-changer", "unlocks unprecedented potential", the "it doesn't just X, it Y" cadence, the em dash. What got added: a stance and a normal rhythm.

### Quick start

**Any LLM (ChatGPT / Claude / Gemini / …):** two ways, whichever is easier.

- **Hand the file to your agent** - give [`humanizer.en.md`](humanizer.en.md) to your AI agent (Claude Code, Cursor, a custom GPT, etc.) and it reads the rules itself.
- **Copy into the chat** - open [`humanizer.en.md`](humanizer.en.md) and paste the part from `TASK` to the end as your first message.

Then send the text you want to humanize. Done.

**Claude Code (skill):**
```
git clone https://github.com/thevseprod/humanizer-ru ~/.claude/skills/humanizer-ru
```
Then call `/humanizer` with your text. *(Skill packaging coming in the first release.)*

**Optional voice calibration:** paste one or two samples of your own writing and the
model matches your style. Your samples stay with you.

### Author

I write and show everything about neural nets, AI agents and vibe-coding, to make life
and earning easier:

- 📢 Telegram: [@buyonhigh](https://t.me/buyonhigh)
- ▶️ YouTube: [@thevseproduction](https://www.youtube.com/@thevseproduction)

---

## License

MIT, see [`LICENSE`](LICENSE). Use it, fork it, ship it.
