Ucup_HP = int(input())
Ucup_AP = 100
minion_HP, minion_AP = 100, 2
knight_HP, knight_AP = 500, 5

knight_iblis = int(input())
minion_iblis = int(input())

raja_iblis_HP, raja_iblis_AP = 1000, 100

total_minion = minion_iblis//2
total_knight = knight_iblis//2

if(Ucup_HP>0):
    Ucup_HP -= (total_knight*knight_AP*5)
    if(Ucup_HP>0):
        Ucup_HP-= (total_minion*minion_AP)
        if(Ucup_HP>0):
            Ucup_HP-= raja_iblis_AP*10
            if(Ucup_HP>0):
                print(f"Yey! Ucup Menang! HP tersisa: {Ucup_HP}")
            else:
                print("Yah! Ucup Meninggoy.")
        else:
            print("Yah! Ucup Meninggoy.")
    else:
        print("Yah! Ucup Meninggoy.")
else:
    print("Yah! Ucup Meninggoy.")


