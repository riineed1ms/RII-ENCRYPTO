import json
import unittest
from pathlib import Path

import rii_encrypto as m

TABLE = json.load(open(Path(__file__).parent / "data.json", encoding="utf-8"))


def original_encrypt(text, data):
    enc = ""
    for i in text:
        for j in data.keys():
            if i == j:
                enc = enc + data.get(i)
        if i not in data.keys():
            enc = enc + i
    return enc


def original_decrypt(text, data):
    dec = ""
    for i in text:
        for key, value in data.items():
            if i == value:
                dec = dec + key
        if i not in data.values():
            dec = dec + i
    return dec


class Tests(unittest.TestCase):
    samples = ["Hello World 123", "RII ENCRYPTO V 1.0.0", "abc XYZ 0987654321",
               "teks, dengan! tanda? baca.", "", "   "]

    def test_matches_original_algorithm(self):
        t = m.load_table()
        for s in self.samples:
            self.assertEqual(m.encrypt_text(s, t), original_encrypt(s, TABLE))
            self.assertEqual(m.decrypt_text(s, t), original_decrypt(s, TABLE))

    def test_roundtrip(self):
        t = m.load_table()
        for s in self.samples:
            self.assertEqual(m.decrypt_text(m.encrypt_text(s, t), t), s)

    def test_known_values(self):
        t = m.load_table()
        self.assertEqual(m.encrypt_text("Aa", t), "Çü")

    def test_all_table_chars(self):
        t = m.load_table()
        s = "".join(t.keys())
        self.assertEqual(m.decrypt_text(m.encrypt_text(s, t), t), s)


if __name__ == "__main__":
    unittest.main()
