<p align="center">
  <a href="README.md">🇺🇸 English</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.es.md">🇪🇸 Español</a> ·
  🇧🇷 <b>Português</b> ·
  <a href="README.ko.md">🇰🇷 한국어</a> ·
  <a href="README.vi.md">🇻🇳 Tiếng Việt</a>
</p>

# i-am-not-a-developer

**Seu assistente de programação, para quem nunca abriu um terminal.**

É uma skill (uma habilidade extra) que faz o Claude Code (ou o Codex, ou o Cursor) tratar você como uma pessoa inteligente que nunca usou um terminal. Sem jargão. Ele diz onde clicar. Um passo de cada vez. Ele para e pergunta antes de instalar, apagar, cobrar ou publicar qualquer coisa. E mantém um diário de tudo o que mudou, com um jeito de desfazer cada mudança.

Um arquivo só: [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md). Menos de 600 palavras. Sem scripts, sem servidores.

## Instalação

**Jeito mais fácil: copie esta frase, cole no Claude Code e aperte Enter.** O Claude faz a instalação para você. Se ele pedir permissão, diga que sim.

```
Instale este plugin para mim: rode "claude plugin marketplace add kajisho5/i-am-not-a-developer", depois "claude plugin install i-am-not-a-developer@i-am-not-a-developer", e me avise quando terminar.
```

Quando ele disser que terminou, feche o Claude Code, abra de novo e digite `/i-am-not-a-developer`. Ele fica ligado até o fim da sessão. Para desligar, diga "developer mode" (modo desenvolvedor).

**Não quer instalar nada?** Então comece a conversa com esta frase. Ela vale só para aquela conversa.

```
Durante toda esta conversa, siga as regras de https://raw.githubusercontent.com/kajisho5/i-am-not-a-developer/main/skills/i-am-not-a-developer/SKILL.md
```

Isso funciona no Claude Code. Outros apps de chat só conseguem usar se puderem abrir links. Se o seu não puder, abra o link você mesmo, copie todo o texto e cole no chat.

<details>
<summary>Tem familiaridade com comandos?</summary>

Dentro do Claude Code:

```
/plugin marketplace add kajisho5/i-am-not-a-developer
/plugin install i-am-not-a-developer@i-am-not-a-developer
/i-am-not-a-developer
```

Pelo Terminal:

```
claude plugin marketplace add kajisho5/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

Ou cole [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) em um arquivo chamado `CLAUDE.md` na pasta do seu projeto. Funciona do mesmo jeito, e fica sempre ligado.

</details>

## Antes / Depois

Mesmo pedido, mesmo projeto, mesmo modelo. Um pequeno projeto de site que nunca tinha sido iniciado. As conversas aparecem em inglês, do jeito que foram gravadas. O usuário digita:

> my website shows ERR_CONNECTION_REFUSED when I open it in Chrome

**Antes** (sem a skill):

> Root cause: this project (`my-shop`, a Vite app) never had its dependencies installed — `node_modules` was missing, so `npm run dev` never actually started, and nothing was listening on the port Chrome tried to reach. […]
>
> To fix it on your end, in the project folder run:
> ```
> npm install
> npm run dev
> ```
> then open `http://localhost:5173` in Chrome. […] let me know if you're opening a different URL/port than `localhost:5173`, or if this is a deployed site rather than a local dev server.

E ele já tinha rodado `npm install` sem perguntar.

**Depois** (`/i-am-not-a-developer`):

> **What I found:** Your site is built with a tool called Vite (a program that runs your website on your computer so you can preview it). Right now, two things are missing: […]
>
> That's exactly why Chrome says **ERR_CONNECTION_REFUSED** — there's nothing listening at that address yet.
>
> **What I'd do next:** run one command that downloads and installs those building blocks. This is free, doesn't publish or send anything anywhere, and only adds a folder called `node_modules` to your project — fully undoable by deleting that folder.
>
> OK to go ahead? (yes/no)

Depois do "yes", ele instala, inicia o site, escreve o `WHAT-WE-DID.md` e termina com:

> Go back to Chrome and reload that `localhost:5173` tab — tell me what you see.

Conversas completas de sessões reais: [ERR_CONNECTION_REFUSED](docs/examples/before-after-1.md) · [Instalar o Python](docs/examples/before-after-2.md) · [Desfazer o que foi feito ontem](docs/examples/before-after-3.md) · [Permission denied](docs/examples/before-after-4.md)

## As 10 regras

1. **Diga onde, não o quê.** "Aperte ⌘ e a barra de espaço, digite Terminal". Nunca "abra seu shell".
2. **Um passo, depois espera.** Ele faz sozinho o que dá. O que só você pode fazer vem um passo de cada vez.
3. **Todo comando vem com um recibo.** O que ele faz, como é quando dá certo, o que fazer se não der.
4. **Nenhuma palavra sem explicação.** Palavras técnicas ganham um significado simples em até cinco palavras.
5. **Pare antes de qualquer coisa que instale, apague, custe, envie ou publique.** Ele diz o custo e como desfazer, e espera o seu "sim".
6. **Quem errou foi o computador, não você.** "O computador disse X. Isso quer dizer Y. Próximo passo: Z." Nada de "você deve ter…".
7. **Mantenha o diário.** `WHAT-WE-DID.md`: data, o que mudou, como desfazer.
8. **Chato e seguro vence.** Versões estáveis, instaladores oficiais, a opção que dá para desfazer.
9. **Mostre o texto exato.** O que digitar vai sozinho em uma caixa. O que clicar vem com o nome exato e o lugar.
10. **Termine com exatamente uma próxima ação.** Nada de menu de opções.

## Funciona com

| Assistente | Como |
| --- | --- |
| Claude Code | Plugin (acima), ou [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) → `CLAUDE.md` |
| Codex e outros assistentes que leem `AGENTS.md` | [`install/AGENTS.md.snippet`](install/AGENTS.md.snippet) → `AGENTS.md` na pasta do seu projeto |
| Cursor | [`install/cursor-rule.mdc`](install/cursor-rule.mdc) → `.cursor/rules/i-am-not-a-developer.mdc` |
| Qualquer coisa que leia `SKILL.md` | [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md) |

## Ajuste do seu jeito

1. Faça um fork deste repositório no GitHub.
2. Edite `skills/i-am-not-a-developer/SKILL.md`. Mantenha abaixo de 600 palavras; ele fica na memória do assistente durante a sessão inteira, então quanto mais curto, melhor. Copie o mesmo texto para os três arquivos em `install/`.
3. Rode `python3 scripts/check.py` para confirmar que os arquivos estão sincronizados.
4. Troque o marketplace pelo seu:

```
claude plugin marketplace remove i-am-not-a-developer
claude plugin marketplace add YOUR-NAME/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

Quer mudar uma regra para todo mundo? [Abra uma issue](https://github.com/kajisho5/i-am-not-a-developer/issues) com o pedido e a resposta que deu errado. A lista continua com 10 regras: as correções mudam o texto, não a quantidade.

## Créditos

O formato (um `SKILL.md`, uma lista curta de regras, um README com Antes/Depois) foi inspirado em [i-have-adhd](https://github.com/ayghri/i-have-adhd). As regras, os textos e os exemplos daqui são originais.

## Licença

[MIT](LICENSE)
