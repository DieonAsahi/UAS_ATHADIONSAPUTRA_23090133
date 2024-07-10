from mangga import Mangga

def tambah_buah():
    nama = input("Masukkan nama buah: ")
    jenis = input("Masukkan jenis mangga: ")
    return Mangga(nama, jenis)

def main():
    print("=== Menambahkan Buah Mangga ===")
    mangga1 = tambah_buah()

    print("\n=== Deskripsi Buah Mangga ===")
    print(mangga1.deskripsi())

if __name__ == "__main__":
    main()
