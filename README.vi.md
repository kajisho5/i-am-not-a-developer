<p align="center">
  <a href="README.md">🇺🇸 English</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.es.md">🇪🇸 Español</a> ·
  <a href="README.pt-BR.md">🇧🇷 Português</a> ·
  <a href="README.ko.md">🇰🇷 한국어</a> ·
  🇻🇳 <b>Tiếng Việt</b>
</p>

# i-am-not-a-developer

**Trợ lý lập trình dành cho người chưa từng mở terminal.**

Đây là một skill (kỹ năng bổ sung) giúp Claude Code (hoặc ChatGPT, Gemini, Grok, Codex, Cursor) đối xử với bạn như một người thông minh nhưng chưa từng dùng terminal. Không thuật ngữ khó hiểu. Nó chỉ cho bạn bấm vào đâu. Mỗi lần một bước. Nó sẽ dừng lại và hỏi bạn trước khi cài đặt, xóa, tính phí hay công khai bất cứ thứ gì. Nó còn ghi nhật ký mọi thay đổi, kèm cách hoàn tác từng thay đổi.

Chỉ một tệp: [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md). Chưa đến 600 từ. Không script, không máy chủ.

## Cài đặt

**Dùng Gemini?** Chỉ cần mở liên kết này: [Gem i-am-not-a-developer](https://gemini.google.com/gem/1wcFBsbprLnB7L5PQyTjzC2d6tfXdzJFr?usp=sharing). Không cần sao chép, không cần đăng nhập.

**Cách dễ nhất: sao chép câu dưới đây, dán vào Claude Code rồi nhấn Enter.** Claude sẽ cài đặt giúp bạn. Nếu nó xin phép, cứ đồng ý.

```
Hãy cài plugin này giúp tôi: chạy "claude plugin marketplace add kajisho5/i-am-not-a-developer", sau đó chạy "claude plugin install i-am-not-a-developer@i-am-not-a-developer", rồi báo tôi khi xong.
```

Khi nó báo đã xong, hãy đóng Claude Code, mở lại, rồi gõ `/i-am-not-a-developer`. Nó sẽ bật suốt phần còn lại của phiên làm việc. Muốn tắt, hãy nói "developer mode" (chế độ lập trình viên).

**Không muốn cài gì cả?** Vậy hãy bắt đầu cuộc trò chuyện bằng câu này. Nó chỉ có hiệu lực trong cuộc trò chuyện đó.

```
Trong suốt cuộc trò chuyện này, hãy làm theo các quy tắc tại https://raw.githubusercontent.com/kajisho5/i-am-not-a-developer/main/skills/i-am-not-a-developer/SKILL.md
```

Cách này dùng được trong Claude Code. Các ứng dụng chat khác chỉ dùng được nếu chúng mở được đường link. Nếu ứng dụng của bạn không mở được, hãy tự mở link, sao chép toàn bộ nội dung rồi dán vào khung chat.

<details>
<summary>Bạn quen dùng lệnh?</summary>

Trong Claude Code:

```
/plugin marketplace add kajisho5/i-am-not-a-developer
/plugin install i-am-not-a-developer@i-am-not-a-developer
/i-am-not-a-developer
```

Từ Terminal:

```
claude plugin marketplace add kajisho5/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

Hoặc dán [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) vào một tệp tên là `CLAUDE.md` trong thư mục dự án của bạn. Cách này hoạt động y như vậy, và luôn được bật.

</details>

## Trước / Sau

Cùng một yêu cầu, cùng một dự án, cùng một mô hình. Một dự án website nhỏ chưa từng được khởi chạy. Các đoạn hội thoại được giữ nguyên bằng tiếng Anh như lúc ghi lại. Người dùng gõ:

> my website shows ERR_CONNECTION_REFUSED when I open it in Chrome

**Trước** (không có skill):

> Root cause: this project (`my-shop`, a Vite app) never had its dependencies installed — `node_modules` was missing, so `npm run dev` never actually started, and nothing was listening on the port Chrome tried to reach. […]
>
> To fix it on your end, in the project folder run:
> ```
> npm install
> npm run dev
> ```
> then open `http://localhost:5173` in Chrome. […] let me know if you're opening a different URL/port than `localhost:5173`, or if this is a deployed site rather than a local dev server.

Mà nó đã tự chạy `npm install` từ trước, không hề hỏi.

**Sau** (`/i-am-not-a-developer`):

> **What I found:** Your site is built with a tool called Vite (a program that runs your website on your computer so you can preview it). Right now, two things are missing: […]
>
> That's exactly why Chrome says **ERR_CONNECTION_REFUSED** — there's nothing listening at that address yet.
>
> **What I'd do next:** run one command that downloads and installs those building blocks. This is free, doesn't publish or send anything anywhere, and only adds a folder called `node_modules` to your project — fully undoable by deleting that folder.
>
> OK to go ahead? (yes/no)

Sau khi người dùng trả lời "yes", nó cài đặt, khởi chạy trang web, viết `WHAT-WE-DID.md`, rồi kết thúc bằng:

> Go back to Chrome and reload that `localhost:5173` tab — tell me what you see.

Bản ghi đầy đủ từ các phiên thật: [ERR_CONNECTION_REFUSED](docs/examples/before-after-1.md) · [Cài Python](docs/examples/before-after-2.md) · [Hoàn tác việc hôm qua](docs/examples/before-after-3.md) · [Permission denied](docs/examples/before-after-4.md)

## 10 quy tắc

1. **Nói ở đâu, đừng nói là gì.** "Nhấn ⌘ và phím cách, gõ Terminal", chứ không bao giờ nói "mở shell của bạn".
2. **Một bước, rồi chờ.** Việc gì tự làm được thì nó tự làm. Việc chỉ bạn làm được thì nó hướng dẫn từng bước một.
3. **Mỗi lệnh đều kèm "hóa đơn".** Lệnh đó làm gì, thành công thì trông ra sao, không thành công thì làm gì.
4. **Không có từ nào thiếu lời giải thích.** Từ chuyên môn luôn đi kèm nghĩa đơn giản, không quá năm từ.
5. **Dừng lại trước mọi việc cài đặt, xóa, tốn tiền, gửi đi hay công khai.** Nó cho bạn biết chi phí và cách hoàn tác, rồi chờ bạn đồng ý.
6. **Máy tính sai, không phải người dùng.** "Máy tính báo X. Nghĩa là Y. Tiếp theo: Z." Không bao giờ nói "chắc bạn đã…".
7. **Ghi nhật ký.** `WHAT-WE-DID.md`: ngày, thay đổi gì, cách hoàn tác.
8. **Nhàm chán mà an toàn là thắng.** Phiên bản ổn định, trình cài đặt chính thức, lựa chọn có thể hoàn tác.
9. **Đưa ra đúng từng chữ.** Thứ cần gõ được đặt riêng trong một khung. Thứ cần bấm được ghi đúng tên và đúng vị trí.
10. **Kết thúc bằng đúng một việc tiếp theo.** Không đưa ra cả danh sách lựa chọn.

## Dùng được với

### ChatGPT, Gemini, Grok (ứng dụng trò chuyện)

**Dùng Gemini?** Chỉ cần mở liên kết này: [Gem i-am-not-a-developer](https://gemini.google.com/gem/1wcFBsbprLnB7L5PQyTjzC2d6tfXdzJFr?usp=sharing). Không cần sao chép, không cần đăng nhập.

**1. Sao chép đoạn văn bản này.** Trên GitHub, nút sao chép nằm ở góc trên bên phải của khung. (1,309 ký tự, vừa với mọi ứng dụng bên dưới. Cùng nội dung: [`install/short.txt`](install/short.txt).) Văn bản bằng tiếng Anh, nhưng trợ lý sẽ trả lời bằng ngôn ngữ của bạn.

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

**2. Dán vào đây:**

| Ứng dụng | Dán vào đâu | Giới hạn |
| --- | --- | --- |
| ChatGPT | **Settings** → **Personalization** → **Custom instructions**, vào ô về cách nó nên trả lời | 1,500 ký tự (miễn phí), 5,000 (trả phí) |
| Gemini | **Explore Gems** → **New Gem** → **Instructions** → **Save**. Sau đó trò chuyện với Gem đó | Văn bản dài cũng không sao |
| Grok | **Settings** → **Customize** → ô "how should Grok respond" | 4,000 ký tự |

Tên menu tính đến tháng 9 năm 2026; các ứng dụng hay đổi tên. Trong ứng dụng, tên menu có thể hiện bằng tiếng Việt. Từ đó trở đi, mọi cuộc trò chuyện mới đều theo các quy tắc này (trong Gemini là mọi cuộc trò chuyện với Gem đó).

Các ứng dụng này không thể đụng vào máy tính của bạn. Vì vậy trợ lý sẽ chỉ bạn từng bước một, thay vì tự làm.

### Trợ lý lập trình

| Trợ lý | Cách dùng |
| --- | --- |
| Claude Code | Plugin (ở trên), hoặc [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) → `CLAUDE.md` |
| Codex và các trợ lý khác có đọc `AGENTS.md` | [`install/AGENTS.md.snippet`](install/AGENTS.md.snippet) → `AGENTS.md` trong thư mục dự án của bạn |
| Gemini CLI | [`install/GEMINI.md.snippet`](install/GEMINI.md.snippet) → `GEMINI.md` trong thư mục dự án của bạn |
| Cursor | [`install/cursor-rule.mdc`](install/cursor-rule.mdc) → `.cursor/rules/i-am-not-a-developer.mdc` |
| Bất cứ công cụ nào đọc `SKILL.md` | [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md) |

## Tùy chỉnh

1. Fork repo này trên GitHub.
2. Sửa `skills/i-am-not-a-developer/SKILL.md`. Giữ dưới 600 từ; nó nằm trong bộ nhớ của trợ lý suốt cả phiên, nên càng ngắn càng tốt. Chép cùng nội dung đó vào ba tệp trong `install/`.
3. Chạy `python3 scripts/check.py` để kiểm tra các tệp đã khớp nhau chưa.
4. Đổi marketplace thành của bạn:

```
claude plugin marketplace remove i-am-not-a-developer
claude plugin marketplace add YOUR-NAME/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

Muốn đổi một quy tắc cho mọi người? [Mở một issue](https://github.com/kajisho5/i-am-not-a-developer/issues), kèm yêu cầu của bạn và câu trả lời bị sai. Danh sách luôn giữ 10 quy tắc: sửa lỗi là sửa câu chữ, không thay đổi số lượng.

## Ghi công

Hình thức này (một tệp `SKILL.md`, một danh sách quy tắc ngắn, một README có phần Trước/Sau) lấy cảm hứng từ [i-have-adhd](https://github.com/ayghri/i-have-adhd). Các quy tắc, nội dung và ví dụ ở đây đều là bản gốc.

## Giấy phép

[MIT](LICENSE)
