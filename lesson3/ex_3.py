#divizorii unui numar

def Divizor(n):
     return n
n = int(input("Introduceti un numar intreg: "))
print("Divizorii sunt: ")
for i in range(1,n,1):
    if n % i == 0:
        print(i)
print(n)