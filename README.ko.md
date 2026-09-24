<p align="center">
  <a href="README.md">🇺🇸 English</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.es.md">🇪🇸 Español</a> ·
  <a href="README.pt-BR.md">🇧🇷 Português</a> ·
  🇰🇷 <b>한국어</b> ·
  <a href="README.vi.md">🇻🇳 Tiếng Việt</a>
</p>

# i-am-not-a-developer

**터미널을 한 번도 열어 본 적 없는 사람을 위한 코딩 에이전트.**

Claude Code(또는 ChatGPT, Gemini, Grok, Codex, Cursor)가 여러분을 "똑똑하지만 터미널은 한 번도 써 본 적 없는 사람"으로 대하게 만드는 스킬입니다. 전문 용어는 쓰지 않습니다. 어디를 클릭해야 하는지 알려 줍니다. 한 번에 한 단계씩 진행합니다. 무언가를 설치하거나, 지우거나, 돈이 들거나, 공개하기 전에는 반드시 멈추고 물어봅니다. 그리고 바꾼 내용을 전부 일기처럼 기록하고, 하나하나 되돌리는 방법도 함께 남깁니다.

파일은 하나뿐입니다: [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md). 영어로 600단어도 안 됩니다. 스크립트도, 서버도 없습니다.

## 설치

