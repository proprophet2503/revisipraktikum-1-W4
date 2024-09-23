test_cases = int(input("Enter the test cases:"))

row = []
col = []
for i in range(0, test_cases):
    baris, kolom = (map(int, input().split(' ')))
    row.append(baris)  
    col.append(kolom)  


try:
    for baris in row:
        baris>= 4
    
    for kolom in col:
        kolom>= 6
except:
    print(f"Test Cases isn't matched with the amounts of rows and collums: ")

'''

row = [4, 6]
col = [6, 8]



4, 6:

* ****   i = 1, 
** ***   i = 2, 
*** **   i = 3  
**** *   i = 4   


'''

for baris, kolom in zip(row, col):  # loop secara bersama, karena jika diinput seperti contoh (row = [4, 6]col = [6, 8]) supaya row[i] dengan col[i] berpasangan tak berubah
    print()  # newline untuk pattern selanjutnya 
    for i in range(baris):  
        for j in range(kolom):  
            if j == i+1:  
                print(" ", end="")
            else:
                print("*", end="")
        print()  # Move to the next line after inner loop
        



