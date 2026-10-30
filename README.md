# RII ENCRYPTO

Terminal text encryption tool with a clean, professional black, cyan and white interface.
Letters, numbers and spaces are substituted using the table in `data.json`, so text encrypted
with this tool can be decrypted again with the same table.

Version: V: 1.0.0

## Features

- Encrypt Text
- Decrypt Text
- Return to menu or exit after every operation
- Fully compatible with the original `data.json` substitution table

## Requirements

- Python 3.7 or newer
- colorama (listed in `requirements.txt`)

## Installation and Usage

```
pip install -r requirements.txt
python3 rii_encrypto.py
```

On Windows use `python rii_encrypto.py`.

## Project Structure

| File               | Description                                  |
| ------------------ | -------------------------------------------- |
| `rii_encrypto.py`  | Main program (banner, menu, encrypt, decrypt) |
| `data.json`        | Substitution table (unchanged)               |
| `requirements.txt` | Python dependencies                          |
| `test_rii_encrypto.py` | Automated tests (`python3 test_rii_encrypto.py`) |
| `LICENSE`          | Original license (Boost Software License 1.0) |

## Notes

Characters that are not in `data.json` (for example punctuation) are kept as they are.
Do not include characters from the encrypted alphabet (such as accented letters used by the
table) in your original text, because they would be converted back during decryption.

## Creator

- TikTok: @rii_project
- Account: @riineed1mshaujvz
- WhatsApp Channel: https://whatsapp.com/channel/0029Vb9CF7cLCoX3LWHm0A10

This project is derived from Black-Encrypto and keeps its original license.
