import functools
import hashlib
import re
import secrets
from datetime import datetime

# Pola RegEx (dipakai dengan fullmatch -> seluruh teks harus cocok)
POLA_USERNAME = re.compile(r"[A-Za-z0-9]{5,}")   # alfanumerik, min 5 karakter
POLA_PASSWORD = re.compile(r"(?=.*[0-9]).{8,}")   # lookahead: wajib ada angka 0-9, min 8 karakter
