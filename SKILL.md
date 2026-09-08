---
name: humanizer-ru
version: 1.3.0
description: Rewrite text so it reads like a real person wrote it, not an AI. Auto-detects Russian vs English and applies the matching rule set. Use when the user asks to humanize text, remove the "AI smell", de-AI, or make AI output sound natural - especially for Russian.
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

---

# Правила для русского текста

## ЗАДАЧА

Перепиши присланный текст так, чтобы он читался как написанный живым человеком.
Сохрани смысл, факты и цифры. Не добавляй ничего от себя и не выдумывай данные.
Меняй ИМЕННО подачу: убирай признаки ИИ по правилам ниже.

**Чего нельзя терять.** Чистка не должна съедать утверждения. Особенно легко
теряются слова, которые кажутся «пафосом», а на деле несут факт: «первый»,
«единственный», «самый», «впервые», «рекордный», «только», «до сих пор»,
«одновременно». Убрать «первый в России сервис» до «сервис» - это уже не
оживление текста, а искажение. Если слово подтверждает факт - оставь его,
даже если звучит громко. Выбрасывай пустое усиление («по-настоящему»,
«поистине», «крайне важно»), а не само утверждение.

Работай в два прохода:
1. Перепиши текст по правилам.
2. Пройдись по результату ещё раз и спроси себя два вопроса: «что здесь всё ещё
   пахнет нейросетью?» - и дочисти; «не пропало ли по дороге чего-то из фактов,
   цифр и утверждений?» - и верни.

## Признаки ИИ, которые надо убрать

### 1. Типографика
- Длинное тире «—» - это главный маркер ИИ. Нейросети почти всегда ставят именно
  его, живой человек на клавиатуре - почти никогда. Замени на обычный дефис «-»,
  запятую или перестрой фразу.
- Никаких «!!!» подряд - максимум один «!».
- Эмодзи не в потоке текста и не в каждой строке. В меру и по делу.

### 2. Канцелярит и водяные штампы
Выкинь обороты, по которым сразу видно «писала машина»:
- «следует отметить», «важно понимать», «стоит подчеркнуть», «необходимо учитывать»
- «в современном мире», «в эпоху цифровизации», «в рамках данной статьи»
- «является важным аспектом», «играет ключевую роль»

Плохо: «Важно отметить, что данный инструмент играет ключевую роль…»
Живо: «Эта штука реально решает вот что:»

### 3. Анонс вместо содержания
ИИ объявляет, что сейчас скажет, вместо того чтобы просто сказать: «Погнали»,
«Разберём по пунктам», «Сразу к делу», «Что важно понимать», «Забегая вперёд»,
«Сейчас объясню на пальцах».

Это приём структурный, а не список слов, и в разговорной обёртке он выживает:
«короче, вот что меня подкосило, сейчас расскажу», «сразу предупрежу, тут есть
нюанс». Тон стал живее, анонс остался - значит и признак ИИ остался.

Лечится удалением, а не смягчением: выкинь фразу-анонс целиком и начни с самой
мысли. Заголовок и первая фраза и так скажут, о чём речь.

Плохо: «Разберём, почему падают охваты. Сразу скажу: причина одна.»
Живо: «Охваты падают из-за одной вещи: алгоритм режет посты со ссылками.»

### 4. Буллшит-лексикон
Слова-пустышки из маркетингового буллшита - под нож: «прорыв», «трансформация»,
«инсайт», «синергия», «экосистема» (без нужды), «успешный успех», «создавать
ценность», «масштабировать себя», «раскрыть потенциал».

### 5. Негативный параллелизм
Заезженная ИИ-риторика: «это не просто X, это Y», «не только…, но и…». Скажи
прямо: «это Y».

### 6. Механическое «правило тройки»
ИИ всё пихает в группы по три ради красоты: «быстро, надёжно и удобно». Если
пунктов реально два или четыре - пиши столько, сколько есть.

### 7. Псевдо-авторитетные подводки-пустышки
ИИ делает вид, что «прорезает шум», вводными ни о чём: «по сути», «на самом деле»,
«что действительно важно», «в основе своей», «как известно». Убери их и скажи мысль
прямо.

### 8. Подобострастные и дежурные концовки
Никаких «надеюсь, было полезно», «спасибо за внимание», «подводя итог».
И никакого пустого позитива в финале: «будущее за этим», «впереди интересные
времена», «время покажет». Заканчивай конкретикой или сильной короткой строкой,
а не вежливым поклоном.

### 9. Симметричный хедж (отсутствие позиции)
«С одной стороны… с другой стороны», «у каждого свой подход», «всё зависит от
ситуации» - так пишет ИИ, у которого нет мнения. Займи сторону и скажи прямо.
(Перечисление «во-первых… во-вторых…» - это нормально, оставляй.)

### 10. «Пустая уместность»
Каждый абзац должен добавлять новую мысль, факт или конкретику. Текст «по теме, но
ни о чём» и пересказ очевидного - типичный признак ИИ. Вырезай воду.

### 11. Жирный по-человечески
- Не выделяй жирным первое слово каждого пункта списка - это типичный ИИ-маркер
  (модель пытается «акцентировать хоть что-то» в каждой строке).
- Жирный - только на конкретный факт: цифру, дату, имя. Не на целые фразы и мысли.

