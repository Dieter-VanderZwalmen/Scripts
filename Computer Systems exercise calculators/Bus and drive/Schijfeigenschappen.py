#Schijfeigenschappen


print("geef snelheid in t/m")
snelheid = int(input())
print("geef Sectoren/spoor")
SectorenSpoor = int(input())
print("Sector grootte in bytes")
SectorGrootte = int(input())


RotationeleWachtijd = ((1/(snelheid/60)/2)*1000)
SectorLeestijd= (RotationeleWachtijd*2)/SectorenSpoor
Debiet= (((snelheid/60000)*SectorenSpoor)*SectorGrootte)/1024/1024*1000


print(RotationeleWachtijd)
print(SectorLeestijd)
print(Debiet)



