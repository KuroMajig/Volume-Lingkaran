import math
#masukkan jari jari lingkaran

r = float(input ("masukkann jari-jari lingkaran: "))

#hitung Luas lingkaran
luas = math . pi * r**2

#hitung keliling lingkaran
keliling = 2 * math.pi *r

#hasil 
print (f" luas lingkaran :{luas:.2f}")
print (f"Keliling lingkaran: {keliling:.2f}")