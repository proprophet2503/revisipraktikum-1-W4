import sys

def ubah_string (string_akan_diubah, jumlah_perubahan):
    hasil = []

    for char in string_akan_diubah:
        if 'a' <= char <= 'z':  # karakter rendah agar tanda-tanda tidak berubah harus dibatasi
            string_terubah = chr((ord(char) - ord('a') + jumlah_perubahan) % 26 + ord('a'))
            hasil.append(string_terubah)    # nambahin karakter yang sudah diubah ke list agar kembali menjadi kalimat
        elif 'A' <= char <= 'Z': # karakter kapital agar tanda-tanda (whitespace, %) tidak berubah
            string_terubah = chr((ord(char) - ord('A') + jumlah_perubahan) % 26 + ord('A'))
            hasil.append(string_terubah)
        else:
             hasil.append(char)
    return ''.join(hasil)    # mengubah list menjadi string kembali 



cmd, k = map(int, input().split(' '))

string_0 = sys.stdin.read()

hasil_ubah_string = ubah_string(string_0, k)

print(hasil_ubah_string)

