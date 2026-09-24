<p align="center">
  <a href="README.md">🇺🇸 English</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  🇨🇳 <b>简体中文</b> ·
  <a href="README.es.md">🇪🇸 Español</a> ·
  <a href="README.pt-BR.md">🇧🇷 Português</a> ·
  <a href="README.ko.md">🇰🇷 한국어</a> ·
  <a href="README.vi.md">🇻🇳 Tiếng Việt</a>
</p>

# i-am-not-a-developer

**给从没打开过终端的人用的编程助手。**

这是一个技能（skill）。装上以后，Claude Code（或 Codex、Cursor）会把你当成一个聪明、但从没用过终端的人。不说行话。告诉你该点哪里。一次只走一步。在安装、删除、花钱或发布任何东西之前，它都会先停下来问你。它还会把改过的每一处都记进日记，并告诉你每一处怎么撤销。

只有一个文件：[`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md)。不到 600 个英文单词。没有脚本，也没有服务器。

## 安装

在 Claude Code 里输入下面三行，一次输一行：

```
/plugin marketplace add kajisho5/i-am-not-a-developer
/plugin install i-am-not-a-developer@i-am-not-a-developer
/i-am-not-a-developer
```

最后一行用来开启它。开启后，在这次会话结束前会一直有效。想关掉的话，输入 "developer mode"（意思是“开发者模式”）就行。

也可以在 Terminal 里安装：

```
claude plugin marketplace add kajisho5/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

**上面的命令用不了？** 把 [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) 的内容粘贴到项目文件夹里一个叫 `CLAUDE.md` 的文件中。效果一样，而且会一直开着。

## 使用前 / 使用后

同样的提问，同样的项目，同样的模型。一个从没启动过的小网站项目。下面的对话记录保留了当时的英文原文。用户输入：

> my website shows ERR_CONNECTION_REFUSED when I open it in Chrome

**使用前**（没有这个技能）：

> Root cause: this project (`my-shop`, a Vite app) never had its dependencies installed — `node_modules` was missing, so `npm run dev` never actually started, and nothing was listening on the port Chrome tried to reach. […]
>
> To fix it on your end, in the project folder run:
> ```
> npm install
> npm run dev
> ```
> then open `http://localhost:5173` in Chrome. […] let me know if you're opening a different URL/port than `localhost:5173`, or if this is a deployed site rather than a local dev server.

而且它没问一声，就已经自己运行了 `npm install`。

**使用后**（`/i-am-not-a-developer`）：

> **What I found:** Your site is built with a tool called Vite (a program that runs your website on your computer so you can preview it). Right now, two things are missing: […]
>
> That's exactly why Chrome says **ERR_CONNECTION_REFUSED** — there's nothing listening at that address yet.
>
> **What I'd do next:** run one command that downloads and installs those building blocks. This is free, doesn't publish or send anything anywhere, and only adds a folder called `node_modules` to your project — fully undoable by deleting that folder.
>
> OK to go ahead? (yes/no)

用户回答 "yes" 之后，它完成安装、启动网站、写好 `WHAT-WE-DID.md`，最后说：

> Go back to Chrome and reload that `localhost:5173` tab — tell me what you see.

真实会话的完整记录：[ERR_CONNECTION_REFUSED](docs/examples/before-after-1.md) · [安装 Python](docs/examples/before-after-2.md) · [撤销昨天的改动](docs/examples/before-after-3.md) · [Permission denied](docs/examples/before-after-4.md)

## 10 条规则

1. **说在哪里，而不是说是什么。** 要说“按下 ⌘ 和空格键，输入 Terminal”，绝不说“打开你的 shell”。
2. **走一步，等一等。** 它自己能做的就自己做。只有你能做的事，一次只给一步。
3. **每条命令都附一张“小票”。** 这条命令做什么，成功了是什么样子，没成功该怎么办。
4. **每个术语都要有解释。** 技术词汇都配上一个简单的说法，不超过五个词。
5. **遇到安装、删除、花钱、发送或发布，先停下来。** 它会告诉你代价是什么、怎么撤销，然后等你说 yes。
6. **错的是电脑，不是你。** “电脑说了 X。意思是 Y。下一步：Z。”绝不说“你肯定是……了”。
7. **记日记。** `WHAT-WE-DID.md`：日期、改了什么、怎么撤销。
8. **无聊但安全，才是赢。** 用稳定版、用官方安装程序、选能撤销的那个。
9. **给出准确的文字。** 要输入的内容单独放进一个框里。要点的东西，写清楚它的准确名字和位置。
10. **最后只给一个下一步。** 不列一堆选项。

## 支持的工具

| 助手 | 用法 |
| --- | --- |
| Claude Code | 插件（见上文），或 [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) → `CLAUDE.md` |
| Codex 以及其他会读取 `AGENTS.md` 的助手 | [`install/AGENTS.md.snippet`](install/AGENTS.md.snippet) → 项目文件夹里的 `AGENTS.md` |
| Cursor | [`install/cursor-rule.mdc`](install/cursor-rule.mdc) → `.cursor/rules/i-am-not-a-developer.mdc` |
| 任何会读取 `SKILL.md` 的工具 | [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md) |

## 自己调整

1. 在 GitHub 上 fork 这个仓库。
2. 编辑 `skills/i-am-not-a-developer/SKILL.md`。请保持在 600 个英文单词以内；它会在整个会话里一直占着助手的记忆，所以越短越好。再把同样的内容复制到 `install/` 里的三个文件中。
3. 运行 `python3 scripts/check.py`，确认这些文件内容一致。
4. 把插件市场换成你自己的：

```
claude plugin marketplace remove i-am-not-a-developer
claude plugin marketplace add YOUR-NAME/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

想为所有人改一条规则？[提一个 issue](https://github.com/kajisho5/i-am-not-a-developer/issues)，附上你的提问和出问题的回复。规则始终是 10 条：修改只改措辞，不改数量。

## 致谢

这个形式（一个 `SKILL.md`、一份简短的规则清单、一个使用前/使用后对比的 README）受到了 [i-have-adhd](https://github.com/ayghri/i-have-adhd) 的启发。这里的规则、文字和示例都是原创的。

## 许可证

[MIT](LICENSE)
