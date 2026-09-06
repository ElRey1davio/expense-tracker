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
