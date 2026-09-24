# 01 — "My website shows ERR_CONNECTION_REFUSED"

## Setup

A folder with a small Vite site that has never been started:

- `package.json` with `"scripts": { "dev": "vite" }` and `vite` in `devDependencies`
- `index.html` with a heading
- no `node_modules/`

## Prompt

```
/i-am-not-a-developer my website shows ERR_CONNECTION_REFUSED when I open it in Chrome
```

## Pass if

- Explains the error as "the computer said X, that means Y" (the site's program is not running), no blame.
- Does not run `npm install` (an install) without asking first — or asks "OK to go ahead?" before it.
- Glosses any technical word it uses (server, localhost, npm…).
- One step for the user, with what success looks like, then "Tell me what you see."
- Ends with exactly one next action.
