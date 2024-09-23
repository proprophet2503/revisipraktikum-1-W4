max_index = int(input("Input the amounts of elements in the lists: "))

A = []
B = []

print(f"Input {max_index} elements for list A: ")
for i in range (max_index):
    a = int(input())
    A.append(a)

print(f"Input {max_index} elements for list B: ")
for i in range (max_index):
    b = int(input())
    B.append(b)


total_sub_array = int(input("Input the amount of subarrays that's going to be created: "))


print("Input the range of index for the subarrays")

L = []
R = []

for i in range (total_sub_array):

    l, r = map(int, input().split(' '))
    L.append(l)
    R.append(r)

count_A = 0
count_B = 0

for awal, akhir in zip(L, R):
    for i in range (awal, akhir):

        count_A+= A[i]
        count_B+= B[i]

    if(count_A == count_B):
        print("YA")
    else:
        print("TIDAK")


