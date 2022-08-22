from decimal import Decimal

print("geef 0 als waarde voor onbekende")
#print("Snelheid in MT/s debiet in MB/s en Breedte in Bits")
print("breedte in bits:")
breedte= Decimal(input())
print("snelheid in MT/S:")
snelheid = Decimal(input())
print("debiet in MB/s:")
debiet = Decimal(input())


if(breedte == 0):
    print((debiet/snelheid)*8)
if(snelheid == 0):
    print(debiet*(8/breedte))
if(debiet == 0):
    print((breedte/8)*snelheid)
