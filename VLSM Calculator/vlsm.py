#Hoeveel bits vereist voor  het aantal hosts 
def getBits(x):
	getal = 2**1
	bits = 1
	#print(getal,bits)
	while(getal<x+2):
	    getal = 2**bits
	    bits +=1
	    #print(getal,bits)
	
	
	return bits-1

def getAdresZonderMask(adres):
    return adres[:adres.find("/")]


def toIpAdres(adr):
    y= ""

    if "0b" in adr:
        adr = adr[2:]
    adress = [int(adr[:8],2),int(adr[8:16],2),int(adr[16:24],2),int(adr[24:32],2)]

    for x in adress:
        y += "."+str(x)
    return y[1:]

#22.11.192.0 neemt deze vorm
def naarBinair(adr):
        y = ""
        for x in adr.split("."):
                string = str(bin(int(x)))
                y +=string[2:].rjust(8,"0")

        return y
    
ipRange = "22.11.192.0/18"
Netwerken = {"A":4,
             "B":34,
             "C":300,
             "D":4,
             "E":1048,
             "F":33,
             "G":456,
             "H":90}


berekenIP = ipRange


print("lijst sorteren:")
Netwerken = sorted(Netwerken.items(), key=lambda x: x[1], reverse=True)

for i in Netwerken:
	print(i[0], i[1])



print("\n berekenen hoeveel bits je nodig hebt per netwerk")
subnetMasks = {}
for i in Netwerken:
    aantalHosts = i[1]
    aantalBits = getBits(aantalHosts)
    subnetMasks[i[0]] = 32-aantalBits
    print("voor netwerk",i,"heb je bits nodig:",aantalBits,"\n",2**aantalBits,">",i[1]+2,">",2**(aantalBits-1)) 

for i in subnetMasks:
    print(i,"Heeft als subnet Mask /",subnetMasks.get(i))
    
print("\n")
adres = ""
for netwerk,subnetMask in zip(Netwerken,subnetMasks):
    print("\nnetwerk:",netwerk[0],"\n")
    if adres != "":
            adres = int(broadcast,2) + 1
            adres = bin(adres)
            adres = str(adres)[2:].rjust(32,"0")
            adres = toIpAdres(adres)
            adres += "/xx"

    else:
            adres = ipRange
            
    print("adres = ",adres)
    mask = subnetMasks.get(subnetMask)
    print("mask = ",mask)
    
    ipAdres = getAdresZonderMask(adres)
    #print("ipAdresZonderMask",ipAdres)
    
    ipAdresBinair = naarBinair(ipAdres)
    print("ipAdresBinair",ipAdresBinair)

    
    eersteAdres = int(ipAdresBinair,2) + 1
    eersteAdres = bin(eersteAdres)
    eersteAdres = str(eersteAdres)[2:].rjust(32,"0")
    print("1ste = ",[eersteAdres[i:i+8] for i in range(0, len(eersteAdres), 8)])
    eersteAdres = toIpAdres(eersteAdres)
    print("1ste = ",eersteAdres)

    
    laatsteAdres = ipAdresBinair[:mask].ljust(31,"1") + "0"
    print("laatste = ",[laatsteAdres[i:i+8] for i in range(0, len(laatsteAdres), 8)])
    print("laatste = ",toIpAdres(laatsteAdres))

    
    broadcast = ipAdresBinair[:mask].ljust(32,"1")
    print("broadcast = ",[broadcast[i:i+8] for i in range(0, len(broadcast), 8)])
    print("broadcast = ",toIpAdres(broadcast))
    
