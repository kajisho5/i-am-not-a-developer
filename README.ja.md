<p align="center">
  <a href="README.md">🇺🇸 English</a> ·
  🇯🇵 <b>日本語</b> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.es.md">🇪🇸 Español</a> ·
  <a href="README.pt-BR.md">🇧🇷 Português</a> ·
  <a href="README.ko.md">🇰🇷 한국어</a> ·
  <a href="README.vi.md">🇻🇳 Tiếng Việt</a>
</p>

# i-am-not-a-developer

**ターミナルを開いたことがない人のための、コーディングエージェント。**

Claude Code（Codex、Cursor でも）を「頭はいいけど、ターミナルは触ったことがない人」向けの話し方に切り替えるスキルです。専門用語を使わない。どこを押せばいいかを言う。1 手ずつ進める。インストール・削除・課金・公開の前には必ず止まって聞く。そして、変えたことと元に戻す方法を日記に残す。

中身は 1 ファイルだけ：[`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md)。600 語以内。スクリプトもサーバーもありません。

## インストール

**いちばん簡単な方法: 下の文をコピーして Claude Code に貼り付け、Enter を押すだけです。** 設定作業は Claude がやってくれます。途中で許可を求められたら「はい」と答えてください。

```
このプラグインを入れてください。"claude plugin marketplace add kajisho5/i-am-not-a-developer" を実行してから "claude plugin install i-am-not-a-developer@i-am-not-a-developer" を実行して、終わったら教えてください。
```

「終わりました」と返ってきたら、Claude Code をいったん閉じて開き直し、`/i-am-not-a-developer` と入力します。そのセッションの間はずっとオンです。やめたいときは "developer mode" と入力してください。

**何もインストールしたくない場合は**、会話の最初に下の文を送ってください。その会話の間だけ有効です。

```
この会話の間は https://raw.githubusercontent.com/kajisho5/i-am-not-a-developer/main/skills/i-am-not-a-developer/SKILL.md のルールに従ってください。
```

Claude Code では動作を確認済みです。ほかのチャットアプリで使えるのは、そのアプリがリンク先を読める場合だけです。読めない場合は、リンクを自分で開いて中の文章をすべてコピーし、チャットに貼り付けてください。

<details>
<summary>コマンドに慣れている方へ</summary>

Claude Code の中で:

```
/plugin marketplace add kajisho5/i-am-not-a-developer
/plugin install i-am-not-a-developer@i-am-not-a-developer
/i-am-not-a-developer
```

ターミナルから:

```
claude plugin marketplace add kajisho5/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

または、[`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) の中身を、プロジェクトのフォルダにある `CLAUDE.md` というファイルに貼り付けても同じように動きます（こちらは常にオン）。

</details>

## Before / After

同じ質問・同じプロジェクト・同じモデルで比べました。一度も起動したことがない小さな Web サイトのフォルダで、ユーザーがこう入力します（実際のやり取りなので英語のまま載せています）：

> my website shows ERR_CONNECTION_REFUSED when I open it in Chrome

**Before**（スキルなし）：

> Root cause: this project (`my-shop`, a Vite app) never had its dependencies installed — `node_modules` was missing, so `npm run dev` never actually started, and nothing was listening on the port Chrome tried to reach. […]
>
> To fix it on your end, in the project folder run:
> ```
> npm install
> npm run dev
> ```
> then open `http://localhost:5173` in Chrome. […] let me know if you're opening a different URL/port than `localhost:5173`, or if this is a deployed site rather than a local dev server.

しかもこの時点で、断りなく `npm install` を実行済みでした。

**After**（`/i-am-not-a-developer`）：

> **What I found:** Your site is built with a tool called Vite (a program that runs your website on your computer so you can preview it). Right now, two things are missing: […]
>
> That's exactly why Chrome says **ERR_CONNECTION_REFUSED** — there's nothing listening at that address yet.
>
> **What I'd do next:** run one command that downloads and installs those building blocks. This is free, doesn't publish or send anything anywhere, and only adds a folder called `node_modules` to your project — fully undoable by deleting that folder.
>
> OK to go ahead? (yes/no)

「yes」と答えると、インストールしてサイトを起動し、`WHAT-WE-DID.md` に記録してから、最後にこう締めます：

> Go back to Chrome and reload that `localhost:5173` tab — tell me what you see.

実際のセッションの全文：[ERR_CONNECTION_REFUSED](docs/examples/before-after-1.md) · [Python のインストール](docs/examples/before-after-2.md) · [昨日の変更を元に戻す](docs/examples/before-after-3.md) · [Permission denied](docs/examples/before-after-4.md)

## 10 のルール

1. **「何を」ではなく「どこを」。** 「⌘ とスペースを押して Terminal と入力」。「シェルを開いて」とは言わない。
2. **1 手ずつ、待つ。** 自分でできることは自分でやる。あなたにしかできないことは 1 手ずつ渡す。
3. **コマンドには必ず「説明書き」。** 何をするか、成功したらどう見えるか、違ったらどうするか。
4. **専門用語には必ず一言の説明。** 5 語以内のやさしい言い換えを添える。
5. **インストール・削除・課金・送信・公開の前に止まる。** 費用と戻し方を伝えて、「yes」を待つ。
6. **悪いのはパソコン、あなたじゃない。** 「パソコンは X と言っています。つまり Y です。次は Z」。「〜したはずです」とは言わない。
7. **日記をつける。** `WHAT-WE-DID.md` に、日付・何を変えたか・戻し方。
8. **地味で安全なほうを選ぶ。** 安定版、公式インストーラー、元に戻せるやり方。
9. **打つ文字はそのまま見せる。** 入力する文字は枠の中に単独で。押すボタンは正確なラベルと場所で。
10. **最後は「次にやること」を 1 つだけ。** 選択肢のメニューは出さない。

## 対応しているエージェント

| エージェント | 方法 |
| --- | --- |
| Claude Code | プラグイン（上記）、または [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) → `CLAUDE.md` |
| Codex など `AGENTS.md` を読むエージェント | [`install/AGENTS.md.snippet`](install/AGENTS.md.snippet) → プロジェクトのフォルダの `AGENTS.md` |
| Cursor | [`install/cursor-rule.mdc`](install/cursor-rule.mdc) → `.cursor/rules/i-am-not-a-developer.mdc` |
| `SKILL.md` を読めるもの全般 | [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md) |

## 自分好みに調整する

1. GitHub でこのリポジトリを fork します。
2. `skills/i-am-not-a-developer/SKILL.md` を編集します。600 語以内に収めてください（セッション中ずっとエージェントの記憶に載るので、短いほど効きます）。同じ本文を `install/` の 3 ファイルにもコピーします。
3. `python3 scripts/check.py` を実行して、ファイルがそろっているか確認します。
4. マーケットプレイスを自分のものに差し替えます：

```
claude plugin marketplace remove i-am-not-a-developer
claude plugin marketplace add YOUR-NAME/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

全員向けにルールを直してほしいときは、うまくいかなかった質問と返答を添えて [Issue を立ててください](https://github.com/kajisho5/i-am-not-a-developer/issues)。ルールは 10 個のまま増やしません。直すのは言い回しで、数ではありません。

## クレジット

形式（`SKILL.md` 1 枚、短いルール集、Before/After の README）は [i-have-adhd](https://github.com/ayghri/i-have-adhd) に着想を得ました。ルール・文章・例はすべてオリジナルです。

## ライセンス

[MIT](LICENSE)
