<!-- Short, focused instructions for AI coding agents working on this repository -->
# Copilot instructions — OIBSIP repository

This repository contains a few small, mostly independent Python projects. Give concise, repository-specific suggestions only; avoid generic guidance.

Key components
- weatheraaplication/: A Django 5 project. The main app is `weatherupdates` which renders a simple form and calls the OpenWeatherMap API. Key files:
  - `manage.py` — Django CLI entrypoint.
  - `weatheraaplication/settings.py` — uses SQLite (db.sqlite3) and DEBUG=True.
  - `weatheraaplication/weatherupdates/views.py` — single view `index` handling POST form input, calls OpenWeatherMap API, and renders `weatherupdates/home.html` or `404.html` on errors.
- voice_assistant/: A small Python script-based voice assistant. See `voice_assist.py` and `README.md` for dependencies and usage notes.
- password_generator/: Standalone script `pass_word.py` and README; typical run with `python pass_word.py`.

What to do when editing
- For Django changes, update `manage.py` invocations and `settings.py` only if you understand Django startup. Use `python manage.py runserver` to test locally.
- Preserve the single-responsibility pattern used in `weatherupdates/views.py` — the view both handles form input and formats the API response into `city_weather_update` dict.
- Small scripts (voice assistant, password generator) are meant to be runnable scripts: prefer minimal-invasive changes and keep CLI behavior intact.

Run / debug commands (Windows PowerShell)
- Install dependencies (project has no requirements.txt; infer per-folder):
  - For Django app: create a venv and install Django 5.x and requests:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1; pip install django==5.2.4 requests

  - For voice assistant: install `speech_recognition`, `pyttsx3`, and `wikipedia` as needed.

- Run Django dev server (from repository root):

    .\.venv\Scripts\Activate.ps1; python weatheraaplication\manage.py runserver

- Run individual scripts:

    python password_generator\pass_word.py
    python voice_assistant\voice_assist.py

Patterns & conventions discovered
- Single-view app: `weatherupdates/views.py` defines an `index` view that handles both GET and POST. It builds a `city_weather_update` dict and passes it to the template. When updating templates, search for keys like `city`, `description`, `temperature`, `icon`, `wind`, `humidity`, `time`.
- Minimal error handling: the Django view uses a bare `except:` to render `404.html`. Prefer adding targeted exception handling (requests exceptions, KeyError) if changing behavior.
- Secret/config: `weatheraaplication/settings.py` contains an inline `SECRET_KEY` and DEBUG=True. Don't add production secrets — follow existing convention (no environment variable wiring present).

Integration points
- OpenWeatherMap API used in `weatherupdates/views.py`. API key is hard-coded in the view. If adding features, either keep the same simple approach or refactor to use environment variables consistently across the repo.

Files to reference when making changes
- `weatheraaplication/manage.py` — project entrypoint.
- `weatheraaplication/weatheraaplication/settings.py` — DB and settings.
- `weatheraaplication/weatherupdates/views.py` — main logic to inspect/modify.
- `weatheraaplication/weatherupdates/templates/weatherupdates/*` — UI templates (home.html, 404.html).
- `voice_assistant/README.md` and `voice_assistant/voice_assist.py` — lightweight script patterns.
- `password_generator/pass_word.py` and `password_generator/README.md` — simple CLI script example.

When to ask the human
- If a change requires adding new dependencies, modifying settings (DB, SECRET_KEY), or changing run workflow, ask for confirmation.
- If you need to store or rotate API keys, request the preferred secret-management pattern (env var, .env, or CI secrets).

If anything here is unclear or you want me to expand examples (e.g., show a sample refactor of the API key to environment variables or add a requirements.txt), tell me which area to update.