### 12. Рваный человеческий ритм
- Короткие абзацы: 1-3 предложения, между ними пустая строка. Никаких стен текста.
- Не пиши предложения на четыре строки с пятью придаточными. Дроби.
- Варьируй длину фраз: подряд короткая - длинная - короткая читается живо.

### 13. Живой голос, а не безликое медиа
- Пиши от первого лица, со своим мнением. Не прячься за «эксперты считают»,
  «специалисты рекомендуют» - если есть позиция, говори «я считаю», «по моему опыту».
- Не сюсюкай и не смотри на читателя сверху. Общайся на равных.

### 14. Не выдумывай в пробелах
Нет данных - так и скажи. Не лепи догадки-затычки с хеджем («вероятно, около…»,
«точных цифр нет, но скорее всего…»). Лучше честное «не знаю», чем правдоподобная
выдумка.

## Приёмы живости (добавляй умеренно, не в каждый абзац)

- **Возражение читателя + ответ.** Вставь реплику от лица читателя и сразу ответь:
  «Скажешь: звучит сложно. На деле нет, потому что…». Меняй форму, не повторяй одну
  и ту же конструкцию из абзаца в абзац.
- **«Если коротко».** Сложный кусок закрывай одной строкой-выводом: «Если коротко -
  [одна фраза]».
- **Сильный финал.** Вместо плоского конца - острая, образная или ироничная
  последняя строка, которую захочется процитировать.
- **Прямое действие вместо риторики.** Не «представьте, что…», а «открой и проверь
  прямо сейчас: …».

## Золотое правило

Свежесть формулировок важнее «красоты». Если видишь, что повторяешь один и тот же
приём или слово - перепиши по-новому. Живой автор каждый раз говорит немного иначе;
ИИ выдаёт одинаковые шаблоны. Твоя цель - звучать как первый, а не как второй.

---

# Rules for English text

## TASK

Rewrite the supplied text so it reads as if written by a real human. Keep the
meaning, facts, and numbers. Do not add anything or invent data. Change only the
DELIVERY: remove the AI tells listed below.

**What you must not lose.** Cleaning must not eat claims. The words that go
missing most easily are the ones that look like hype but carry a fact: "first",
"only", "most", "record", "still", "at the same time". Cutting "the first service
in the country" down to "the service" is no longer polishing - it changes what
the text says. If a word backs a claim, keep it, however loud it sounds. Cut
empty intensifiers ("truly", "genuinely", "critically important"), not the claim.

Work in two passes:
1. Rewrite the text by the rules.
2. Re-read your result and ask two questions: "what here still smells like an
   AI?" - and clean it up; "did any fact, number or claim go missing on the
   way?" - and put it back.

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

### 3. Announcing instead of saying
The model announces what it is about to say instead of saying it: "let me walk
you through this", "first, some context", "a quick word before we start",
"what you should keep in mind here".

The tell is structural, not a phrase list, and it survives a casual reword:
"one thing that got me, so watch out for this part". The register changed, the
announcement stayed - so did the machine fingerprint.

Cut it, don't soften it: drop the announcing sentence and open with the point
itself. The heading already says what the paragraph is about.

Bad: "Let's break down why reach is falling. Right away: there is one reason."
Alive: "Reach is falling for one reason: the algorithm throttles posts with links."

### 4. Buzzword soup
Drop the empty hype vocabulary: "delve", "tapestry", "realm", "leverage" (as filler),
"unlock the potential", "game-changer", "revolutionary", "seamless", "robust
solution", "synergy".

### 5. Negative parallelism
The worn-out AI cadence: "It's not just X, it's Y", "Not only… but also…". Say it
straight: "It's Y".

### 6. Mechanical rule of three
AI crams everything into triples for a sense of completeness: "fast, reliable, and
easy". If there are really two or four points, write that many.

### 7. Hollow authority hedges
LLMs pretend to "cut through the noise" with throat-clearing: "Essentially", "At its
core", "The truth is", "What really matters is". Delete them and state the point.

### 8. Servile or boilerplate endings
No "I hope this helps!", "In conclusion", "To sum up", "Let me know if you have any
questions". And no empty-optimism closers: "The future looks bright", "Only time will
tell", "The possibilities are endless". End on something concrete or a sharp line.

### 9. Symmetric hedging (no stance)
"On one hand… on the other hand", "It depends", "There's no one-size-fits-all" - that's
an AI with no opinion. Take a side and say it. (A plain "first… second…" list is fine.)

### 10. "Empty relevance"
Every paragraph must add a new thought, fact, or specific. Text that's "on topic but
about nothing", and restating the obvious, is a classic AI signal. Cut the filler.

### 11. Bold like a human
- Don't bold the first word of every list item - that's a classic AI tell (the model
  tries to "emphasize something" on every line).
- Bold only a concrete fact: a number, a date, a name. Not whole phrases or ideas.

### 12. Human, uneven rhythm
- Short paragraphs: 1-3 sentences, blank line between them. No walls of text.
- Don't write four-line sentences with five subordinate clauses. Break them up.
- Vary sentence length: short - long - short reads alive.

### 13. A living voice, not faceless media
- Write in the first person, with an opinion. Don't hide behind "experts say",
  "studies suggest" - if you have a view, say "I think", "in my experience".
- Don't talk down to the reader and don't grovel. Talk as an equal.

### 14. Don't invent in the gaps
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
