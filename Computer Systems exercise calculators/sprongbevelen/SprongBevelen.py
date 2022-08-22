import sys
from textwrap import wrap

def __formaat__(getal,aanvulling):
        uit = ""
        if(len(str(getal))>8):
            return getal[-8:]
        for x in range(8-len(str(hex(int(getal,16))[2:]))):
            uit += str(aanvulling)
        uit+=str(hex(int(getal,16)))[2:]
        return uit

minEenOfNiet = 0
minEenOfNiet2 = 0
lijst = []
bevelregister1 = ""
bevelregister2 = ""
bevelregister3 = ""
bevelregister4 = ""
bevelenteller1 = 0
bevelenteller2 = 0
bevelenteller3 = 0
bevelenteller4 = 0


with open("input9.txt","r") as file:
    for lijn in file:
            lijst.append(lijn.strip('\n').replace("         ",""))
#print(lijst)

for x in range(len(lijst)):
    if 'j' in lijst[x]:
        getal = x
        
bg = (lijst[0])
lijst2 = lijst[2:getal+1]
lijst3 = lijst[-1]
print("begin is",bg)
print("ingegeven bevelen:\n")
for x in lijst[1:]:
    print(x,'\n')
    
teller =0

for x in lijst2:
    teller += int((len(x.split("]",1)[0])-1)/2)
    #beginGetalHex = "0x"+bg
    if(x.find("j")):
        sprong = x.split("[")[1].split("]")[0]
        sprong = wrap(sprong,2)[::-1]

sprongUit=""
for x in sprong:
    sprongUit +=x

if sprong[0] == '00':
    sprongUit = __formaat__(sprongUit,"0")
elif bin(int(sprongUit,16))[2] == "1":
    sprongUit = __formaat__(sprongUit,"f")
else:
    print("fout bij formateren lijn 60")


      
bevelenteller1 = hex(int(bg,16) + teller)
bevelregister1 =bevelregister2 =  lijst2[-1].split(" ")[0]
bevelenteller2= hex(int(bevelenteller1,16)+int(sprongUit,16))


if'[' in lijst[getal+1].split(" ")[0]:
    bevelenteller3 = hex(int(bevelenteller1,16)+int(len(lijst[getal+1].split(" ")[0])/2)-1)
    minEenOfNiet = int(len(lijst[getal+1].split(" ")[0])/2)-1
else:
    bevelenteller3 = hex(int(bevelenteller1,16)+int(len(lijst[getal+1].split(" ")[0])/2))
        
bevelregister3 = lijst[getal+1].split(" ")[0]


if'[' in lijst3.split(" ")[0]:
    bevelenteller4 = hex(int(bevelenteller2,16)+int(len(lijst3.split(" ")[0])/2)-1)
    minEenOfNiet2 = int(len(lijst3.split(" ")[0])/2)-1
else:
    bevelenteller4 = hex(int(bevelenteller2,16)+int(len(lijst3.split(" ")[0])/2))
bevelregister4 = lijst3.split(" ")[0]



print("bevelenteller 1 berekening",hex(int(bg,16)) ,"+", hex(teller),"=",bevelenteller1)
print("bevelenteller 2 berekening",bevelenteller1,"+",hex(int(sprongUit,16)),"=",bevelenteller2)
print("bevelenteller 3 berekening",bevelenteller1 ,"+", minEenOfNiet,"=",bevelenteller3)
print("bevelenteller 4 berekening",bevelenteller2,"+", minEenOfNiet2,"=",bevelenteller4)



#indien sprongUit oftewel de sprong negatief is moet je iets anders doen moet nog nakijken
        
print("rij 1 is bevelenteller:",__formaat__(bevelenteller1,0),'\t',"bevelregister:",bevelregister1,)
print("rij 2 is bevelenteller:",__formaat__(bevelenteller2,0),'\t',"bevelregister:",bevelregister2,'\n')
print("rij 3 is bevelenteller:",__formaat__(bevelenteller3,0),'\t',"bevelregister",bevelregister3)
print("rij 4 is bevelenteller:",__formaat__(bevelenteller4,0),'\t',"bevelregister",bevelregister4)

#neemt hex getal returned geformateerd getal
