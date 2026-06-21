import csv
from collections import deque

FILE_CSV = "rental_ps.csv"

# =========================
# INISIALISASI FILE CSV
# =========================
def init_file():
    try:
        with open(FILE_CSV, "x", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID_Sewa",
                "Nama_Pelanggan",
                "No_PS",
                "Durasi",
                "Tarif",
                "Total_Bayar",
                "Status"
            ])
    except FileExistsError:
        pass

# =========================
# LOAD DATA
# =========================
def load_data():
    data = []
    try:
        with open(FILE_CSV, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        pass
    return data

# =========================
# SAVE DATA
# =========================
def save_data(data):
    with open(FILE_CSV, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "ID_Sewa",
            "Nama_Pelanggan",
            "No_PS",
            "Durasi",
            "Tarif",
            "Total_Bayar",
            "Status"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

# =========================
# CREATE
# =========================
def tambah_penyewaan():
    data = load_data()

    id_sewa = input("ID Sewa            : ")
    nama = input("Nama Pelanggan     : ")
    no_ps = input("Nomor PS           : ")
    durasi = int(input("Durasi (Jam)       : "))
    tarif = int(input("Tarif per Jam      : "))

    total = durasi * tarif

    transaksi = {
        "ID_Sewa": id_sewa,
        "Nama_Pelanggan": nama,
        "No_PS": no_ps,
        "Durasi": durasi,
        "Tarif": tarif,
        "Total_Bayar": total,
        "Status": "Aktif"
    }

    data.append(transaksi)
    save_data(data)

    print("\nData berhasil ditambahkan!")
    print("Total Bayar : Rp", total)

# =========================
# READ
# =========================
def tampilkan_data():
    data = load_data()

    if not data:
        print("Belum ada data.")
        return

    print("\n===== DATA PENYEWAAN =====")

    for item in data:
        print("-" * 40)
        print("ID Sewa       :", item["ID_Sewa"])
        print("Nama          :", item["Nama_Pelanggan"])
        print("No PS         :", item["No_PS"])
        print("Durasi        :", item["Durasi"], "Jam")
        print("Tarif         : Rp", item["Tarif"])
        print("Total Bayar   : Rp", item["Total_Bayar"])
        print("Status        :", item["Status"])

# =========================
# UPDATE
# =========================
def update_data():
    data = load_data()

    kode = input("Masukkan ID Sewa : ")

    ditemukan = False

    for item in data:
        if item["ID_Sewa"] == kode:

            status_baru = input("Status Baru (Aktif/Selesai): ")
            item["Status"] = status_baru

            ditemukan = True
            break

    if ditemukan:
        save_data(data)
        print("Data berhasil diupdate.")
    else:
        print("Data tidak ditemukan.")

# =========================
# DELETE
# =========================
def hapus_data():
    data = load_data()

    kode = input("Masukkan ID Sewa yang akan dihapus : ")

    data_baru = []
    ditemukan = False

    for item in data:
        if item["ID_Sewa"] == kode:
            ditemukan = True
        else:
            data_baru.append(item)

    if ditemukan:
        save_data(data_baru)
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan.")

# =========================
# SEARCHING (HASH MAP)
# =========================
def cari_data():
    data = load_data()

    hashmap = {}

    for item in data:
        hashmap[item["ID_Sewa"]] = item

    kode = input("Masukkan ID Sewa : ")

    if kode in hashmap:

        print("\nDATA DITEMUKAN")
        print("-" * 30)

        for k, v in hashmap[kode].items():
            print(f"{k} : {v}")

    else:
        print("Data tidak ditemukan.")

# =========================
# SORTING
# =========================
def sorting_total_bayar():
    data = load_data()

    data.sort(
        key=lambda x: int(x["Total_Bayar"]),
        reverse=True
    )

    print("\n===== TOTAL BAYAR TERBESAR =====")

    for item in data:
        print(
            item["ID_Sewa"],
            "-",
            item["Nama_Pelanggan"],
            "- Rp",
            item["Total_Bayar"]
        )

# =========================
# QUEUE ANTRIAN
# =========================
antrian = deque()

def tambah_antrian():
    nama = input("Nama Pelanggan : ")
    antrian.append(nama)

    print("Pelanggan masuk antrian.")

def panggil_antrian():
    if antrian:
        print("Memanggil :", antrian.popleft())
    else:
        print("Antrian kosong.")

def lihat_antrian():
    if not antrian:
        print("Antrian kosong.")
    else:
        print("\n===== DAFTAR ANTRIAN =====")
        for i, nama in enumerate(antrian, start=1):
            print(f"{i}. {nama}")

# =========================
# MENU
# =========================
def menu():
    init_file()

    while True:

        print("\n")
        print("=" * 45)
        print(" SISTEM RENTAL PLAYSTATION ")
        print("=" * 45)
        print("1. Tambah Penyewaan")
        print("2. Tampilkan Data")
        print("3. Cari Data")
        print("4. Update Status")
        print("5. Hapus Data")
        print("6. Urutkan Total Bayar")
        print("7. Tambah Antrian")
        print("8. Panggil Antrian")
        print("9. Lihat Antrian")
        print("0. Keluar")

        pilih = input("Pilih Menu : ")

        if pilih == "1":
            tambah_penyewaan()

        elif pilih == "2":
            tampilkan_data()

        elif pilih == "3":
            cari_data()

        elif pilih == "4":
            update_data()

        elif pilih == "5":
            hapus_data()

        elif pilih == "6":
            sorting_total_bayar()

        elif pilih == "7":
            tambah_antrian()

        elif pilih == "8":
            panggil_antrian()

        elif pilih == "9":
            lihat_antrian()

        elif pilih == "0":
            print("Terima kasih telah menggunakan aplikasi.")
            break

        else:
            print("Pilihan tidak tersedia!")

menu()