def checkGrote(x):
    if "dword" in x:
        return "4"
    for reg in registers:
        if reg in x:
            return "4"
    for reg in halveReg:
        if reg in x:
            return "2"
    for reg in kwartReg:
        if reg in x:
            return "1"


registers = ["eax","ebx","ecx","edx"]
halveReg = ["ax","bv","cx","dx"]
kwartReg = ["ah","al","bh","bl","ch","cl","dh","dl"]

bevelenPush = []
bevelenPop = []
tellerPush = 0
tellerPop = 0
beweging = 0
beginPointer = 0
with open("input.txt","r") as file:
    for line in file:
        print(line)
        if 'ESP' in line:
            beginPointer = hex(int(line.strip()[3:],16))
        if 'push' in line:
            bevelenPush.append(line.strip())
        if 'pop' in line:
            bevelenPop.append(line.strip())

print("############ BEREKENINGEN ##################(alle pushes eerst en dan alle pops)")
for x in bevelenPush:
    
    tellerPush = tellerPush + int(checkGrote(x))
    print(x,"DUS",checkGrote(x))


for x in bevelenPop:
    tellerPop = tellerPop + int(checkGrote(x))
    print(x,"DUS",checkGrote(x))


print("Totaal Pop=",tellerPop,"en het Totaal Push=",tellerPush)

beweging = tellerPop - tellerPush
print("############ UITKOMST ##################")
print(hex(int(beginPointer,16) + beweging)[2:])

einde = input()
