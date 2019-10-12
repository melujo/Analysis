def format(a,b,c):
    return (str(a) + " x 100, " + str(b) + " x 20, " + str(c) + " x 1")
def allposibilities(x,y,z):
    e,f = y,z
    
    allPossibList = []
    while True:
        if z > 0:
            allPossibList.append([x,y,z])
            z -= 1
        elif y > 0 and z == 0:
            allPossibList.append([x,y,z])
            y -= 1
            z = f
        elif x > 0 and y == 0 and z == 0:
            allPossibList.append([x,y,z])
            z = f
            y = e
            x -= 1
        elif x == 0 and y == 0 and z == 0:
            allPossibList.append([x,y,z])
            break



    return allPossibList 


count = 0
print("Please enter the value of the bill you have to pay")
amount = int(input(">>> "))
print("Please enter the amount of 100, 20 and 1 banknotes in your wallet")
p = int(input(">>> "))
q = int(input(">>> "))
r = int(input(">>> "))
print("")
poslist = []
allPossibList = allposibilities(p,q,r)
cap = p*100 + q*20 + r*1



if cap < amount:
    count = 0
elif cap == amount:
    count = 1
    poslist.append(format(p,q,r))
    
else:
    for i in allPossibList:
        if int(i[0])*100 + int(i[1])*20 + int(i[2])*1 == amount:
                poslist.append(format(i[0],i[1],i[2]))
                count += 1
            
        
poslist = poslist[::-1]

print("There are " + str(count) + " ways to pay this")
for i in poslist:
    
    print(i)