**Gemini를 쓰시나요?** 이 링크만 열면 됩니다: [i-am-not-a-developer Gem](https://gemini.google.com/gem/1wcFBsbprLnB7L5PQyTjzC2d6tfXdzJFr?usp=sharing). 복사·붙여넣기도, 로그인도 필요 없습니다.

**가장 쉬운 방법: 아래 문장을 복사해서 Claude Code에 붙여 넣고 Enter를 누르세요.** 설치는 Claude가 대신 해 줍니다. 허락해 달라고 물어보면 "네"라고 답하세요.

```
이 플러그인을 설치해 줘: "claude plugin marketplace add kajisho5/i-am-not-a-developer"를 실행하고, 그다음 "claude plugin install i-am-not-a-developer@i-am-not-a-developer"를 실행한 뒤, 다 끝나면 알려 줘.
```

다 끝났다고 하면 Claude Code를 닫았다가 다시 열고, `/i-am-not-a-developer`를 입력하세요. 켜진 상태는 세션이 끝날 때까지 유지됩니다. 끄고 싶으면 "developer mode"(개발자 모드)라고 말하면 됩니다.

**아무것도 설치하고 싶지 않나요?** 그럼 대화를 이 문장으로 시작하세요. 그 대화에서만 적용됩니다.

```
이 대화 내내 다음 링크에 있는 규칙을 따라 줘: https://raw.githubusercontent.com/kajisho5/i-am-not-a-developer/main/skills/i-am-not-a-developer/SKILL.md
```

이 방법은 Claude Code에서 작동합니다. 다른 채팅 앱은 링크를 열 수 있을 때만 쓸 수 있습니다. 쓰는 앱이 링크를 못 연다면, 직접 링크를 열어 글 전체를 복사한 뒤 채팅에 붙여 넣으세요.

<details>
<summary>명령어가 익숙하신가요?</summary>

Claude Code 안에서:

```
/plugin marketplace add kajisho5/i-am-not-a-developer
/plugin install i-am-not-a-developer@i-am-not-a-developer
/i-am-not-a-developer
```

Terminal에서:

```
claude plugin marketplace add kajisho5/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

또는 [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet)의 내용을 프로젝트 폴더 안의 `CLAUDE.md`라는 파일에 붙여 넣으세요. 똑같이 작동하고, 항상 켜져 있습니다.

</details>

## 사용 전 / 사용 후

같은 요청, 같은 프로젝트, 같은 모델입니다. 한 번도 실행된 적 없는 작은 웹사이트 프로젝트입니다. 대화 내용은 기록된 그대로 영어로 보여 드립니다. 사용자가 이렇게 입력합니다:

> my website shows ERR_CONNECTION_REFUSED when I open it in Chrome

**사용 전** (스킬 없음):

> Root cause: this project (`my-shop`, a Vite app) never had its dependencies installed — `node_modules` was missing, so `npm run dev` never actually started, and nothing was listening on the port Chrome tried to reach. […]
>
> To fix it on your end, in the project folder run:
> ```
> npm install
> npm run dev
> ```
> then open `http://localhost:5173` in Chrome. […] let me know if you're opening a different URL/port than `localhost:5173`, or if this is a deployed site rather than a local dev server.

게다가 묻지도 않고 이미 `npm install`을 실행해 버렸습니다.

**사용 후** (`/i-am-not-a-developer`):

> **What I found:** Your site is built with a tool called Vite (a program that runs your website on your computer so you can preview it). Right now, two things are missing: […]
>
> That's exactly why Chrome says **ERR_CONNECTION_REFUSED** — there's nothing listening at that address yet.
>
> **What I'd do next:** run one command that downloads and installs those building blocks. This is free, doesn't publish or send anything anywhere, and only adds a folder called `node_modules` to your project — fully undoable by deleting that folder.
>
> OK to go ahead? (yes/no)

"yes"라고 답하면 설치하고, 사이트를 실행하고, `WHAT-WE-DID.md`를 작성한 뒤 이렇게 마무리합니다:

> Go back to Chrome and reload that `localhost:5173` tab — tell me what you see.

실제 세션의 전체 대화: [ERR_CONNECTION_REFUSED](docs/examples/before-after-1.md) · [Python 설치하기](docs/examples/before-after-2.md) · [어제 한 일 되돌리기](docs/examples/before-after-3.md) · [Permission denied](docs/examples/before-after-4.md)

## 10가지 규칙

1. **무엇이 아니라 어디를 말한다.** "⌘ 키와 스페이스 바를 누르고 Terminal이라고 입력하세요"처럼 말합니다. "셸을 여세요"라고는 절대 말하지 않습니다.
2. **한 단계, 그리고 기다리기.** 에이전트가 직접 할 수 있는 일은 직접 합니다. 여러분만 할 수 있는 일은 한 번에 한 단계씩 안내합니다.
3. **모든 명령에는 영수증이 붙는다.** 무엇을 하는지, 성공하면 어떻게 보이는지, 실패하면 어떻게 해야 하는지.
4. **설명 없는 단어는 없다.** 기술 용어에는 다섯 단어 이내의 쉬운 뜻을 붙입니다.
5. **설치, 삭제, 비용, 전송, 공개 전에는 멈춘다.** 비용과 되돌리는 방법을 알려 주고, "예"라고 할 때까지 기다립니다.
6. **틀린 건 사용자가 아니라 컴퓨터다.** "컴퓨터가 X라고 했습니다. 이건 Y라는 뜻입니다. 다음: Z." "분명 뭔가 잘못 하셨을…" 같은 말은 하지 않습니다.
7. **일기를 쓴다.** `WHAT-WE-DID.md`: 날짜, 바뀐 것, 되돌리는 방법.
8. **지루하고 안전한 게 이긴다.** 안정 버전, 공식 설치 프로그램, 되돌릴 수 있는 선택지.
9. **정확한 텍스트를 보여 준다.** 입력할 내용은 상자 안에 따로 넣습니다. 클릭할 곳은 정확한 이름과 위치를 알려 줍니다.
10. **다음 행동 딱 하나로 끝낸다.** 선택지를 늘어놓지 않습니다.

## 지원 도구

### ChatGPT, Gemini, Grok (채팅 앱)

**Gemini를 쓰시나요?** 이 링크만 열면 됩니다: [i-am-not-a-developer Gem](https://gemini.google.com/gem/1wcFBsbprLnB7L5PQyTjzC2d6tfXdzJFr?usp=sharing). 복사·붙여넣기도, 로그인도 필요 없습니다.

**1. 아래 글을 복사하세요.** GitHub에서는 상자 오른쪽 위에 복사 버튼이 있습니다. (1,309자, 아래 앱 모두에 들어갑니다. 같은 글: [`install/short.txt`](install/short.txt).) 글은 영어지만, 에이전트는 여러분의 언어로 답합니다.

```text
I am not a developer. I'm smart, but I have never used a terminal. Follow these rules in every reply, in my language, until I say "developer mode".
1. Say where, not what: app → menu → button. Never "open your shell" or "edit the config".
2. One step at a time. Do what you can yourself. Give me one step (plus how to get there), ask what I see, and stop.
3. Before a command, say what it does. After it, say what success looks like and what to paste back if it looks different.
4. Explain each technical word in five words or fewer, or avoid it.
5. Before anything that installs, deletes, costs money, sends, publishes or touches passwords: say what changes, the cost, the risk and how to undo it, then wait for my yes. No sudo or curl | bash without a reason.
6. Errors: "The computer said X. That means Y. Next: Z." If you haven't seen the error, ask me to paste it and nothing else. Never blame me.
7. Keep a diary (WHAT-WE-DID.md, or a list in this chat): date, what changed, how to undo it. Read it before any undo and ask first.
8. Pick the stable, official, free option that can be undone. Don't offer alternatives.
9. Put anything I type alone in a code box. For clicks, give the exact button label and where it is.
10. End every reply with exactly one next action. Never ask more than one question.
```

**2. 여기에 붙여 넣으세요:**

| 앱 | 붙여 넣을 곳 | 글자 수 제한 |
| --- | --- | --- |
| ChatGPT | **Settings** → **Personalization** → **Custom instructions**에서, 어떻게 답해야 하는지 적는 칸 | 1,500자(무료), 5,000자(유료) |
| Gemini | **Explore Gems** → **New Gem** → **Instructions** → **Save**. 그다음 그 Gem과 대화하세요 | 길어도 괜찮습니다 |
| Grok | **Settings** → **Customize** → "how should Grok respond" 칸 | 4,000자 |

메뉴 이름은 2026년 9월 기준이며, 앱에서 자주 바뀝니다. 앱에서는 메뉴 이름이 한국어로 보일 수 있습니다. 그다음부터는 새 대화마다 이 규칙을 따릅니다(Gemini에서는 그 Gem과의 대화마다).

이 앱들은 여러분의 컴퓨터를 직접 만질 수 없습니다. 그래서 대신 해 주지 않고, 한 번에 한 단계씩 알려 줍니다.

### 코딩 에이전트

| 에이전트 | 방법 |
| --- | --- |
| Claude Code | 플러그인(위 참고), 또는 [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) → `CLAUDE.md` |
| Codex 및 `AGENTS.md`를 읽는 다른 에이전트 | [`install/AGENTS.md.snippet`](install/AGENTS.md.snippet) → 프로젝트 폴더의 `AGENTS.md` |
| Gemini CLI | [`install/GEMINI.md.snippet`](install/GEMINI.md.snippet) → 프로젝트 폴더의 `GEMINI.md` |
| Cursor | [`install/cursor-rule.mdc`](install/cursor-rule.mdc) → `.cursor/rules/i-am-not-a-developer.mdc` |
| `SKILL.md`를 읽는 모든 도구 | [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md) |

## 내 입맛대로 고치기

1. GitHub에서 이 저장소를 fork 하세요.
2. `skills/i-am-not-a-developer/SKILL.md`를 수정하세요. 600단어 이내로 유지하세요. 세션 내내 에이전트의 기억 속에 들어 있으니 짧을수록 좋습니다. 같은 내용을 `install/` 안의 세 파일에도 복사하세요.
3. `python3 scripts/check.py`를 실행해서 파일들이 서로 맞는지 확인하세요.
4. 마켓플레이스를 여러분의 것으로 바꾸세요:

```
claude plugin marketplace remove i-am-not-a-developer
claude plugin marketplace add YOUR-NAME/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

모두를 위해 규칙을 바꾸고 싶으신가요? 요청 내용과 잘못된 답변을 담아 [issue를 열어 주세요](https://github.com/kajisho5/i-am-not-a-developer/issues). 규칙은 계속 10개입니다. 수정은 표현을 바꿀 뿐, 개수는 바꾸지 않습니다.

## 크레딧

이 형식(`SKILL.md` 하나, 짧은 규칙 목록, 사용 전/사용 후를 보여 주는 README)은 [i-have-adhd](https://github.com/ayghri/i-have-adhd)에서 영감을 받았습니다. 여기 있는 규칙, 글, 예시는 모두 새로 쓴 것입니다.

## 라이선스

[MIT](LICENSE)
