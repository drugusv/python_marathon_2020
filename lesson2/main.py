print("Exercitiul 1")
a = 10
a += len(str(a))
a = str(a)
print("Valoarea lui 'a' este: ", a)

print("\nExercitiul 2")
print("In padurea cu alune aveau casa" + ' 2 ' + "pitici")

print("\nExercitiul 3")
a = 10
print(a + 1)

print("\nExercitiul 4")
a = int(input("Scrie un numar: "))
a += 1
print(a)

print("\nExercitiul 5")
file_name = input("Separam extensia fisierului: ")
a = file_name.split(".")
print(a[1])

print("\nExercitiul 6")
a = ['a','b','c','d']
#6.1
print(a[int('3'*2)//11])
# raspunsul este d

#6.2
a.insert(0, 'x')
print(a)

#6.3
a.remove('d')
a.remove('c')
print(a)

#6.4
a.sort(reverse=True)
print(a)

#6.5
b = a.copy()
b.pop(0)
b.pop(1)
print(b)

print("\nExercitiul 7")
inventar = {
    'scaune':20,
    'mese':10,
    'dulapuri':4,
    'paturi':2
    }
print('\nItems: ', inventar.keys())
#sau asa:
print('Items: ')
for keys, values in inventar.items():  #accessing keys
    print(keys, end='.')
print('\nTotal:', sum(inventar.values()))
