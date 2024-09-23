'''
lol = input("Berikan kata-kata: ")

list_lol = []
list_lol[:0] = lol
print(list_lol)
temp = ""

for i in range(lol):
    temp = list_lol[0]
    list_lol[0] = list_lol[len(lol)-1]
    list_lol[len(lol)-1] = temp

print(list_lol)

TUGAS TUKER index string

'''


kata = input()
angka = int(input())


for i in range(angka):
    kata = kata[1:] + kata[0]

print(kata)


