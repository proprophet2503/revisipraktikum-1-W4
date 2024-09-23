'''
idea: 
iterate through the list with loops, 
find the colors code with the most rooms
erase the most colors from the loops and
count the rest of the list len 

'''

def findrooms_tochange(rooms_colors_id):
    counter = [0]*1000001

    for colors_id in rooms_colors_id:
        counter[colors_id] += 1       # array counter menyimpan jumlah setiap elemen di rooms_colors_id

    highest = 0 

    for jumlah_id in counter:
        if (jumlah_id > highest):
            highest = jumlah_id

    room_chosen_color = 0

    for i in range (len(counter)):
        if (counter[i] == highest):
            room_chosen_color = i
            
            
    
    # menghapus warna yang dipilih agar bisa sisanya bisa dihitung untuk mendapatkan banyaknya room yang harus diubah

    rooms_needs_to_change = [x for x in rooms_colors_id if x != room_chosen_color]

    return len(rooms_needs_to_change)




amount_of_rooms = int(input("Input the amount of rooms: "))
rooms_colors_id = list(map(int, input().split(' ') ))

if (len(rooms_colors_id) != amount_of_rooms):
    raise Exception("Enter the same amount of rooms colors id as the amount of rooms you input!")

total_rooms_needs_to_change = findrooms_tochange(rooms_colors_id)

print(total_rooms_needs_to_change)

