x = 2
y = 1000

z = pow(x,y)
print("Sayımız: ", z)

sayi = str(z)
toplam = 0
for rakam in sayi:
    toplam += int(rakam)

print("Sayının rakamları toplamı:", toplam)