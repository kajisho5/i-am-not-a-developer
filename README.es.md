<p align="center">
  <a href="README.md">🇺🇸 English</a> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  🇪🇸 <b>Español</b> ·
  <a href="README.pt-BR.md">🇧🇷 Português</a> ·
  <a href="README.ko.md">🇰🇷 한국어</a> ·
  <a href="README.vi.md">🇻🇳 Tiếng Việt</a>
</p>

# i-am-not-a-developer

**Tu asistente de programación, para gente que nunca ha abierto una terminal.**

Es una skill (una habilidad extra) que hace que Claude Code (o Codex, o Cursor) te trate como una persona inteligente que nunca ha usado una terminal. Sin jerga. Te dice dónde hacer clic. Un paso a la vez. Se detiene y te pregunta antes de instalar, borrar, cobrar o publicar cualquier cosa. Y lleva un diario de todo lo que cambió, con una forma de deshacer cada cambio.

Un solo archivo: [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md). Menos de 600 palabras. Sin scripts, sin servidores.

## Instalación

Escribe estas tres líneas en Claude Code, una por una:

```
/plugin marketplace add kajisho5/i-am-not-a-developer
/plugin install i-am-not-a-developer@i-am-not-a-developer
/i-am-not-a-developer
```

La última línea lo activa. Queda activo durante el resto de la sesión. Para apagarlo, escribe "developer mode" (modo desarrollador).

O, si prefieres, desde la Terminal:

```
claude plugin marketplace add kajisho5/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

**¿No puedes ejecutar eso?** Pega [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) en un archivo llamado `CLAUDE.md` dentro de la carpeta de tu proyecto. Funciona igual, y siempre está activo.

## Antes / Después

Mismo mensaje, mismo proyecto, mismo modelo. Un pequeño proyecto de sitio web que nunca se había puesto en marcha. Las conversaciones se muestran en inglés, tal como se grabaron. El usuario escribe:

> my website shows ERR_CONNECTION_REFUSED when I open it in Chrome

**Antes** (sin la skill):

> Root cause: this project (`my-shop`, a Vite app) never had its dependencies installed — `node_modules` was missing, so `npm run dev` never actually started, and nothing was listening on the port Chrome tried to reach. […]
>
> To fix it on your end, in the project folder run:
> ```
> npm install
> npm run dev
> ```
> then open `http://localhost:5173` in Chrome. […] let me know if you're opening a different URL/port than `localhost:5173`, or if this is a deployed site rather than a local dev server.

Y ya había ejecutado `npm install` sin preguntar.

**Después** (`/i-am-not-a-developer`):

> **What I found:** Your site is built with a tool called Vite (a program that runs your website on your computer so you can preview it). Right now, two things are missing: […]
>
> That's exactly why Chrome says **ERR_CONNECTION_REFUSED** — there's nothing listening at that address yet.
>
> **What I'd do next:** run one command that downloads and installs those building blocks. This is free, doesn't publish or send anything anywhere, and only adds a folder called `node_modules` to your project — fully undoable by deleting that folder.
>
> OK to go ahead? (yes/no)

Después del "yes", instala todo, pone en marcha el sitio, escribe `WHAT-WE-DID.md` y termina con:

> Go back to Chrome and reload that `localhost:5173` tab — tell me what you see.

Conversaciones completas de sesiones reales: [ERR_CONNECTION_REFUSED](docs/examples/before-after-1.md) · [Instalar Python](docs/examples/before-after-2.md) · [Deshacer lo de ayer](docs/examples/before-after-3.md) · [Permission denied](docs/examples/before-after-4.md)

## Las 10 reglas

1. **Di dónde, no qué.** "Presiona ⌘ y la barra espaciadora, escribe Terminal", nunca "abre tu shell".
2. **Un paso, y a esperar.** Hace por sí mismo lo que puede. Lo que solo tú puedes hacer te lo pide un paso a la vez.
3. **Cada comando viene con su recibo.** Qué hace, cómo se ve cuando sale bien, qué hacer si no sale.
4. **Ninguna palabra sin explicación.** Cada término técnico lleva un significado sencillo en cinco palabras o menos.
5. **Frena antes de instalar, borrar, cobrar, enviar o publicar.** Te dice cuánto cuesta y cómo deshacerlo, y espera tu "sí".
6. **La que se equivoca es la computadora, no tú.** "La computadora dijo X. Eso significa Y. Siguiente: Z." Nada de "seguramente tú…".
7. **Lleva el diario.** `WHAT-WE-DID.md`: fecha, qué cambió, cómo deshacerlo.
8. **Lo aburrido y seguro gana.** Versiones estables, instaladores oficiales, la opción que se puede deshacer.
9. **Muestra el texto exacto.** Lo que hay que escribir va solo en un recuadro. Lo que hay que pulsar, con su nombre exacto y dónde está.
10. **Termina con una sola acción siguiente.** Nada de menús de opciones.

## Funciona con

| Asistente | Cómo |
| --- | --- |
| Claude Code | Plugin (arriba), o [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) → `CLAUDE.md` |
| Codex y otros asistentes que leen `AGENTS.md` | [`install/AGENTS.md.snippet`](install/AGENTS.md.snippet) → `AGENTS.md` en la carpeta de tu proyecto |
| Cursor | [`install/cursor-rule.mdc`](install/cursor-rule.mdc) → `.cursor/rules/i-am-not-a-developer.mdc` |
| Cualquier cosa que lea `SKILL.md` | [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md) |

## Ajústalo a tu gusto

1. Haz un fork de este repositorio en GitHub.
2. Edita `skills/i-am-not-a-developer/SKILL.md`. Mantenlo por debajo de 600 palabras; se queda en la memoria del asistente durante toda la sesión, así que mientras más corto, mejor. Copia el mismo texto en los tres archivos de `install/`.
3. Ejecuta `python3 scripts/check.py` para confirmar que los archivos están sincronizados.
4. Cambia el marketplace por el tuyo:

```
claude plugin marketplace remove i-am-not-a-developer
claude plugin marketplace add YOUR-NAME/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

¿Quieres cambiar una regla para todos? [Abre un issue](https://github.com/kajisho5/i-am-not-a-developer/issues) con el mensaje y la respuesta que salió mal. La lista se queda en 10 reglas: los arreglos cambian la redacción, no la cantidad.

## Créditos

El formato (un solo `SKILL.md`, una lista corta de reglas, un README con Antes/Después) se inspiró en [i-have-adhd](https://github.com/ayghri/i-have-adhd). Las reglas, los textos y los ejemplos de aquí son originales.

## Licencia

[MIT](LICENSE)
