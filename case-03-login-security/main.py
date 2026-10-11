import functools
import hashlib
import re
import secrets
from datetime import datetime

POLA_USERNAME = re.compile(r"[A-Za-z0-9]{5,}")   
POLA_PASSWORD = re.compile(r"(?=.*[0-9]).{8,}")   
class User:
    def __init__(self, username, password):
        self.username = username   
        self.password = password   
 
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
    @property
    def password(self):
        # Password asli tidak pernah dikembalikan
        raise AttributeError("Password tidak dapat dibaca")
 
    @password.setter
    def password(self, nilai):
        if not isinstance(nilai, str):
            raise ValueError("Password harus berupa teks")
        if not POLA_PASSWORD.fullmatch(nilai):
            raise ValueError("Password harus minimal 8 karakter dan memuat setidaknya satu angka")
        self._salt = secrets.token_hex(8)
        self._hash = hashlib.sha256((self._salt + nilai).encode()).hexdigest()

def audit_log(riwayat):
    
    def dekorator(fungsi_login):
        @functools.wraps(fungsi_login)
        def pembungkus(username, password):
            waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                hasil = fungsi_login(username, password)
                status, alasan = "BERHASIL", "-"
            except ValueError as err:
                hasil = False
                status, alasan = "DITOLAK", str(err)
            baris = f"[{waktu}] user={username!r:<14} status={status:<8} alasan={alasan}"
            riwayat.append(baris)
            print(baris)
            return hasil
 
        return pembungkus
 
    return dekorator
 
 
riwayat_audit = []
 
 
@audit_log(riwayat_audit)
def login(username, password):
    """Logika otentikasi murni: membuat User memicu semua validasi."""
    User(username, password)
    return True