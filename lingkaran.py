def jarak_kuadrat(x1, y1, x2, y2):
    return (x2 - x1)**2 + (y2 - y1)**2

def cek_king_kena_ling(x1, y1, xs, ys, xf, yf):
    
    jarak_awal_akhir = jarak_kuadrat(xs, ys, xf, yf)
    
    # jarak kuadrat titik pusat lingkaran dan titik awal
    jarak_ling_awal = jarak_kuadrat(xs, ys, x1, y1)
    
    if(jarak_ling_awal == 0):
        return "No"
    
    # jarak titik pusat lingkaran dan titik akhir
    jarak_ling_akhir = jarak_kuadrat(xf, yf, x1, y1)
    
    if jarak_ling_akhir > jarak_awal_akhir:
        return "Yes"
    else:
        return "No"

x1, y1 = map(int, input().split())

xs, ys = map(int, input().split())

xf, yf = map(int, input().split())

hasil = cek_king_kena_ling(x1, y1, xs, ys, xf, yf)
print(hasil)

