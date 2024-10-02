nama = input("Masukkan nama karyawan: ")
gol = input("Masukkan golongan karyawan: ").upper()
jam_kerja = int(input("Masukkan jam kerja selama seminggu: "))

def golongan(golongan):
    if golongan == "A":
        return 5000
    elif golongan == "B":
        return 7000
    elif golongan == "C":
        return 8000
    elif golongan == "D":
        return 10000
    else:
        return 0

def hitung_gaji():
    upah = golongan(gol)
    if jam_kerja > 48:
        lembur = (jam_kerja - 48) * 4000
        total_upah = (48 * upah) + lembur
    else:
        total_upah = upah * jam_kerja
    return total_upah


print(nama, "menerima upah Rp.", hitung_gaji(), "per minggu")