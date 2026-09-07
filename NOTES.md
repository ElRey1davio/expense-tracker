# Project 1: Expense Tracker — Progress Log


Update this after each session, even briefly. Read it first thing next time
instead of trying to remember where you left off.

---

## Session 1 — [31/08/2026]

**Built:**
- Project structure (`app.py`, `models.py`, `requirements.txt`, `templates/`, `static/`)
- First working Flask route: `GET /` returns expenses joined into a string
- Ran the app successfully with `python app.py`, confirmed blank page (expected — `expenses` list is empty)

**Learned:**
- `@app.route()` needs `app = Flask(__name__)` defined first
- `"\n".join(list)` turns a list into one string; on an empty list it returns `""`, not `None`
- Flask defaults to GET if `methods` isn't specified
- `<int:var>` in a route path is a converter — captures + type-casts part of the URL

**Decided:**
- Using Postgres (via Supabase) instead of SQLite, once account setup is sorted (Neon site had loading issues)
- Adding `category` column later, once the ML classifier step arrives — not now, one concept at a time

**Next session, start here:**
- Add some fake data to `expenses` list so `/` actually shows something
- Build the `/add` route (GET shows a form, POST handles submission)

**Stuck on / confused about:**
- (nothing blocking right now)



## Git Cheat Sheet (my own notes)

WHAT EACH COMMAND DOES:
- git init            → start tracking this folder with git
- git status          → check what's changed / staged / committed (run this A LOT)
- git add .            → stage all changed files for the next commit
- git commit -m "msg"  → save a snapshot with a description of what changed
- git remote add origin <url>  → link local folder to a GitHub repo
- git push -u origin main      → upload commits to GitHub
- git checkout -b <name>       → create + switch to a new branch (for trying things safely)
- git checkout main             → switch back to main branch

RULE I LEARNED THE HARD WAY:
- Type/paste ONE command at a time in PowerShell. Pasting several 
  lines together can crash the terminal (PSReadLine bug) — not my fault, 
  just restart the terminal and continue if it happens.

MY STATUS:
- ✅ git init, add, commit — done, first commit made (3 files)
- ⏳ GitHub remote + push — in progress
- ⏳ branching — not yet practiced
- ⏳ Postgres/Supabase — total beginner, still to learn


## Flask + API practice — Session 1
- Dynamic routes: <var> in @app.route(), matched in function params
- Chained dict access: data["rates"][to_currency]
- Read tracebacks bottom-up — find the last frame in YOUR file
- Always check API response shape before using it (if "key" not in data)
- Built: /convert/<from>/<to> route with graceful error handling