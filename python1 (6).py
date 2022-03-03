# Mahasena

n = int(input())
a = list(map(int, input().split()))[:n]
Ecount = 0
Ocount = 0
for i in a:
    if i % 2 == 0:
        Ecount += 1
    else:
        Ocount += 1
if Ecount > Ocount:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
