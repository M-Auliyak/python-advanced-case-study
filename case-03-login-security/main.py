import functools
import hashlib
import re
import secrets
from datetime import datetime

POLA_USERNAME = re.compile(r"[A-Za-z0-9]{5,}")   
POLA_PASSWORD = re.compile(r"(?=.*[0-9]).{8,}")   
class User:
    def __init__(self, username, password):
        self.username = username   # memicu setter -> validasi
        self.password = password   # memicu setter -> validasi + hashing
 
    @property
    def username(self):
        return self._username
 
    @username.setter
    def username(self, nilai):
        if not isinstance(nilai, str):
            raise ValueError("Username harus berupa teks")
        if not POLA_USERNAME.fullmatch(nilai):
            raise ValueError(
                "Username harus minimal 5 karakter, hanya huruf dan angka (tanpa spasi/simbol)"
            )
        self._username = nilai
 