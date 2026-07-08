import sys
import shutil
import os 

BANNER = r"""
    ╔═══════════════════════════════════════════════════════════╗
    ║                   ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗     ║
    ║                   ██╔══██╗██║  ██║██║██╔════╝██║  ██║     ║
    ║                   ██████╔╝███████║██║███████╗███████║     ║
    ║                   ██╔═══╝ ██╔══██║██║╚════██║██╔══██║     ║
    ║                   ██║     ██║  ██║██║███████║██║  ██║     ║
    ║                   ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝     ║
    ║                                                           ║
    ║           Educational Phishing Simulation Tool            ║
    ║               For Security Research Only                  ║
    ╚═══════════════════════════════════════════════════════════╝
"""

WARNING = """
╔══════════════════════════════════════════════════════════════════════╗
║                     DISCLAIMER & TERMS OF USE                        ║
╠══════════════════════════════════════════════════════════════════════╣
║  This tool is developed STRICTLY for educational and security        ║
║  research purposes ONLY. It demonstrates how phishing attacks        ║
║  function so that defenders can better understand and mitigate       ║
║  these threats.                                                      ║
║                                                                      ║
║    PROHIBITED USE                                                    ║   
║  ─────────────────────                                               ║
║  • Do NOT use this tool to target individuals without consent        ║
║  • Do NOT use this tool for identity theft or fraud                  ║
║  • Do NOT use this tool to violate any applicable laws               ║
║  • Do NOT deploy this against any system you do not own              ║
║                                                                      ║
║  By accepting, you acknowledge:                                      ║
║  • You will only test systems you own or have explicit permission    ║
║  • You understand the ethical implications of phishing               ║
║  • The developers assume NO liability for any misuse                 ║
╚══════════════════════════════════════════════════════════════════════╝
"""

MENU = """
╔══════════════════════════════════════════════════╗
║           SELECT TARGET PLATFORM                 ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║     [1]     Facebook                             ║
║     [2]     Instagram                            ║
║     [3]     Snapchat                             ║
║     [0]     Exit                                 ║
║                                                  ║
╚══════════════════════════════════════════════════╝
"""

PLATFORM_MAP = {1: 'facebook', 2: 'instagram', 3: 'snapchat'}


def _styled_input(prompt: str) -> str:
    return input(prompt).strip()


def display_banner() -> None:
    print(BANNER)


def display_warning() -> None:
    print(WARNING)


def get_acceptance() -> bool:
    while True:
        choice = _styled_input('\n  Do you accept the terms and conditions? [y/N]: ').lower()
        if choice == 'y':
            return True
        if choice in ('n', ''):
            return False
        print('  Invalid input. Please enter "y" or "n".')


def display_menu() -> None:
    os.system("cls" if os.name == "nt" else "clear")
    print(BANNER)
    print(MENU)
    


def get_platform_choice() -> int | None:
    while True:
        choice = _styled_input('  Enter your choice [0-3]: ')
        if choice == '0':
            return None
        try:
            num = int(choice)
            if num in PLATFORM_MAP:
                return num
            print('  Invalid choice. Please enter a number between 0 and 3.')
        except ValueError:
            print('  Invalid input. Please enter a number.')


def get_platform_name(choice: int) -> str | None:
    return PLATFORM_MAP.get(choice)
