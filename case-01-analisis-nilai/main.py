data_mahasiswa = [
    {"nama": "Aisyah",   "nim": "230101", "tugas": 85, "uts": 80, "uas": 88}, 
    {"nama": "Budi",     "nim": "230102", "tugas": 70, "uts": 65, "uas": 75}, 
    {"nama": "Cantika",  "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Satrio",   "nim": "230104", "tugas": 80, "uts": 75, "uas": 82},
    {"nama": "Dika",     "nim": "230105", "tugas": 85, "uts": 75, "uas": 79},
] 

BOBOT = {"tugas": 0.30, "uts":0.30, "uas": 0.40 }
Nilai_Prestasi = 80

def hitung_nilai_akhir (mhs):
    return round(sum(mhs[komponen]* bobot for komponen, bobot in BOBOT.items()),2)

def cetak_tabel(judul, daftar):
    print(f"\n{judul}")
    print("-" * 52)
    print(f"{'No':<4}{'Nama':<12}{'NIM':<10}{'Tugas':>6}{'UTS':>6}{'UAS':>6}{'Akhir':>8}")
    print("-" * 52)
    for i, m in enumerate(daftar, start=1):
        print(f"{i:<4}{m['nama']:<12}{m['nim']:<10}{m['tugas']:>6}{m['uts']:>6}"
              f"{m['uas']:>6}{m['nilai_akhir']:>8.2f}")


def main():
    mahasiswa = [{**m, "nilai_akhir": hitung_nilai_akhir(m)} for m in data_mahasiswa]
    cetak_tabel("1. DAFTAR NILAI AKHIR", mahasiswa)
 
    berprestasi = [m for m in mahasiswa if m["nilai_akhir"] > Nilai_Prestasi]
    cetak_tabel(f"2. MAHASISWA BERPRESTASI (nilai akhir > {Nilai_Prestasi})", berprestasi)

    ranking = sorted(mahasiswa, key=lambda m: m["nilai_akhir"], reverse=True)
    cetak_tabel("3. RANKING (tertinggi ke terendah)", ranking)
 
    terbaik = ranking[0]
    print("\n4. MAHASISWA TERBAIK")
    print("-" * 52)
    print(f"Nama        : {terbaik['nama']}")
    print(f"NIM         : {terbaik['nim']}")
    print(f"Tugas / UTS / UAS : {terbaik['tugas']} / {terbaik['uts']} / {terbaik['uas']}")
    print(f"Nilai Akhir : {terbaik['nilai_akhir']:.2f}")
 
    nama_besar = list(map(lambda m: m["nama"].upper(), ranking))
    print(f"\nUrutan nama (hasil map + lambda): {nama_besar}")
 
 
if __name__ == "__main__":
    main()