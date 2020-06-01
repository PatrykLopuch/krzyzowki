import random


file = open("skrocone_baza.txt", "r+")
lines = file.readlines()
file.seek(0)


losowe = []
for x in range(450):
    losowe.append(lines[random.randint(0,1500000)])
file.truncate()    
file.writelines(losowe)
file.close()