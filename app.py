#!/usr/bin/env python3
"""
PhishLab — Educational Phishing Simulation Tool
=================================================

Intended for educational and authorised security testing ONLY.

Architecture:
  app.py          Entry point & Flask application factory
  core/cli.py     Terminal-based UI (warning, consent, menu)
  core/collector.py   Credential capture, logging & persistent storage
  web/routes.py   Flask route handlers / HTTP layer
  web/templates/  Jinja2 HTML templates for each platform
  web/static/     CSS assets
  data/           Runtime credential storage (data.txt)

Usage:
  python app.py
"""

import sys
import webbrowser

from flask import Flask

from core.cli import (
    display_banner,
    display_warning,
    get_acceptance,
    display_menu,
    get_platform_choice,
    get_platform_name,
)
from web.routes import web_bp

HOST = '127.0.0.1'
PORT = 5000cd ..


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(web_bp)
    return app


def main() -> None:
   
    display_warning()

    if not get_acceptance():
        print('\n  Terms not accepted. Exiting.\n')
        sys.exit(0)

    display_menu()
    choice = get_platform_choice()

    if choice is None:
        print('\n  Exiting.\n')
        sys.exit(0)

    platform = get_platform_name(choice)
    url = f'http://{HOST}:{PORT}/{platform}'

    print(f'\n  [+] Server starting at {url}')
    print(f'  [+] Press Ctrl+C to stop the server\n')

    app = create_app()
    webbrowser.open(url, new=2)

    try:
        app.run(host=HOST, port=PORT, debug=False)
    except KeyboardInterrupt:
        print('\n  Server stopped by user.\n')
        sys.exit(0)


if __name__ == '__main__':
    main()
