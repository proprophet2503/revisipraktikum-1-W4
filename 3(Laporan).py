
jenis_batu = input("")
jenis_batu = list(jenis_batu)

total_batu = len(jenis_batu)


jotaro_error_count = 0
i = 0


total_kerugian = 0
# total_kerugian = ascii jenis batu i * 1000 + jenis_batu i+1 * 1000
while i < len(jenis_batu)-1 :
    if(jenis_batu[i] == jenis_batu[i+1]):

        total_batu-=2
        jotaro_error_count+=1
        total_kerugian+= ord(jenis_batu[i])*1000 + ord(jenis_batu[i+1])*1000

        del jenis_batu[i:i + 2]
    else:
        i+= 1

   
print(f"Di gudang tersisa {total_batu} batu.")
if(total_kerugian>0):
    print(f"Total Kerugian: {total_kerugian} Dolar Imu")
if (jotaro_error_count == 0):
    print("Wah, Jotaro Joemama tidak jadi dipecat")
else:
    print("Wah, Jotaro Joemama dipecat")

