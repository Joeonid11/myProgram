print(50*'=')
print('MY SIMPLE CALCULATOR')

bil1 = int(input('bilangan pertama : '))
bil2 = int(input('bilangan kedua : '))
int(bil1)
int(bil2)

print('[1]Perkalian')
print('[2]Pembagian')
print('[3]pengurangan')
print('[4]penjumlahan')
choice = int(input('pilih salah satu operator diatas \npilihanmu ? ',))

if choice == 1:
    print('hasil dari', bil1, 'x', bil2, '=', bil1*bil2)
elif choice == 2:
    print('hasil dari', bil1, '/', bil2, '=', bil1/bil2)
elif choice == 3:
    print('hasil dari', bil1, '-', bil2, '=', bil1-bil2)
elif choice == 4:
    print('hasil dari', bil1, '+', bil2, '=', bil1+bil2)
else:
    print('pilihanmu tidak ada')

print('=='*20)
