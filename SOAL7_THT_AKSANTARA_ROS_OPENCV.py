# KAMUS
# la = latitude; lo = longitude; al = altitude
# [koordinat][1/2] : 1 = awal; 2 = akhir
# d = jarak

# ALGORITMA
la1,lo1,al1 = input().split(", ")   # input koordinat awal
la2,lo2,al2 = input().split(", ")   # input koordinat akhir
# sesuai contoh input antar bilangan terdapat ", "

d = (((float(la1)-float(la2))**2) + ((float(lo1)-float(lo2))**2) + ((float(al1)-float(al2))**2))**0.5
# rumus mencari jarak d = sqrt((delta(la))^2 + (delta(lo))^2 + (delta(al))^2)

print(f"{d:.2f}")   # output
# menyesuaikan dengan contoh output pembulatan 2 dibelakang koma