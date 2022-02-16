# KAMUS
# img = gambar
# decoder = built in function open cv
# data = Decode text
# point = array simpul/ver

import cv2
import webbrowser
# mendapatkan akses fungsi untuk kode dari modul Open Cv dan web browser

img = cv2.imread("C:/Users/LENOVO/Documents/CODE/TUGAS AKSANTARA/THT OPREC/QR CODE.png")
# membaca gambar yang diberikan dan di-assign sebagai img
# !!! path image harus diperbarui sebelum run program !!! 

decoder = cv2.QRCodeDetector()
# QRCodeDetector adalah detector QR code bulit in dari Open CV
# di assign sebagai decoder
 
data, points, _ = decoder.detectAndDecode(img)
# detectAndDecode() menerima input gambar dan mengembalikan tuple berisi 3 variabel
# data = Decoded text
# points = Output array simpul dari kode QR yang ditemukan
# yang ketiga optional, output gambar berisi kode QR yang diperbaiki dan dibinerisasi

print(f'Decoded data: {data}')  # output link/ data
webbrowser.open(data)   # fungsi open browser diambil dari modul webbrowser