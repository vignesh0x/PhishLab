# PhishLab

A educational phishing simulation tool built with Python and Flask. Designed for security researchers and students to understand how credential harvesting attacks work in order to build better defenses.

## ⚠️ Disclaimer

**This tool is for educational and authorised security testing ONLY.**

Unauthorised use of this tool to access accounts or systems without explicit consent is illegal. The developers assume **zero liability** for any misuse. You are responsible for complying with all applicable laws in your jurisdiction.

## Features

- **Terminal-based consent flow** — clear ethical warning with y/n acceptance before any action
- **3 platform login pages** — Facebook, Instagram, Snapchat (modern, responsive clones)
- **Local credential capture** — captured data printed to terminal and persisted to `data/data.txt`
- **Redirect after capture** — victims are redirected to the real platform after submitting credentials
- **Extensible architecture** — add new platforms with minimal code changes

## Project Structure

```
PhishLab/
├── app.py                  # Entry point, Flask app factory, CLI orchestration
├── requirements.txt        # Python dependencies (flask>=3.0)
├── README.md
├── core/                   # Core logic (no Flask dependency)
│   ├── cli.py              # Terminal UI: banner, warning consent, platform menu
│   └── collector.py        # Credential logging, timestamping, file persistence
├── web/                    # Web layer (Flask-specific)
│   ├── routes.py           # Blueprint: GET /, /facebook, /instagram, /snapchat / POST /login/<platform>
│   ├── templates/          # Jinja2 HTML templates
│   │   ├── menu.html
│   │   ├── facebook.html
│   │   ├── instagram.html
│   │   └── snapchat.html
│   └── static/css/
│       └── style.css       # Shared styles across all pages
└── data/                   # Runtime credential storage (created on first capture)
    └── data.txt
```

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the tool
python app.py
```

Follow the terminal prompts:

1. Read and accept the terms of use (y/n)
2. Select a target platform (1-3)
3. A browser window opens with the cloned login page
4. Entered credentials are captured to the terminal and saved to `data/data.txt`

## Adding a New Platform

1. Create a new HTML template in `web/templates/` (e.g. `twitter.html`)
2. Add a route in `web/routes.py`:
   ```python
   @web_bp.route('/twitter')
   def twitter():
       return render_template('twitter.html')
   ```
3. Register the platform in `core/cli.py`:
   ```python
   PLATFORM_MAP = {1: 'facebook', 2: 'instagram', 3: 'snapchat', 4: 'twitter'}
   ```
4. Add the redirect URL in `web/routes.py`:
   ```python
   _REDIRECT_MAP = { ..., 'twitter': 'https://twitter.com' }
   ```

No changes to `app.py`, `collector.py`, or the menu template are required.

## Architecture Notes

- **Separation of concerns** — `core/` has zero Flask imports; `web/` handles all HTTP concerns. This keeps testing and future migration clean.
- **Stateless collector** — `collector.py` is a simple module with a single `save_credentials()` function. Swap it for a database, API, or encryption layer without touching routes.
- **Blueprint pattern** — All routes live in a Flask Blueprint for modular registration.

## License

This project is licensed under the [MIT License](LICENSE) — you are free to use, modify, and distribute this software with attribution.

## Contributing

Contributions are welcome! Anyone can fork this repository, fix bugs, or add new features. Once you're done, open a Pull Request — I'll review it and merge it in. Let's build something useful together.
