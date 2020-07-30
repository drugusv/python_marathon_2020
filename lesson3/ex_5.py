# numarul de litere, cifre si alte simboluri din text

def caractere(s):
    cifre = 0
    litere = 0
    alte = 0
    for i in s :
        if i.isalpha():
            litere += 1
        elif i.isdigit():
            cifre += 1
        else:
            alte += 1
    return('Cifre:',cifre, 'Litere:',litere, 'Alte simboluri:',alte)

s = input("Introduceti un text: ")
print (caractere(s))