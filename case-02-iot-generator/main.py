import random
import time
import tracemalloc

SUHU_MIN = 15.0
SUHU_MAX = 38.0


def baca_sensor(jumlah=None):
    nomor = 0
    while jumlah is None or nomor < jumlah:
        nomor += 1
        yield round(random.uniform(SUHU_MIN, SUHU_MAX), 1)


def kategorikan(suhu):
    if suhu < 20:
        return "Dingin"
    if suhu <= 30:
        return "Normal"
    return "Panas"


def demo_memori(n=1_000_000):
    tracemalloc.start()
    total = 0.0
    for suhu in baca_sensor(n):
        total += suhu
    _, puncak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"\nStreaming {n:,} data selesai tanpa menyimpan list.")
    print(f"  Rata-rata suhu : {total / n:.2f} °C")
    print(f"  Puncak memori  : {puncak:,} byte")


def main():
    random.seed(42)
    sensor = baca_sensor()   

    print("=== MONITOR SUHU STASIUN CUACA ===")
    print(f"{'Baca ke-':<10}{'Suhu (°C)':>10}   Status")
    print("-" * 32)

    # Konsumsi satu per satu dengan next()
    for urutan in range(1, 13):
        suhu = next(sensor)
        print(f"{urutan:<10}{suhu:>10.1f}   {kategorikan(suhu)}")
        time.sleep(0.05)  

    demo_memori()


if __name__ == "__main__":
    main()