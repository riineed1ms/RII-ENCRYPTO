#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RII ENCRYPTO - terminal text encryption tool.

Encryption uses the substitution table stored in data.json
(one character is replaced by exactly one character).
"""

import json
import os
import sys
from pathlib import Path

from colorama import Fore, Style, init as colorama_init

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data.json"

VERSION = "V: 1.0.0"
TIKTOK = "@rii_project"
ACCOUNT = "@riineed1mshaujvz"
CHANNEL = "https://whatsapp.com/channel/0029Vb9CF7cLCoX3LWHm0A10"

# ASCII block font (same family as the original banner).
GLYPHS = {
    "R": [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔══██╗",
        "██║  ██║",
        "╚═╝  ╚═╝",
    ],
    "I": [
        "██╗",
        "██║",
        "██║",
        "██║",
        "██║",
        "╚═╝",
    ],
    "E": [
        "███████╗",
        "██╔════╝",
        "█████╗  ",
        "██╔══╝  ",
        "███████╗",
        "╚══════╝",
    ],
    "N": [
        "███╗   ██╗",
        "████╗  ██║",
        "██╔██╗ ██║",
        "██║╚██╗██║",
        "██║ ╚████║",
        "╚═╝  ╚═══╝",
    ],
    "C": [
        " ██████╗",
        "██╔════╝",
        "██║     ",
        "██║     ",
        "╚██████╗",
        " ╚═════╝",
    ],
    "Y": [
        "██╗   ██╗",
        "╚██╗ ██╔╝",
        " ╚████╔╝ ",
        "  ╚██╔╝  ",
        "   ██║   ",
        "   ╚═╝   ",
    ],
    "P": [
        "██████╗ ",
        "██╔══██╗",
        "██████╔╝",
        "██╔═══╝ ",
        "██║     ",
        "╚═╝     ",
    ],
    "T": [
        "████████╗",
        "╚══██╔══╝",
        "   ██║   ",
        "   ██║   ",
        "   ██║   ",
        "   ╚═╝   ",
    ],
    "O": [
        " ██████╗ ",
        "██╔═══██╗",
        "██║   ██║",
        "██║   ██║",
        "╚██████╔╝",
        " ╚═════╝ ",
    ],
}

WIDTH = 68  # inner width of every panel


# ---------------------------------------------------------------- core logic
def load_table(path=DATA_FILE):
    """Load data.json and verify that it is a one-to-one table."""
    with open(path, encoding="utf-8") as fh:
        table = json.load(fh)
    values = list(table.values())
    if len(set(values)) != len(values):
        raise ValueError("data.json contains duplicate values; decryption would be ambiguous.")
    return table


def encrypt_text(text, table):
    """Replace every character found in the table; keep all others unchanged."""
    return "".join(table.get(ch, ch) for ch in text)


def decrypt_text(text, table):
    """Reverse of encrypt_text using the same table."""
    reverse = {value: key for key, value in table.items()}
    return "".join(reverse.get(ch, ch) for ch in text)


# ---------------------------------------------------------------- rendering
C = Style.BRIGHT + Fore.CYAN
W = Style.BRIGHT + Fore.WHITE
D = Style.NORMAL + Fore.CYAN
R = Style.RESET_ALL


def render_word(word):
    rows = ["", "", "", "", "", ""]
    for letter in word:
        for i, part in enumerate(GLYPHS[letter]):
            rows[i] += part
    return rows


def clear_screen():
    if sys.stdout.isatty():
        os.system("cls" if os.name == "nt" else "clear")


def line(left, fill, right, title=""):
    if title:
        head = f"{fill} {title} "
        return D + left + head + fill * (WIDTH - len(head)) + right + R
    return D + left + fill * WIDTH + right + R


def row(text="", label=None):
    body = f"  {label:<10}{text}" if label else f"  {text}"
    return D + "│" + W + body.ljust(WIDTH) + D + "│" + R


def panel(title, rows):
    out = [line("┌", "─", "┐", title)]
    out.extend(rows)
    out.append(line("└", "─", "┘"))
    return "\n".join(out)


def banner():
    clear_screen()
    print()
    for r_line in render_word("RII"):
        print(" " + W + r_line + R)
    for e_line in render_word("ENCRYPTO"):
        print(" " + C + e_line + R)
    print()
    info = [
        row(VERSION, "Version"),
        row(TIKTOK, "TikTok"),
        row(ACCOUNT, "Account"),
        row("WhatsApp Channel"),
        row(CHANNEL),
    ]
    print(panel("INFORMATION", info))


def menu():
    items = [
        row("[1]  Encrypt Text"),
        row("[2]  Decrypt Text"),
        row("[3]  Exit"),
    ]
    print()
    print(panel("MENU", items))


def result_panel(title, text):
    print()
    print(line("┌", "─", "┐", title))
    chunks = [text[i:i + WIDTH - 4] for i in range(0, len(text), WIDTH - 4)] or [""]
    for chunk in chunks:
        print(D + "│" + W + ("  " + chunk).ljust(WIDTH) + D + "│" + R)
    print(line("└", "─", "┘"))
    print(D + "  Result (raw text, safe to copy):" + R)
    print(W + text + R)


def prompt(label):
    return input("\n" + C + label + R + " " + W)


# ---------------------------------------------------------------- actions
def action_encrypt(table):
    text = prompt("Enter text to encrypt >")
    print(R, end="")
    result_panel("ENCRYPTED OUTPUT", encrypt_text(text, table))


def action_decrypt(table):
    text = prompt("Enter text to decrypt >")
    print(R, end="")
    result_panel("DECRYPTED OUTPUT", decrypt_text(text, table))


def goodbye():
    print()
    print(panel("RII ENCRYPTO", [
        row("Thank you for using RII ENCRYPTO."),
        row(),
        row(TIKTOK, "TikTok"),
        row(ACCOUNT, "Account"),
        row("WhatsApp Channel"),
        row(CHANNEL),
    ]))
    print()


def main():
    colorama_init()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass
    try:
        table = load_table()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"Failed to load {DATA_FILE.name}: {exc}")
        return 1

    try:
        while True:
            banner()
            menu()
            choice = prompt("Select an option [1-3] >").strip()
            print(R, end="")
            if choice == "1":
                action_encrypt(table)
            elif choice == "2":
                action_decrypt(table)
            elif choice == "3":
                goodbye()
                return 0
            else:
                print("\n" + Fore.WHITE + "  Invalid option. Please choose 1, 2 or 3." + R)

            back = prompt("Return to menu? [y = menu / n = exit] >").strip().lower()
            print(R, end="")
            if back in ("n", "no"):
                goodbye()
                return 0
    except (KeyboardInterrupt, EOFError):
        print(R)
        goodbye()
        return 0


if __name__ == "__main__":
    sys.exit(main())
