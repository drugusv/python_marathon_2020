#suma numereleor intre 1000 si 2300

sum = 0
for i in range(1000,2300):
    if (i % 5 == 0) and (i % 7 == 0):
        sum = sum + i
print(sum)