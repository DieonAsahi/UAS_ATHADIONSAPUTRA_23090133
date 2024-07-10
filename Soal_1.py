# mahasiswa_manager.py

# Inisialisasi dictionary untuk menyimpan data mahasiswa
mahasiswa = {}

def tambah_mahasiswa(nim, nama):
    """Menambahkan data mahasiswa."""
    if nim in mahasiswa:
        print(f"Mahasiswa dengan NIM '{nim}' sudah ada. Mengupdate nama.")
        mahasiswa[nim] = nama
    else:
        mahasiswa[nim] = nama
    print(f"Mahasiswa dengan NIM '{nim}' dan nama '{nama}' berhasil ditambahkan/diupdate.")

def tampilkan_mahasiswa():
    """Menampilkan semua data mahasiswa."""
    if mahasiswa:
        print("Daftar mahasiswa:")
        for nim, nama in mahasiswa.items():
            print(f"- NIM: {nim}, Nama: {nama}")
    else:
        print("Tidak ada data mahasiswa.")

def menu():
    print("\nManajemen Data Mahasiswa")
    print("1. Tambah Data Mahasiswa")
    print("2. Tampilkan Data Mahasiswa")
    print("3. Keluar")

def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1-3): ")
        
        if pilihan == '1':
            while True:
                nim = input("Masukkan NIM: ")
                nama = input("Masukkan nama mahasiswa: ")
                tambah_mahasiswa(nim, nama)
                
                tambah_lagi = input("Ingin tambah mahasiswa lagi? (y/n): ").lower()
                if tambah_lagi != 'y':
                    break
        
        elif pilihan == '2':
            while True:
                tambah_sebelum = input("Ingin menambahkan mahasiswa sebelum menampilkan data? (y/n): ").lower()
                if tambah_sebelum == 'y':
                    nim = input("Masukkan NIM: ")
                    nama = input("Masukkan nama mahasiswa: ")
                    tambah_mahasiswa(nim, nama)
                else:
                    break
            tampilkan_mahasiswa()
        
        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
