test_cases = int(input("Enter the test cases:"))


row = []
col = []
for i in range(0, test_cases):
    r, c = (map(int, input().split(' ')))
    row.append(r)  
    col.append(c)  


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

for r in row:
    
    for c in col:
        
        
        for i in range(r):  
            for j in range(c):  
                if (j == i+1):
                    print(" ", end="")
                else:
                    print("*", end="")
            print()
        
        
    




